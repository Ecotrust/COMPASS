from django.conf.urls import url, include
from data_manager.views import *

urlpatterns = [
    '',
    (r'^layer/([A-Za-z0-9_-]+)$', update_layer),
    (r'^layer', create_layer),
    (r'^wa_config', load_config),
    (r'^get_json/([\w-]*)', get_json)
]
