from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from django.conf import settings
from data_manager.api import LayerResource, ThemeResource, TocThemeResource
from tastypie.api import Api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from data_manager.views import import_export_admin, import_report_hex, get_current_fixture, create_data_manager_snapshot, data_manager_make_current
from map_proxy.views import mapproxy_view

from django.views import static

import visualize
import explore
#from mapproxy.views import proxy_view
#import map_proxy
# print(dir(map_proxy))
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(LayerResource())
v1_api.register(ThemeResource())
v1_api.register(TocThemeResource())


urlpatterns = [
    '',
    url(r'^admin/port_data_manager/$', import_export_admin),
    url(r'^admin/import_report_hex/$', import_report_hex),
    url(r'^admin/get_current_data_manager_fixture/$', get_current_fixture),
    url(r'^admin/create_data_manager_snapshot/$', create_data_manager_snapshot),
    url(r'^admin/data_manager_make_current/(?P<import_id>.*)$', data_manager_make_current),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    (r'^api/', include(v1_api.urls)),
    (r'^mp_profile/', include('mp_profile.urls')),
    #(r'^sdc/', include('scenarios.urls')),
    (r'^drawing/', include('drawing.urls')),
    (r'^data_manager/', include('data_manager.urls')),
    (r'^content/', include('content.urls')),
    #(r'^learn/', include('learn.urls')),
    (r'^scenario/', include('scenarios.urls')),
    (r'^explore/', include('explore.urls')),
    (r'^visualize/', include('visualize.urls')),
    (r'^planner/', include('visualize.urls')),
    (r'^embed/', include('visualize.urls')),
    (r'^mobile/', include('visualize.urls')),
    (r'^feedback/', include('feedback.urls')),
    (r'^proxy/', include('mp_proxy.urls')),
    url(r'^mapproxy/(?P<path>.*)',
       mapproxy_view),
    (r'^([\w-]*)/planner/', visualize.views.show_planner),
    (r'^([\w-]*)/visualize/', visualize.views.show_planner),
    (r'^([\w-]*)/embed/',
        visualize.views.show_embedded_map),
    (r'^([\w-]*)/catalog/', explore.views.data_catalog),
    (r'^$', RedirectView.as_view(url='/visualize')),
    url("^media/admin/(?P<path>.*)$",
           static.serve,
           {"document_root": settings.ADMIN_MEDIA_PATH}),
    (r'', include('madrona.common.urls')),
    (r'^tinymce/', include('tinymce.urls')),
]


if settings.DEBUG:
    # urlpatterns = [
    #     url("^media/admin/(?P<path>.*)$",
    #     "django.views.static.serve",
    #     {"document_root": settings.ADMIN_MEDIA_PATH})] + urlpatterns
    urlpatterns += staticfiles_urlpatterns()
