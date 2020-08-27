# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render
from django.template import RequestContext, loader
import json
from django.views.decorators.cache import cache_page
from django.contrib.admin.views.decorators import staff_member_required
from django.core.files.uploadedfile import UploadedFile
import os, datetime, time, zipfile, sys, glob, settings
from data_manager.models import *
from data_manager.forms import *


#@cache_page(60 * 60 * 24, key_prefix="data_manager_get_json")
def get_json(request, project=None):
    from mp_settings.models import MarinePlannerSettings
    try:
        if project:
            activeSettings = MarinePlannerSettings.objects.get(slug_name=project)
        else:
            activeSettings = MarinePlannerSettings.objects.get(active=True)
        #if activeSettings.table_of_contents is not None:
        layer_list = []
        themes = activeSettings.table_of_contents.themes.all()
        for theme in themes:
            for layer in theme.layers.all().order_by('name').order_by('order'):
                layer_list.append(layer.toDict)
            for subtheme in theme.subthemes.all():
                for layer in subtheme.layers.all().order_by('name').order_by('order'):
                    layer_list.append(layer.toDict)

        json_response = {
            "state": { "activeLayers": [] },
            "layers": layer_list,
            "themes": [theme.toDict for theme in themes.order_by('display_name').order_by('order')],
            "success": True
        }
        return HttpResponse(json.dumps(json_response))
    except:
        pass

    json_response = {
        "state": { "activeLayers": [] },
        "layers": [layer.toDict for layer in Layer.objects.filter(is_sublayer=False).exclude(layer_type='placeholder').order_by('name').order_by('order')],
        "themes": [theme.toDict for theme in TOCTheme.objects.all().order_by('display_name')],
        "success": True
    }
    return HttpResponse(json.dumps(json_response))


def create_layer(request):
    if request.POST:
        try:
            url, name, type, themes = get_layer_components(request.POST)
            layer = Layer(
                url = url,
                name = name,
                layer_type = type
            )
            layer.save()

            for theme_id in themes:
                theme = Theme.objects.get(id=theme_id)
                layer.themes.add(theme)
            layer.save()

        except Exception as e:
            return HttpResponse(e, status=500)

        result = layer_result(layer, message="Saved Successfully")
        return HttpResponse(json.dumps(result))


def update_layer(request, layer_id):
    if request.POST:
        layer = get_object_or_404(Layer, id=layer_id)

        try:
            url, name, type, themes = get_layer_components(request.POST)
            layer.url = url
            layer.name = name
            layer.save()

            for theme in layer.themes.all():
                layer.themes.remove(theme)
            for theme_id in themes:
                theme = Theme.objects.get(id=theme_id)
                layer.themes.add(theme)
            layer.save()

        except Exception as e:
            return HttpResponse(e, status=500)

        result = layer_result(layer, message="Edited Successfully")
        return HttpResponse(json.dumps(result))


def get_layer_components(request_dict, url='', name='', type='XYZ', themes=[]):
    if 'url' in request_dict:
        url = request_dict['url']
    if 'name' in request_dict:
        name = request_dict['name']
    if 'type' in request_dict:
        type = request_dict['type']
    if 'themes' in request_dict:
        themes = request_dict.getlist('themes')
    return url, name, type, themes


def layer_result(layer, status_code=1, success=True, message="Success"):
    result = {
        "status_code":status_code,
        "success":success,
        "message":message,
        "layer": layer.toDict,
        "themes": [theme.id for theme in layer.themes.all()]
    }
    return result

