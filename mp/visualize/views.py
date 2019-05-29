# Create your views here.
from django.contrib.auth.models import Group
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import os
from querystring_parser import parser
import json

from json import dumps
# from social.backends.google import GooglePlusAuth
from madrona.features import get_feature_by_uid

import settings

from visualize.models import *
from data_manager.models import *
from mp_settings.models import *

def show_planner(request, project=None, template='planner.html'):
    try:
        socket_url = settings.SOCKET_URL
    except AttributeError:
        socket_url = ''
    try:
        if project:
            mp_settings = MarinePlannerSettings.objects.get(slug_name=project)
        else:
            mp_settings = MarinePlannerSettings.objects.get(active=True)
        project_name = mp_settings.project_name
        latitude = mp_settings.latitude
        longitude = mp_settings.longitude
        zoom = mp_settings.zoom
        default_hash = mp_settings.default_hash
        min_zoom = mp_settings.min_zoom
        max_zoom = mp_settings.max_zoom
        project_logo = mp_settings.project_logo
        try:
            if project_logo:
                url_validator = URLValidator()
                url_validator(project_logo)
        except ValidationError as e:
            project_logo = os.path.join(settings.MEDIA_URL, project_logo)
        project_icon = mp_settings.project_icon
        try:
            url_validator = URLValidator()
            url_validator(project_icon)
        except ValidationError as e:
            project_icon = os.path.join(settings.MEDIA_URL, project_icon)
        project_home_page = mp_settings.project_home_page
        enable_drawing = mp_settings.enable_drawing
        bitly_registered_domain = mp_settings.bitly_registered_domain
        bitly_username = mp_settings.bitly_username
        bitly_api_key = mp_settings.bitly_api_key
    except:
        project_name = project_logo = project_icon = project_home_page = bitly_registered_domain = bitly_username = bitly_api_key = default_hash = ""
        latitude = longitude = zoom = min_zoom = max_zoom = None
        enable_drawing = False
    try:
        from content.models import Content
        contents = Content.objects.all()
        content_dict = {}
        for content in contents:
            content_dict[content.name] = {
                "name": content.name,
                "display_name": content.display_name,
                "description": content.description,
                "content": content.content
            }
    except:
        content_dict = {
            "disclaimer": {
                "content": "<p>ODFW crucial habitat layers updated:</p>\r\n<p>&nbsp;February 26, 2014.&nbsp;</p>\r\n<p>&nbsp;</p>\r\n<p>&nbsp;ODFW Compass provides coarse-scale, non-regulatory fish and wildlife information, and the crucial habitat layers emphasize areas documented as containing important natural resources. This site is intended to support early planning for large-scale land-use, development, or conservation projects.&nbsp;</p>\r\n<p>&nbsp;</p>\r\n<p><strong>&nbsp;By clicking \"Agree\", you are acknowledging the following statements:</strong>&nbsp;</p>\r\n<p>&nbsp;</p>\r\n<ul>\r\n<li>Data and analyses presented within Compass are based on best available information, and are expected to be updated regularly. Crucial habitat layers reflect documented resources at the time of data aggregation; and as such absence of crucial habitat prioritization does not necessarily indicate that no crucial species or habitats are present (or have been present in that location at one time.)</li>\r\n<li>Most layers within Compass do not provide detailed information on site-specific locations or streams and using this site does not replace or supersede site-specific consolation with appropriate agencies, including the Oregon Department of Fish and Wildlife.</li>\r\n<li>Some data layers may be summarized to preserve the confidentiality of sensitive information.</li>\r\n<li>Documentation for layers and methodologies should be used to better understand the results and methodologies presented.</li>\r\n</ul>\r\n<p>&nbsp;</p>\r\n<p>&nbsp;I have read this disclaimer and understand the intent of this system, and therefore hold ODFW harmless from any liability arising from or related to using the ODFW Compass system.&nbsp;</p>",
                "display_name": "Disclaimer",
                "name": "disclaimer",
                "description": "Text content for the disclaimer window all users see upon opening Compass."
            }
        }
    context = {
        'MEDIA_URL': settings.MEDIA_URL, 'SOCKET_URL': socket_url, 'login': 'true',
        'project_name': project_name, 'latitude': latitude, 'longitude': longitude, 'zoom': zoom,
        'default_hash': default_hash, 'min_zoom': min_zoom, 'max_zoom': max_zoom,
        'project_logo': project_logo, 'project_icon': project_icon, 'project_home_page': project_home_page,
        'enable_drawing': enable_drawing,
        'bitly_registered_domain': bitly_registered_domain, 'bitly_username': bitly_username, 'bitly_api_key': bitly_api_key,
        'content': content_dict
    }
    if request.user.is_authenticated:
        context['session'] = request.session._session_key
    # if request.user.is_authenticated and request.user.social_auth.all().count() > 0:
    #     context['picture'] = request.user.social_auth.all()[0].extra_data.get('picture')
    # if settings.SOCIAL_AUTH_GOOGLE_PLUS_KEY:
    #     context['plus_scope'] = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    #     context['plus_id'] = settings.SOCIAL_AUTH_GOOGLE_PLUS_KEY
    if settings.UNDER_MAINTENANCE_TEMPLATE:
        return render(request, 'under_maintenance.html', context)
    return render(request, template, context)

