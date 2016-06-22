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

def get_unique_list_values(grid_cells, field):
    import ast
    values = []
    for gc in grid_cells:
        value = getattr(gc, field)
        input_list = ast.literal_eval(value)
        for item in input_list:
            str_item = str(item)
            if str_item not in values:
                values.append(str_item)
    return values

def apply_lookup(id_list, lookup):
    values = []
    for id in id_list:
        values.append(lookup[id])
    return values

def unordered_list(list):
    return "<ul><li>%s</li></ul>" % ("</li><li>".join(list))

#TODO: Populate species lookup when you get it from Mike

species_lookup = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

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

    habitats = apply_lookup(get_unique_list_values(grid_cells, 'habitat'), species_lookup)
    habitats.sort()
    if len(habitats) == 1:
        attributes.append({'title': 'Habitat', 'data': habitats[0]})
    elif len(habitats) > 1:
        attributes.append({'title': 'Habitats', 'data': unordered_list(habitats)})

    fish = apply_lookup(get_unique_list_values(grid_cells, 'fish'), species_lookup)
    fish.sort()
    attributes.append({'title': 'Fish', 'data': unordered_list(fish)})

    obs_spec = apply_lookup(get_unique_list_values(grid_cells, 'obs_spec'), species_lookup)
    obs_spec.sort()
    attributes.append({'title': 'Observed Species', 'data': unordered_list(obs_spec)})

    mod_spec = apply_lookup(get_unique_list_values(grid_cells, 'mod_spec'), species_lookup)
    mod_spec.sort()
    attributes.append({'title': 'Modeled Species', 'data': unordered_list(mod_spec)})

    return attributes
