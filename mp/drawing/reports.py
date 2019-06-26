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
        try:
            input_list = ast.literal_eval(value)
        except:
            if field=='coa_name' and value=='NA':
                input_list=[]
            else:
                input_list = [value]
        for item in input_list:
            str_item = str(item)
            if str_item not in values:
                values.append(str_item)

    return values

def apply_lookup(id_list, lookup):
    values = []
    for id in id_list:
        try:
            values.append(lookup[id])
        except:
            print("NO VALUE MATCH FOUND FOR ID %s" % id)
            values.append(str(id))
    return values

def unordered_list(list):
    if len(list)> 0:
        return "<ul><li>%s</li></ul>" % ("</li><li>".join(list))
    else:
        return "<ul><li>None</li></ul>"

coa_lookup = settings.COA_LOOKUP
species_lookup = settings.SPECIES_LOOKUP

def get_summary_reports(grid_cells, list_style='unordered'):
    """
    List of attributes for drawing summary reports
    """
    attributes = []

    if grid_cells.count() == 0:
        return attributes

    # Number of Grid Cells
    cell_count = grid_cells.count()
    attributes.append({'title': 'Area mi<sup>2</sup>', 'data': format(cell_count, ',d')})

    # Total Area
    # total_area = sum([gc.geometry.area for gc in grid_cells]) / 1000000  # sq m to sq km
    # attributes.append({'title': 'Total Area', 'data': str(format_precision(total_area, 2)) + ' sq km'})

    # ------- attributes -------
    report_attr_names = {
        'ecoregions': '<a href="https://oregonconservationstrategy.org/ecoregions/" class="strategy-report-attribute-link" target="_blank">Ecoregions</a>',
        'coas': '<a href="https://oregonconservationstrategy.org/conservation-opportunity-areas/" class="strategy-report-attribute-link" target="_blank">Conservation Opportunity Areas</a>',
        'habitat': '<a href="https://oregonconservationstrategy.org/strategy-habitats/" class="strategy-report-attribute-link" target="_blank">Strategy Habitats</a>',
        'fish': '<a href="https://oregonconservationstrategy.org/ocs-strategy-species/fish/" class="strategy-report-attribute-link" target="_blank">Documented Strategy Fish</a>',
        'modeled': '<a href="https://www.dfw.state.or.us/maps/compass/reportingtool.asp" class="strategy-report-attribute-link" target="_blank">Modeled Strategy Wildlife Habitat</a>',
        'observed': '<a href="https://oregonconservationstrategy.org/ocs-strategy-species/" class="strategy-report-attribute-link" target="_blank">Observed Strategy Wildlife</a>'
    }

    ecoregions = get_unique_list_values(grid_cells, 'ecoregion')
    ecoregions.sort()
    ecoregion_list = []
    for ecoregion in ecoregions:
        if ecoregion.lower() in settings.ECOREGION_LOOKUP.keys():
            ecoregion_list.append(settings.ECOREGION_LOOKUP[ecoregion.lower()])
        else:
            ecoregion_list.append(ecoregion)
    if list_style=='unordered':
        attributes.append({'title': report_attr_names['ecoregions'], 'data': unordered_list(ecoregion_list)})
    else:
        attributes.append({'title': report_attr_names['ecoregions'], 'data': ecoregion_list})

    coas = apply_lookup(get_unique_list_values(grid_cells, 'coa_name'), coa_lookup)
    coas.sort()
    if list_style=='unordered':
        attributes.append({'title': report_attr_names['coas'], 'data': unordered_list(coas)})
    else:
        attributes.append({'title': report_attr_names['coas'], 'data': coas})

    habitats = apply_lookup(get_unique_list_values(grid_cells, 'habitat'), species_lookup)
    habitats.sort()
    if len(habitats) == 1:
        attributes.append({'title': report_attr_names['habitat'], 'data': habitats[0]})
    elif len(habitats) > 1:
        if list_style=='unordered':
            attributes.append({'title': report_attr_names['habitat'], 'data': unordered_list(habitats)})
        else:
            attributes.append({'title': report_attr_names['habitat'], 'data': habitats})

    fish = apply_lookup(get_unique_list_values(grid_cells, 'fish'), species_lookup)
    fish.sort()
    if list_style=='unordered':
        attributes.append({'title': report_attr_names['fish'], 'data': unordered_list(fish)})
    else:
        attributes.append({'title': report_attr_names['fish'], 'data': fish})

    obs_spec = apply_lookup(get_unique_list_values(grid_cells, 'obs_spec'), species_lookup)
    obs_spec.sort()
    if list_style=='unordered':
        attributes.append({'title': report_attr_names['observed'], 'data': unordered_list(obs_spec)})
    else:
        attributes.append({'title': report_attr_names['observed'], 'data': obs_spec})

    mod_spec = apply_lookup(get_unique_list_values(grid_cells, 'mod_spec'), species_lookup)
    mod_spec.sort()
    if list_style=='unordered':
        attributes.append({'title': report_attr_names['modeled'], 'data': unordered_list(mod_spec)})
    else:
        attributes.append({'title': report_attr_names['modeled'], 'data': mod_spec})

    return attributes
