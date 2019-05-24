from django.conf.urls import url, include
from explore.views import *

urlpatterns = [
    '',
    (r'^catalog', data_catalog),
    (r'^needs', data_needs),
    (r'^map_tile_example/([\w-]*)', map_tile_example),
    (r'^map_tile_esri_example/([\w-]*)', map_tile_esri_example),
    (r'^map_tile_leaflet_example/([\w-]*)', map_tile_leaflet_example),
    (r'^arcrest_example/([\w-]*)', arcrest_example),
    (r'^([\w-]*)', tiles_page)
]
