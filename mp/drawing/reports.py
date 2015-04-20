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

    title = 'Area of mapped Dense Acropora cervicornis'
    acerv_area = get_sum(grid_cells, 'acerv_area')
    data = str(format_precision(acerv_area, 0)) + ' m²'
    attributes.append({'title': title, 'data': data})

    title = 'Dense Acropora presence'
    data = 'No Known Dense Acropora Patches'
    num_acropora = get_value_count(grid_cells, 'acropora_pa', 'Y')
    if num_acropora == 1:
        data = '1 cell is known to contain Dense Acropora Patches'
    elif num_acropora > 1:
        data = str(num_acropora) + ' cells are known to contain Dense Acropora Patches'
    attributes.append({'title': title, 'data': data})

    title = "Anchoring density"
    levels = ['Low', 'Medium', 'High', 'Very High']
    data = []
    for level in levels:
        data.append((level, get_value_count(grid_cells, 'anchor_desc', level)))
    attributes.append({'title': title,
                       'data': ', '.join(["%s (%s cells)" % d for d in data])})

    title = 'Intersects with designated anchorage'
    data = 'No'
    num_anchorages = get_value_count(grid_cells, 'anchorage', 'Y')
    if num_anchorages >= 1:
        data = 'Yes'
    attributes.append({'title': title, 'data': data})

    title = 'Artificial Habitats'
    art_area = get_sum(grid_cells, 'art_area')
    data = str(format_precision(art_area, 0)) + ' m²'
    attributes.append({'title': title, 'data': data})

    title = 'Boater Use Intensity (OFR 2015)'
    val = get_sum(grid_cells, 'boat_use')
    data = str(format_precision(val, 0)) + ' activity days'
    attributes.append({'title': title, 'data': data})

    title = 'Planning Units with Coral Bleaching Index data'
    val = get_count_notnull(grid_cells, 'coral_bleach')
    attributes.append({'title': title, 'data': str(int(val))})
    if val >= 1:
        # average
        title = 'Average Coral Bleaching Index'
        val = get_average(grid_cells, 'coral_bleach')
        data = str(format_precision(val, 0)) + ' units'
        attributes.append({'title': title, 'data': data})
        # range
        title = 'Range of Coral Bleaching Index'
        data = "%s to %s" % get_range(grid_cells, 'coral_bleach')
        attributes.append({'title': title, 'data': data})

    title = 'Planning Units with Coral Cover data'
    val = get_count_notnull(grid_cells, 'coral_cover')
    attributes.append({'title': title, 'data': str(int(val))})
    if val >= 1:
        # average
        title = 'Average Coral Cover'
        coral_cover = get_average(grid_cells, 'coral_cover')
        data = str(format_precision(coral_cover, 0)) + ' percent'
        attributes.append({'title': title, 'data': data})
        # range
        title = 'Range of Coral Cover'
        data = "%s to %s percent" % get_range(grid_cells, 'coral_cover')
        attributes.append({'title': title, 'data': data})

    title = 'Planning Units with Coral Density data'
    val = get_count_notnull(grid_cells, 'coral_density')
    attributes.append({'title': title, 'data': str(int(val))})
    if val >= 1:
        # average
        title = 'Number of coral colonies per square meter (FRRP data)'
        coral_density = get_average(grid_cells, 'coral_density')
        data = str(format_precision(coral_density, 0))
        attributes.append({'title': title, 'data': data})
        # range
        title = 'Range of Coral Density'
        data = "%s to %s m2" % get_range(grid_cells, 'coral_density')
        attributes.append({'title': title, 'data': data})

    title = 'Planning Units with Coral Disease Index data'
    val = get_count_notnull(grid_cells, 'coral_disease')
    attributes.append({'title': title, 'data': str(int(val))})
    if val >= 1:
        # average
        title = 'Average Coral Disease Index'
        val = get_average(grid_cells, 'coral_disease')
        data = str(format_precision(val, 0)) + ' units'
        attributes.append({'title': title, 'data': data})
        # range
        title = 'Range of Coral Disease Index'
        data = "%s to %s" % get_range(grid_cells, 'coral_disease')
        attributes.append({'title': title, 'data': data})

    title = 'Average Coral Resilience Index'
    data = 'No Planning Units with Coral Resilience Index of 1'
    count = get_value_count(grid_cells, 'coral_resilience', 1)
    if count >= 1:
        data = str(count) + ' cells with Coral Resilience Index of 1'
    attributes.append({'title': title, 'data': data})

    title = 'Planning Units with Coral Richness data'
    val = get_count_notnull(grid_cells, 'coral_richness')
    attributes.append({'title': title, 'data': str(int(val))})
    if val >= 1:
        # average
        title = 'Number of coral species (FRRP data)'
        coral_richness = get_average(grid_cells, 'coral_richness')
        data = str(format_precision(coral_richness, 0))
        attributes.append({'title': title, 'data': data})
        # range
        title = 'Range of Coral Richness'
        data = "%s to %s species" % get_range(grid_cells, 'coral_richness')
        attributes.append({'title': title, 'data': data})

    title = 'Planning Units with Soft Coral cover data'
    val = get_count_notnull(grid_cells, 'coral_soft')
    attributes.append({'title': title, 'data': str(int(val))})
    if val >= 1:
        # average
        title = 'Average Soft Coral Percent Cover'
        val = get_average(grid_cells, 'coral_soft')
        data = str(format_precision(val, 0))
        attributes.append({'title': title, 'data': data})
        # range
        title = 'Range of Soft Coral Percent Cover'
        data = "%s to %s percent" % get_range(grid_cells, 'coral_soft')
        attributes.append({'title': title, 'data': data})

    counties = get_unique_values(grid_cells, 'county')
    if len(counties) == 1:
        attributes.append({'title': 'County', 'data': counties[0]})
    elif len(counties) > 1:
        attributes.append({'title': 'Counties', 'data': ", ".join(counties)})

    # Depth Range, no mean
    min_depth = get_min(grid_cells, 'depth_min')
    max_depth = get_max(grid_cells, 'depth_max')
    depth_range = '%s to %s feet' %(format_precision(min_depth,0), format_precision(max_depth,0))
    attributes.append({'title': 'Depth Range', 'data': depth_range})

    mean_depth = get_average(grid_cells, 'depth_mean')  # mean of mean depth?
    data = '%s feet' % (format_precision(mean_depth, 0))
    attributes.append({'title': 'Average Depth', 'data': data})

    title = 'Diving and Fishing use overlap'
    val = get_sum(grid_cells, 'divefish_overlap')
    data = str(format_precision(val, 0)) + ' activity days'
    attributes.append({'title': title, 'data': data})

    title = 'Extractive Diving Use Intensity (OFR 2015)'
    val = get_sum(grid_cells, 'extdive_use')
    data = str(format_precision(val, 0)) + ' activity days'
    attributes.append({'title': title, 'data': data})

    title = 'Mapped Impact Source'
    data = 'No Mapped Impact Sources'
    num_impacted = get_value_count(grid_cells, 'impacted', 'Y')
    if num_impacted == 1:
        data = '1 cell contains Mapped Impact Sources'
    elif num_impacted > 1:
        data = str(num_impacted) + ' cells contain Mapped Impact Sources'
    attributes.append({'title': title, 'data': data})

    title = 'Injury Sites'
    data = 'No Recorded Injury Sites'
    num_injury_sites = get_value_count(grid_cells, 'injury_site', 'Y')
    if num_injury_sites == 1:
        data = '1 cell contains Injury Sites'
    elif num_injury_sites > 1:
        data = str(num_injury_sites) + ' cells contain Injury Sites'
    attributes.append({'title': title, 'data': data})

    min_distance_to_inlet, max_distance_to_inlet = get_range(grid_cells, 'inlet_distance')
    distance_to_inlet = '%s to %s mi' %(format_precision(min_distance_to_inlet,1), format_precision(max_distance_to_inlet,1))
    attributes.append({'title': 'Distance to Nearest Inlet', 'data': distance_to_inlet})

    title = 'Large Live Coral'
    data = 'No Known Large Live Corals'
    num_large_live_corals = get_value_count(grid_cells, 'large_live_coral', 'Y')
    if num_large_live_corals == 1:
        data = '1 cell is known to contain Large Live Corals'
    elif num_large_live_corals > 1:
        data = str(num_large_live_corals) + ' cells known to contain Large Live Corals'
    attributes.append({'title': title, 'data': data})

    title = 'Mooring Buoys'
    data = 'No Mooring Buoys'
    num_mooring_buoys = get_value_count(grid_cells, 'mooring_buoy', 'Y')
    if num_mooring_buoys == 1:
        data = '1 cell contains Mooring Buoy'
    elif num_mooring_buoys > 1:
        data = str(num_mooring_buoys) + ' cells contain Mooring Buoys'
    attributes.append({'title': title, 'data': data})

    title = "Mooring density"
    levels = ['Low', 'Medium', 'High', 'Very High']
    data = []
    for level in levels:
        data.append((level, get_value_count(grid_cells, 'mooring_desc', level)))
    attributes.append({'title': title,
                       'data': ', '.join(["%s (%s cells)" % d for d in data])})

    min_distance_to_outfall, max_distance_to_outfall = get_range(grid_cells, 'outfall_distance')
    distance_to_outfall = '%s to %s mi' %(format_precision(min_distance_to_outfall,1), format_precision(max_distance_to_outfall,1))
    attributes.append({'title': 'Distance to Nearest Outfall', 'data': distance_to_outfall})

    min_distance_to_pier, max_distance_to_pier = get_range(grid_cells, 'pier_distance')
    distance_to_pier = '%s to %s mi' %(format_precision(min_distance_to_pier,1), format_precision(max_distance_to_pier,1))
    attributes.append({'title': 'Distance to Nearest Pier', 'data': distance_to_pier})

    title = 'Pillar Coral Presence'
    data = 'No Known Pillar Corals'
    num_pillar_presence = get_value_count(grid_cells, 'pillar_presence', 'P')
    if num_pillar_presence == 1:
        data = '1 cell is known to contain Pillar Corals'
    elif num_pillar_presence > 1:
        data = str(num_pillar_presence) + ' cells are known to contain Pillar Corals'
    attributes.append({'title': title, 'data': data})

    title = 'Planning Units with important fish density data'
    val = get_count_notnull(grid_cells, 'reccom_fish')
    attributes.append({'title': title, 'data': str(int(val))})
    if val >= 1:
        # average
        title = 'Average Recreationally and commercially important fishes'
        val = get_average(grid_cells, 'reccom_fish')
        data = str(format_precision(val, 1)) + ''
        attributes.append({'title': title, 'data': data})
        # range
        title = 'Range of Recreationally and commercially important fishes density'
        data = "%s to %s" % get_range(grid_cells, 'reccom_fish')
        attributes.append({'title': title, 'data': data})

    title = 'Recreational Fishing Use Intensity (OFR 2015)'
    val = get_sum(grid_cells, 'recfish_use')
    data = str(format_precision(val, 0)) + ' activity days'
    attributes.append({'title': title, 'data': data})

    title = 'Reefs'
    area = get_sum(grid_cells, 'reef_area')
    data = str(format_precision(area, 0)) + ' m²'
    attributes.append({'title': title, 'data': data})

    title = 'Planning Units with Reef Fish Density data'
    val = get_count_notnull(grid_cells, 'reef_fish_density')
    attributes.append({'title': title, 'data': str(int(val))})
    if val >= 1:
        # average
        title = 'Average Reef Fish Density'
        val = get_average(grid_cells, 'reef_fish_density')
        data = str(format_precision(val, 1)) + ' '
        attributes.append({'title': title, 'data': data})
        # range
        title = 'Range of Relative Reef Fish Density'
        data = "%s to %s" % get_range(grid_cells, 'reef_fish_density')
        attributes.append({'title': title, 'data': data})

    title = 'Planning Units with Reef Fish Richness data'
    val = get_count_notnull(grid_cells, 'reef_fish_richness')
    attributes.append({'title': title, 'data': str(int(val))})
    if val >= 1:
        # average
        title = 'Average Reef Fish Species Richness'
        val = get_average(grid_cells, 'reef_fish_richness')
        data = str(format_precision(val, 1)) + ''
        attributes.append({'title': title, 'data': data})
        # range
        title = 'Range of Reef Fish Species Richness'
        data = "%s to %s species" % get_range(grid_cells, 'reef_fish_richness')
        attributes.append({'title': title, 'data': data})

    regions = get_unique_values(grid_cells, 'region')
    if len(regions) == 1:
        attributes.append({'title': 'Region', 'data': regions[0]})
    elif len(regions) > 1:
        attributes.append({'title': 'Regions', 'data': ", ".join(regions)})

    title = 'Sand'
    area = get_sum(grid_cells, 'sand_area')
    data = str(format_precision(area, 0)) + ' m²'
    attributes.append({'title': title, 'data': data})

    title = 'Scuba Diving Use Intensity (OFR 2015)'
    val = get_sum(grid_cells, 'scuba_use')
    data = str(format_precision(val, 0)) + ' activity days'
    attributes.append({'title': title, 'data': data})

    title = 'Seagrass'
    area = get_sum(grid_cells, 'sg_area')
    data = str(format_precision(area, 0)) + ' m²'
    attributes.append({'title': title, 'data': data})

    min_distance_to_shore, max_distance_to_shore = get_range(grid_cells, 'shore_distance')
    distance_to_shore = '%s to %s mi' %(format_precision(min_distance_to_shore,1), format_precision(max_distance_to_shore,1))
    attributes.append({'title': 'Distance to Shore', 'data': distance_to_shore})

    title = 'Spearfishing Use Intensity (OFR 2015)'
    val = get_sum(grid_cells, 'spear_use')
    data = str(format_precision(val, 0)) + ' activity days'
    attributes.append({'title': title, 'data': data})

    title = 'Planning Units with Sponge cover data'
    val = get_count_notnull(grid_cells, 'sponge')
    attributes.append({'title': title, 'data': str(int(val))})
    if val >= 1:
        # average
        title = 'Sponge cover'
        val = get_average(grid_cells, 'sponge')
        data = str(format_precision(val, 0)) + ' percent'
        attributes.append({'title': title, 'data': data})
        # range
        title = 'Range of Sponge cover'
        data = "%s to %s percent" % get_range(grid_cells, 'sponge')
        attributes.append({'title': title, 'data': data})

    title = 'Total Use Intensity (OFR 2015)'
    val = get_sum(grid_cells, 'total_use')
    data = str(format_precision(val, 0)) + ' activity days'
    attributes.append({'title': title, 'data': data})

    title = 'Water Sports (OFR 2015)'
    val = get_sum(grid_cells, 'watersport_use')
    data = str(format_precision(val, 0)) + ' activity days'
    attributes.append({'title': title, 'data': data})

    return attributes
