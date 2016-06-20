# coding: utf-8
from general.utils import format_precision
from django.db.models import Q
from django.conf import settings
from django.db.models import Sum, Avg, Min, Max


def get_min(grid_cells, field):
    grid_cells = remove_nulls(grid_cells, field)
    return grid_cells.aggregate(Min(field)).values()[0]

def get_max(grid_cells, field):
    grid_cells = remove_nulls(grid_cells, field)
    return grid_cells.aggregate(Max(field)).values()[0]

def get_range(grid_cells, field):
    return get_min(grid_cells, field), get_max(grid_cells, field)

def get_value_count(grid_cells, field, value):
    grid_cells = grid_cells.filter(Q((field, value)))
    count = grid_cells.count()
    return count

def get_count_notnull(grid_cells, field):
    grid_cells = remove_nulls(grid_cells, field)
    return grid_cells.count()

def get_sum(grid_cells, field):
    grid_cells = remove_nulls(grid_cells, field)
    return grid_cells.aggregate(Sum(field)).values()[0]

def remove_nulls(grid_cells, field):
    # Only compute averages on non-null cells
    return grid_cells.filter(~Q((field, settings.NULLVALUE)))

def get_average(grid_cells, field):
    grid_cells = remove_nulls(grid_cells, field)
    return grid_cells.aggregate(Avg(field)).values()[0]

def get_unique_values(grid_cells, field):
    values = []
    for gc in grid_cells:
        value = getattr(gc, field)
        if value not in values:
            values.append(value)
    return values


def get_summary_reports(grid_cells):
    """
    List of attributes for drawing summary reports
    """
    attributes = []

    if grid_cells.count() == 0:
        return attributes

    # Number of Grid Cells
    cell_count = grid_cells.count()
    attributes.append({'title': 'Number of Grid Cells', 'data': format(cell_count, ',d')})

    # Total Area
    total_area = sum([gc.geometry.area for gc in grid_cells]) / 1000000  # sq m to sq km
    attributes.append({'title': 'Total Area', 'data': str(format_precision(total_area, 2)) + ' sq km'})

    # ------- attributes -------

    habitats = get_unique_values(grid_cells, 'habitat')
    if len(habitats) == 1:
        attributes.append({'title': 'Habitat', 'data': habitats[0]})
    elif len(habitats) > 1:
        attributes.append({'title': 'Habitats', 'data': ", ".join(habitats)})

    fish = get_unique_values(grid_cells, 'fish')
    attributes.append({'title': 'Fish', 'data': ", ".join(fish)})

    obs_spec = get_unique_values(grid_cells, 'obs_spec')
    attributes.append({'title': 'Observed Species', 'data': ", ".join(obs_spec)})

    mod_spec = get_unique_values(grid_cells, 'mod_spec')
    attributes.append({'title': 'Modeled Species', 'data': ", ".join(mod_spec)})

    return attributes