def show_embedded_map(request, project=None, template='map.html'):
    try:
        if project:
            mp_settings = MarinePlannerSettings.objects.get(slug_name=project)
        else:
            mp_settings = MarinePlannerSettings.objects.get(active=True)
        project_name = mp_settings.project_name
        project_logo = mp_settings.project_logo
        try:
            if project_logo:
                url_validator = URLValidator(verify_exists=False)
                url_validator(project_logo)
        except ValidationError as e:
            project_logo = os.path.join(settings.MEDIA_URL, project_logo)
        project_home_page = mp_settings.project_home_page
    except:
        project_name = project_logo = project_home_page = None
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'project_name': project_name,
        'project_logo': project_logo,
        'project_home_page': project_home_page
    }
    #context = {'MEDIA_URL': settings.MEDIA_URL}
    return render(request, template, context)

def show_mobile_map(request, project=None, template='mobile-map.html'):
    try:
        if project:
            mp_settings = MarinePlannerSettings.objects.get(slug_name=project)
        else:
            mp_settings = MarinePlannerSettings.objects.get(active=True)
        print('so far so good')
        project_name = mp_settings.project_name
        project_logo = mp_settings.project_logo
        print(project_name)
        print(project_logo)
        # try:
        #     if project_logo:
        #         url_validator = URLValidator(verify_exists=False)
        #         url_validator(project_logo)
        # except ValidationError as e:
        #     project_logo = os.path.join(settings.MEDIA_URL, project_logo)
        print('almost there...')
        project_home_page = mp_settings.project_home_page
        print('here we go...')
        latitude = mp_settings.latitude
        print(latitude)
        longitude = mp_settings.longitude
        print(longitude)
        zoom = mp_settings.zoom
        print(zoom)
        min_zoom = mp_settings.min_zoom
        max_zoom = mp_settings.max_zoom
        print(min_zoom)
        print(max_zoom)
    except:
        project_name = project_logo = project_home_page = None
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        # 'project_name': project_name,
        # 'project_logo': project_logo,
        # 'project_home_page': project_home_page
        'latitude': latitude,
        'longitude': longitude,
        'zoom': zoom
    }
    #context = {'MEDIA_URL': settings.MEDIA_URL}
    return render(request, template, context)

def get_sharing_groups(request):
    from madrona.features import user_sharing_groups
    from functools import cmp_to_key
    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    json = []
    sharing_groups = user_sharing_groups(request.user)
    for group in sharing_groups:
        members = []
        for user in group.user_set.all():
            if user.first_name.replace(' ', '') != '' and user.last_name.replace(' ', '') != '':
                members.append(user.first_name + ' ' + user.last_name)
            else:
                members.append(user.username)
        sorted_members = sorted(members, key=cmp_to_key(locale.strcoll))
        json.append({
            'group_name': group.name,
            'group_slug': slugify(group.name)+'-sharing',
            'members': sorted_members
        })
    return HttpResponse(dumps(json))

'''
'''
def geocode(txt):
    """
    Returns geocoded results in MERCATOR projection
    First tries coordinates, then a series of geocoding engines
    """
    from geopy import distance, geocoders
    from geopy.point import Point
    from django.contrib.gis.geos import GEOSGeometry

    searchtype = lat = lon = None
    place = txt
    try:
        p = Point(txt)
        lat, lon, altitude = p
        searchtype = 'coordinates'
    except:
        pass  # not a point

    centerloc = Point(45.94, -120.55)
    max_dist = 315  # should be everything in WA and Oregon

    '''
    geocoders.ArcGIS                    geocoders.OpenMapQuest              geocoders.get_geocoder_for_service
    geocoders.Baidu                     geocoders.Photon                    geocoders.googlev3
    geocoders.Bing                      geocoders.SERVICE_TO_GEOCODER       geocoders.ignfrance
    geocoders.DataBC                    geocoders.What3Words                geocoders.navidata
    geocoders.GeoNames                  geocoders.YahooPlaceFinder          geocoders.opencage
    geocoders.GeocodeFarm               geocoders.Yandex                    geocoders.openmapquest
    geocoders.GeocoderDotUS             geocoders.arcgis                    geocoders.osm
    geocoders.GeocoderNotFound          geocoders.baidu                     geocoders.photon
    geocoders.GoogleV3                  geocoders.base                      geocoders.placefinder
    geocoders.IGNFrance                 geocoders.bing                      geocoders.smartystreets
    geocoders.LiveAddress               geocoders.databc                    geocoders.what3words
    geocoders.NaviData                  geocoders.dot_us                    geocoders.yandex
    geocoders.Nominatim                 geocoders.geocodefarm
    geocoders.OpenCage                  geocoders.geonames
    '''

    searches = [
        # geocoders.GeoNames(),
        geocoders.ArcGIS(),
        geocoders.OpenMapQuest(),
        geocoders.Nominatim(),
        # geocoders.YahooPlaceFinder(),
        # geocoders.Bing(api_key=settings.BING_API_KEY),
        # these are tried in reverse order, fastest first
        # TODO thread them and try them as they come in.
    ]

    while not (searchtype and lat and lon):  # try a geocoder
        try:
            g = searches.pop()
        except IndexError:
            break  # no more search engines left to try

        try:
            for p, loc in g.geocode(txt, exactly_one=False):
                d = distance.distance(loc, centerloc).miles
                if d < max_dist:
                    place = p
                    lat = loc[0]
                    lon = loc[1]
                    max_dist = d
                else:
                    pass
            searchtype = g.__class__.__name__
        except:
            pass

    if searchtype and lat and lon:  # we have a winner
        cntr = GEOSGeometry('SRID=4326;POINT(%f %f)' % (lon, lat))
        cntr.transform(settings.GEOMETRY_DB_SRID)
        cntrbuf = cntr.buffer(settings.POINT_BUFFER)
        extent = cntrbuf.extent
        loc = {
            'status': 'ok',
            'search': txt,
            'place': place,
            'type': searchtype,
            'extent': extent,
            'latlon': [lat, lon],
            'center': (cntr[0], cntr[1]),
        }
    else:
        loc = {
            'status': 'failed',
            'search': txt,
            'type': None,
            'extent': None,
            'center': None,
        }
    return loc


