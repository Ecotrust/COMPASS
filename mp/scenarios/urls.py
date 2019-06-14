# from django.conf.urls import url, include
from django.urls import re_path, include
from scenarios.views import *

urlpatterns = [
    # '',
    #feature reports
    re_path(r'sdc_report/(\d+)', sdc_analysis, name='sdc_analysis'), #user requested sdc analysis
    re_path(r'delete_design/(?P<uid>[\w_]+)/$', delete_design), #user deletes scenario (or cancels empty geometry result)
    re_path(r'get_attributes/(?P<uid>[\w_]+)/$', get_attributes), #get attributes for a given scenario
    re_path(r'get_scenarios$', get_scenarios),
    re_path(r'get_leaseblocks$', get_leaseblocks),
    re_path(r'get_sharing_groups$', get_sharing_groups),
    re_path(r'share_design$', share_design),
    re_path(r'copy_design/(?P<uid>[\w_]+)/$', copy_design),
    re_path(r'get_selections$', get_selections),
    re_path(r'get_leaseblock_features$', get_leaseblock_features),
    re_path(r'get_filter_count$', get_filter_count),
    re_path(r'get_filter_results$', get_filter_results),
]
