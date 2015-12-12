from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    (r'^get/$', get_content),
    # (r'^get/([A-Za-z0-9_-]+)$', get_specific_content),
)
