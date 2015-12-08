# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.utils import simplejson
from django.views.decorators.cache import cache_page
from django.contrib.admin.views.decorators import staff_member_required
from models import *
from forms import *


#@cache_page(60 * 60 * 24, key_prefix="data_manager_get_json")
def get_json(request, project=None):
    from mp_settings.models import *
    try:
        if project:
            activeSettings = MarinePlannerSettings.objects.get(slug_name=project)
        else:
            activeSettings = MarinePlannerSettings.objects.get(active=True)
        #if activeSettings.table_of_contents is not None:
        layer_list = []
        themes = activeSettings.table_of_contents.themes.all()
        for theme in themes:
            for layer in theme.layers.all().order_by('name'):
                layer_list.append(layer.toDict)
            for subtheme in theme.subthemes.all():
                for layer in subtheme.layers.all().order_by('name'):
                    layer_list.append(layer.toDict)

        json = {
            "state": { "activeLayers": [] },
            "layers": layer_list,
            "themes": [theme.toDict for theme in themes.order_by('display_name')],
            "success": True
        }
        return HttpResponse(simplejson.dumps(json))
    except:
        pass

    json = {
        "state": { "activeLayers": [] },
        "layers": [layer.toDict for layer in Layer.objects.filter(is_sublayer=False).exclude(layer_type='placeholder').order_by('name')],
        "themes": [theme.toDict for theme in TOCTheme.objects.all().order_by('display_name')],
        "success": True
    }
    return HttpResponse(simplejson.dumps(json))


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

        except Exception, e:
            return HttpResponse(e.message, status=500)

        result = layer_result(layer, message="Saved Successfully")
        return HttpResponse(simplejson.dumps(result))


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

        except Exception, e:
            return HttpResponse(e.message, status=500)

        result = layer_result(layer, message="Edited Successfully")
        return HttpResponse(simplejson.dumps(result))


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
            return HttpResponseRedirect('/admin/data_manager/')    # success url
    else:
        form = UploadContentsForm()
    if len(ImportEvent.objects.all()) == 0:
        fixture = create_backup_fixture(request.user)
        initial_contents = create_initial_contents(fixture, request.user)
        set_import_as_current(initial_contents)

    current_fixture = ImportEvent.objects.filter(current=True)[0]

    # return render_to_response(template_name, {'form': form})
    template = loader.get_template(template_name)

    context = RequestContext(
        request, {
            'form': form,
            'current_fixture': str(current_fixture.data_file)
        }
    )

    context.update(extra_context)
    return HttpResponse(template.render(context))

import_export_admin = staff_member_required(import_export_admin)

'''
dump current data_manager data to a file to rebuild on import failure
'''
def create_backup_fixture(user):
    from django.core import management
    backup_file = '/tmp/data_manager_backup.json'
    with open(backup_file, 'w') as f:
        management.call_command('dumpdata', 'mp_settings', 'data_manager', format='json', indent=2, exclude=['data_manager.ImportEvent'], stdout=f)
    return backup_file

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
            data_file=File(file_obj)
        )
        file_obj.close()
        return init_event

'''
given a data_manager fixture file name, load the data into the database
fixture must be a string of the file location.
'''
def load_contents_fixture(fixture):
    from django.core import management
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
    TOCSubTheme.objects.all().delete()
    TOC.objects.all().delete()

'''
record the import event and attempt to load the data_manager data into the database
'''
def handle_imported_content_file(import_file, user):
    import json
    backup_file = create_backup_fixture(user)

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