def load_config(request):
    import json
    import os
    from django.core.exceptions import ObjectDoesNotExist
    from django.template.defaultfilters import slugify

    json_data = open('data_manager/fixtures/wa_config.json')
    wa_config = json.load(json_data)
    toc_obj = wa_config['Themes'][0]['Marine Spatial Planning']['TOC'][0]
    layers = wa_config['layersNew']
    base_url = wa_config['DNRAGSServiceURL']

    try:
        toc = TOC.objects.get(name='WA_CMSP')
    except ObjectDoesNotExist:
        toc = TOC(name='WA_CMSP')
        toc.save()
    for layer_name, layer_obj in layers.iteritems():
        if 'url' in layer_obj and layer_obj['url'] != "":
            relative_url = layer_obj['url'].replace('DNRAGSServiceURL/','')
            absolute_url = os.path.join(base_url, relative_url, 'export')
            try:
                layer = Layer.objects.get(name=layer_name)
            except ObjectDoesNotExist:
                layer = Layer(name=layer_name, layer_type='ArcRest', url=absolute_url, arcgis_layers='0')
                layer.save()

    for theme_name, layer_list in toc_obj.iteritems():
        try:
            theme = TOCTheme.objects.get(display_name=theme_name)
        except ObjectDoesNotExist:
            theme = TOCTheme(display_name=theme_name, name=slugify(theme_name))
            theme.save()
        for layer_obj in layer_list:
            try:
                layer = Layer.objects.get(name=layer_obj['layerID'])
                theme.layers.add(layer)
            except ObjectDoesNotExist:
                pass
        theme.save()
        toc.themes.add(theme)
    return HttpResponse('layers and themes successfully loaded into WA_CMSP TOC object', status=200)


def import_export_admin(
    request,
    template_name='admin/import_export_admin.html',
    extra_context={}):

    if request.method == 'POST':
        form = UploadContentsForm(request.POST, request.FILES)
        if form.is_valid():
            handle_imported_content_file(request.FILES['file'], request.user)
            return HttpResponseRedirect('/admin/port_data_manager/')    # success url
    else:
        form = UploadContentsForm()
    if len(ImportEvent.objects.all()) == 0:
        fixture = create_new_fixture(request.user, 'initial')
        initial_contents = create_initial_contents(fixture, request.user)
        set_import_as_current(initial_contents)

    current_fixture = ImportEvent.objects.filter(current=True)[0]

    snapshots = [x for x in ImportEvent.objects.filter(status='complete').order_by('date_created')]

    context = {
        'form': form,
        'current_fixture': str(current_fixture.data_file),
        'snapshots': snapshots
    }

    context.update(extra_context)
    return render(request, template_name, context)

import_export_admin = staff_member_required(import_export_admin)

'''
import zipped shapefile in EPSG:3857 to be new planning unit layer
'''
def import_report_hex(
    request,
    template_name='admin/import_planning_units_admin.html',
    extra_context={}):

    if request.method == 'POST':
        form = UploadContentsForm(request.POST, request.FILES)
        if form.is_valid():
            import_status = handle_imported_planning_units_file(request.FILES['file'], request.user)
            print(import_status['message'])
            extra_context = {
                'status': import_status['state'],
                'message': import_status['message']
            }

    else:
        form = UploadContentsForm()

    context = {
        'form': form
    }

    context.update(extra_context)
    return render(request, template_name, context)

import_report_hex = staff_member_required(import_report_hex)

'''
dump current data_manager data to a file to rebuild on import failure
'''
def create_new_fixture(user, filename):
    from django.core import management
    fixture_file = '/tmp/data_manager_%s_%s.json' % (filename, str(int(time.time()*1000)))
    with open(fixture_file, 'w') as f:
        management.call_command('dumpdata', 'mp_settings', 'data_manager', format='json', indent=2, exclude=['data_manager.ImportEvent'], stdout=f)
    return fixture_file

'''
If no initial import event is available, create one so the user can revert back to a working original
'''
def create_initial_contents(fixture, user):
        from django.core.files.base import File
        file_obj = open(fixture, 'r')
        init_event = ImportEvent.objects.create(
            status='complete',
            notes='Autogenerated: Original state',
            user=user,
            data_file=open(file_obj)
        )
        file_obj.close()
        return init_event

'''
given a data_manager fixture file name, load the data into the database
fixture must be a string of the file location.
'''
def load_contents_fixture(fixture):
    from django.core import management
    from django.db.models.fields.files import FieldFile

    #fixture should be a string of the file location. If not...
    if type(fixture) == ImportEvent:
        fixture = fixture.data_file
    if type(fixture) == FieldFile:
        fixture = fixture.file.name     # doesn't work - need abs path to be sure.

    # some models assume a relative path of '../media/'', though media_root is likely pointing at '../mediaroot/'
    fixture = str.replace(fixture,'../media/',settings.MEDIA_ROOT)

    try:
        management.call_command('loaddata', fixture)
    except:
        return False
    return True

