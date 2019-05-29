# from django.conf.urls import url, include
from django.urls import re_path, include
from content.views import *

urlpatterns = [
    # '',
    re_path(r'^get/$', get_content),
    # (r'^get/([A-Za-z0-9_-]+)$', get_specific_content),
]