'''
'''
def geo_search(request):
    response = {}
    if request.method != 'GET':
        response['message'] = 'Not a GET request'
        response['result'] = 'Error'
    else:
        query = request.GET['query']
        response['message'] = query
        response['result'] = geocode(query)

    return HttpResponse(dumps(response), content_type="application/json")

'''
'''
def share_bookmark(request):
    group_names = request.POST.getlist('groups[]')
    bookmark_uid = request.POST['bookmark']
    bookmark = get_feature_by_uid(bookmark_uid)

    viewable, response = bookmark.is_viewable(request.user)
    if not viewable:
        return response

    #remove previously shared with groups, before sharing with new list
    bookmark.share_with(None)

    groups = []
    for group_name in group_names:
        groups.append(Group.objects.get(name=group_name))

    bookmark.share_with(groups, append=False)

    return HttpResponse("", status=200)

'''
'''
def get_bookmarks(request):
    #sync the client-side bookmarks with the server side bookmarks
    #update the server-side bookmarks and return the new list
    try:
        bookmark_dict = parser.parse(request.POST.urlencode())['bookmarks']
    except:
        bookmark_dict = {}
    try:
        #loop through the list from the client
        #if user, bm_name, and bm_state match then skip
        #otherwise, add to the db
        for key,bookmark in bookmark_dict.items():
            try:
                Bookmark.objects.get(user=request.user, name=bookmark['name'], url_hash=bookmark['hash'])
            except Bookmark.DoesNotExist:
                new_bookmark = Bookmark(user=request.user, name=bookmark['name'], url_hash=bookmark['hash'])
                new_bookmark.save()
            except:
                continue

        #grab all bookmarks belonging to this user
        #serialize bookmarks into 'name', 'hash' objects and return json dump
        content = []
        bookmark_list = Bookmark.objects.filter(user=request.user)
        for bookmark in bookmark_list:
            sharing_groups = [group.name for group in bookmark.sharing_groups.all()]
            content.append({
                'uid': bookmark.uid,
                'name': bookmark.name,
                'hash': bookmark.url_hash,
                'sharing_groups': sharing_groups
            })

        shared_bookmarks = Bookmark.objects.shared_with_user(request.user)
        for bookmark in shared_bookmarks:
            if bookmark not in bookmark_list:
                username = bookmark.user.username
                actual_name = bookmark.user.first_name + ' ' + bookmark.user.last_name
                content.append({
                    'uid': bookmark.uid,
                    'name': bookmark.name,
                    'hash': bookmark.url_hash,
                    'shared': True,
                    'shared_by_username': username,
                    'shared_by_name': actual_name
                })
        return HttpResponse(json.dumps(content), mimetype="application/json", status=200)
    except:
        return HttpResponse(status=304)

def remove_bookmark(request):
    try:
        bookmark_uid = request.POST['uid']
        bookmark = get_feature_by_uid(bookmark_uid)

        viewable, response = bookmark.is_viewable(request.user)
        if not viewable:
            return response

        bookmark.delete()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=304)

def add_bookmark(request):
    try:
        bookmark = Bookmark(user=request.user, name=request.POST.get('name'), url_hash=request.POST.get('hash'))
        bookmark.save()
        sharing_groups = [group.name for group in bookmark.sharing_groups.all()]
        content = []
        content.append({
            'uid': bookmark.uid,
            'name': bookmark.name,
            'hash': bookmark.url_hash,
            'sharing_groups': sharing_groups
        })
        print('returning content')
        return HttpResponse(json.dumps(content), mimetype="application/json", status=200)
    except:
        return HttpResponse(status=304)
