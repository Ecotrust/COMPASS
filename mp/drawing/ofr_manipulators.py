from scenarios.models import GridCell
from django.contrib.gis.db.models.aggregates import Union

def clip_to_grid(geom):

    intersection = intersecting_cells(geom)

    new_shape = intersection.aggregate(Union('geometry'))
    if len(intersection) == 1:
        #single cells come back as a multipolygon
        clipped_shape = new_shape['geometry__union'].simplify();
    else:
        clipped_shape = new_shape['geometry__union'];

    return clipped_shape

def intersecting_cells(geom):
	return GridCell.objects.filter(geometry__intersects=geom)
