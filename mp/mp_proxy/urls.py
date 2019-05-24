from django.conf.urls import url, include
from mp_proxy.views import *

urlpatterns = [
    '',
    (r'^get_legend_json/(?P<url>)$', getLegendJSON),
    url(r'^layer/(?P<layer_id>\d*)', layer_proxy_view),
]