'''
Clean out all data_manager models except for ImportEvents
'''
def clean_data_manager_models():
    DataNeed.objects.all().delete()
    LookupInfo.objects.all().delete()
    AttributeInfo.objects.all().delete()
    Layer.objects.all().delete()
    Theme.objects.all().delete()
    TOCTheme.objects.all().delete()
    TOCSubTheme.objects.all().delete()
    TOC.objects.all().delete()

'''
record the import event and attempt to load the data_manager data into the database
'''
def handle_imported_content_file(import_file, user):
    import json
    backup_file = create_new_fixture(user, 'backup')

    if len(ImportEvent.objects.all()) == 0:
        create_initial_contents(backup_file, user)

    import_event = ImportEvent.objects.create(
        status='pending',
        user=user,
        data_file=import_file
    )
    clean_data_manager_models()

    uploaded_file_location = '../media/%s' % str(import_event.data_file)

    import_success = load_contents_fixture(uploaded_file_location)
    if import_success:
        set_import_as_current(import_event)
        setattr(import_event, 'status', 'complete')
    else:
        setattr(import_event, 'status', 'failed')
        load_contents_fixture(backup_file)
    import_event.save()

'''
set one (and only one) import event as the current event
'''
def set_import_as_current(import_event):
    for event in ImportEvent.objects.filter(current=True):
        setattr(event, 'current', False)
        event.save()
    setattr(import_event, 'current', True)
    import_event.save()

def get_current_fixture(request):
    now = datetime.datetime.now().date()
    fixture = create_new_fixture(request.user, 'current')
    fixture_file = open(fixture, 'r')
    response = HttpResponse(content=fixture_file.read())
    fixture_file.close()
    response['X-Sendfile'] = fixture
    response['Content-Type'] = 'application/json'
    response['Content-Length'] = os.path.getsize(fixture)
    response['Content-Disposition'] = 'attachment; filename="data_manager_current_%s_%s_%s.json"' % (str(now.year), str(now.month), str(now.day))# % fixture
    return response

def create_data_manager_snapshot(request):
    fixture = create_new_fixture(request.user, 'snapshot')
    fixture_file = UploadedFile(open(fixture))
    handle_imported_content_file(fixture_file, request.user)
    return HttpResponseRedirect('/admin/port_data_manager/')

def data_manager_make_current(request, import_id):

    try:
        import_event = ImportEvent.objects.get(id=import_id)
        backup_event = ImportEvent.objects.get(current=True)
        clean_data_manager_models()
        import_success = load_contents_fixture(import_event.data_file.file.name)
        print(import_event.data_file.file.name)


        if import_success:
            set_import_as_current(import_event)
        else:
            load_contents_fixture(backup_event)
            set_import_as_current(backup_event)
    except:
        return HttpResponse('Error 500: Internal Server Error - Failed to make given snapshot current.')
    return HttpResponseRedirect('/admin/port_data_manager/')

