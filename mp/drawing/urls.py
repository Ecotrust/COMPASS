# from django.conf.urls import url, include
from django.urls import re_path, include
from drawing.views import *

urlpatterns = [
    # '',
    #drawings
    re_path(r'get_drawings$', get_drawings),
    re_path(r'delete_design/(?P<uid>[\w_]+)/$', delete_drawing), #user deletes drawing (or cancels empty geometry result)
    re_path(r'get_attributes/(?P<uid>[\w_]+)/$', get_attributes), #get attributes for a given scenario
    re_path(r'get_geometry_orig/(?P<uid>[\w_]+)/$', get_geometry_orig), #get geometry_orig wkt
    re_path(r'clip_to_grid$', get_clipped_shape),
    re_path(r'get_csv/(?P<uid>[\w_]+)/$', get_csv),
    #feature reports
    # url(r'wind_report/(\d+)', wind_analysis, name='wind_analysis'), #user requested wind energy site analysis
    re_path(r'aoi_report/(\d+)', aoi_analysis, name='aoi_analysis'), #user requested area of interest analysis
    re_path(r'get_report_html/$', get_report_html),
    re_path(r'get_report_html/(?P<uid>[\w_]+)/$', get_report_html),
]
