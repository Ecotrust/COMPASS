from django.conf.urls import url, include
from content.views import *

urlpatterns = [
    '',
    (r'^get/$', get_content),
    # (r'^get/([A-Za-z0-9_-]+)$', get_specific_content),
]
