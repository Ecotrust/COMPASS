# from django.conf.urls import url, include
from django.urls import re_path, include
from data_manager.views import *

urlpatterns = [
    # '',
    re_path(r'^layer/([A-Za-z0-9_-]+)$', update_layer),
    re_path(r'^layer', create_layer),
    re_path(r'^wa_config', load_config),
    re_path(r'^get_json/([\w-]*)', get_json)
]
