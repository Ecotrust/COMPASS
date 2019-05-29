from django.conf.urls import url, include as old_include
from django.urls import re_path, include
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
    # '',
    re_path(r'^admin/port_data_manager/$', import_export_admin),
    re_path(r'^admin/import_report_hex/$', import_report_hex),
    re_path(r'^admin/get_current_data_manager_fixture/$', get_current_fixture),
    re_path(r'^admin/create_data_manager_snapshot/$', create_data_manager_snapshot),
    re_path(r'^admin/data_manager_make_current/(?P<import_id>.*)$', data_manager_make_current),
    url(r'^admin/', admin.site.urls),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    re_path(r'^api/', include(v1_api.urls)),
    re_path(r'^mp_profile/', include('mp_profile.urls')),
    #(r'^sdc/', include('scenarios.urls')),
    re_path(r'^drawing/', include('drawing.urls')),
    re_path(r'^data_manager/', include('data_manager.urls')),
    re_path(r'^content/', include('content.urls')),
    #(r'^learn/', include('learn.urls')),
    re_path(r'^scenario/', include('scenarios.urls')),
    re_path(r'^explore/', include('explore.urls')),
    re_path(r'^visualize/', include('visualize.urls')),
    re_path(r'^planner/', include('visualize.urls')),
    re_path(r'^embed/', include('visualize.urls')),
    re_path(r'^mobile/', include('visualize.urls')),
    re_path(r'^feedback/', include('feedback.urls')),
    re_path(r'^proxy/', include('mp_proxy.urls')),
    re_path(r'^mapproxy/(?P<path>.*)',
       mapproxy_view),
    re_path(r'^([\w-]*)/planner/', visualize.views.show_planner),
    re_path(r'^([\w-]*)/visualize/', visualize.views.show_planner),
    re_path(r'^([\w-]*)/embed/',
        visualize.views.show_embedded_map),
    re_path(r'^([\w-]*)/catalog/', explore.views.data_catalog),
    re_path(r'^$', RedirectView.as_view(url='/visualize')),
    re_path(r"^media/admin/(?P<path>.*)$",
           static.serve,
           {"document_root": settings.ADMIN_MEDIA_PATH}),
    re_path(r'^accounts/', include('madrona.openid.urls')),
    re_path(r'', include('madrona.openid.urls')),
    # (r'', include('madrona.common.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
]


if settings.DEBUG:
    # urlpatterns = [
    #     url("^media/admin/(?P<path>.*)$",
    #     "django.views.static.serve",
    #     {"document_root": settings.ADMIN_MEDIA_PATH})] + urlpatterns
    urlpatterns += staticfiles_urlpatterns()
