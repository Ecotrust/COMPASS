from django.conf.urls import url, include
from feedback.views import *

urlpatterns = [
    '',
    (r'^send', send_feedback),
    # (r'^bookmark', send_bookmark),
]
