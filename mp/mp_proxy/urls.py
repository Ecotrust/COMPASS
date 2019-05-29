# from django.conf.urls import url, include
from django.urls import re_path, include
from mp_proxy.views import *

urlpatterns = [
    # '',
    re_path(r'^get_legend_json/(?P<url>)$', getLegendJSON),
    re_path(r'^layer/(?P<layer_id>\d*)', layer_proxy_view),
]