def handle_imported_planning_units_file(import_file, user):
    error_message = "Unknown error importing zipfile. Please contact site administrator at %s" % settings.HELP_EMAIL

    #   * test if it is unzippable
    if not zipfile.is_zipfile(import_file):
        error_message = "File is not a zipfile (.zip)"
        return {'state': False, 'message': error_message}

    #   * unzip
    try:
        with zipfile.ZipFile(import_file) as shapezip:
            shapezip.extractall("../media/extracted/")
    except:
        error_message = "Failed to unzip zipfile."
        return {'state': False, 'message': error_message}

    #   * test if right files exist
    if not (
        os.path.isfile('../media/extracted/%s.cpg' % settings.PLANNING_UNIT_FILENAME) and
        os.path.isfile('../media/extracted/%s.dbf' % settings.PLANNING_UNIT_FILENAME) and
        os.path.isfile('../media/extracted/%s.prj' % settings.PLANNING_UNIT_FILENAME) and
        os.path.isfile('../media/extracted/%s.shp' % settings.PLANNING_UNIT_FILENAME) and
        os.path.isfile('../media/extracted/%s.shx' % settings.PLANNING_UNIT_FILENAME)
    ):
        error_message = "Zipfile does not contail all required filetypes: cpg, dbf, prj, shp, shx"
        return {'state': False, 'message': error_message}

    #   * test if EPSG:3857
    from osgeo import gdal, ogr, osr
    source_3857 = osr.SpatialReference()
    source_3857.ImportFromEPSG(3857)
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataset = driver.Open(r'../media/extracted/%s.shp' % settings.PLANNING_UNIT_FILENAME)
    layer = dataset.GetLayer()
    spatialRef = layer.GetSpatialRef()
    arcgis_web_merc_wkt = 'PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["WGS_1984",SPHEROID["WGS_84",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]'
    if not (spatialRef.IsSame(source_3857) or spatialRef.ExportToWkt() == arcgis_web_merc_wkt):
        error_message = "Imported shapefile is not projected as EPSG:3857 or as ArcGIS:'WGS 1984 Web Mercator (Auxiliary Sphere)'"
        return {'state': False, 'message': error_message}

    #   * test if correct attributes
    geom = layer[0]
    if not (cmp(geom.keys().sort(),settings.PU_FIELDS.keys().sort())==0):
        error_message = "Incorrect attribute names. Must match: %s" % str(settings.PU_FIELDS.keys())
        return {'state': False, 'message': error_message}

    #   * test if correct data types
    for field in settings.PU_FIELDS.keys():
        fieldType = settings.PU_FIELDS[field]
        if not testFieldType(layer, field, fieldType):
            error_message = "Field type mismatch: %s should be %s" % (field, fieldType)
            return {'state': False, 'message': error_message}

    #   * store backup sql
    try:
        if os.path.isfile('%s' % settings.PU_SQL_LIVE):
            from shutil import copyfile
            copyfile(settings.PU_SQL_LIVE,settings.PU_SQL_BACKUP)
    except:
        error_message = "Unknown error while backing up original SQL file. Contact %s for assistance" % settings.HELP_EMAIL
        return {'state': False, 'message': error_message}

    #   * run process_grid
    process_success = 0
    try:
        import subprocess

        if settings.VIRTUAL_ENV_PYTHON:
            python_exec = settings.VIRTUAL_ENV_PYTHON
        elif 'python' in sys.executable:
            python_exec = sys.executable
        elif os.environ.has_key('VIRTUAL_ENV'):
            python_exec = "%s/bin/python" % os.environ['VIRTUAL_ENV']
        else:
            python_exec = "python"
            for osPath in settings.os.environ['PATH'].split(":"):
                pyBins = glob.glob(osPath+'/python')
                if len(pyBins) > 0:
                    python_exec = pyBins[0]
                    break

        if os.path.isfile('%s' % settings.PU_SQL_LIVE):
            start_time = os.stat(settings.PU_SQL_LIVE).st_mtime
        else:
            start_time = float(datetime.datetime.now().strftime("%s"))
        grid_subprocess = "%s ../media/extracted/%s.shp %s %s" % (settings.PROCESS_GRID_SCRIPT,settings.PLANNING_UNIT_FILENAME,settings.PU_SQL_LIVE,python_exec)
        process_success = subprocess.call(grid_subprocess, shell=True)
        mod_time = os.stat(settings.PU_SQL_LIVE).st_mtime
        if not start_time < mod_time:
            error_message = "Unable to write to SQL file. Please contact %s to fix write permissions for this file" % settings.HELP_EMAIL
            return {'state': False, 'message': error_message}

    except:
        process_success = 1
    if process_success == 1:
        if settings.VIRTUAL_ENV_PYTHON:
            error_message = "Unknown error while processing grid. Contact %s for assistance." % settings.HELP_EMAIL
        else:
            error_message = "VIRTUAL_ENV_PYTHON setting not defined. Request %s configure this." % settings.HELP_EMAIL
        return {'state': False, 'message': error_message}

    #   * run sql load
    load_success = 0
    try:
        load_success = subprocess.call("psql -U %s -d %s -f %s" % (settings.DATABASES['default']['USER'],settings.DATABASES['default']['NAME'],settings.PU_SQL_LIVE), shell=True)
    except:
        load_success = 1
    if load_success == 1:
        #   * if success, groovy, if not restore from backup
        from shutil import copyfile
        copyfile(settings.PU_SQL_BACKUP,settings.PU_SQL_LIVE)
        error_message = "Unknown error while loading new planning units into database. Contact %s for assistance" % settings.HELP_EMAIL
        return {'state': False, 'message': error_message}

    return {'state': True, 'message': 'Planning Units Updated'}

def testFieldType(layer, field, fieldType):
    for geom in layer:
        if geom[field]:
            if type(geom[field]) == fieldType:
                return True
            else:
                return False
    return True #all values are None. While not promising it is technically valid
