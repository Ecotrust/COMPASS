# coding: utf-8
from madrona.features.forms import FeatureForm, SpatialFeatureForm
from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple
from django.forms.widgets import *
from django.forms.widgets import Input
from django.utils.safestring import mark_safe
from django.contrib.gis.geos import fromstr
from os.path import splitext, split
from madrona.analysistools.widgets import SliderWidget, DualSliderWidget
from models import *
from widgets import AdminFileWidget, SliderWidgetWithTooltip, DualSliderWidgetWithTooltip, CheckboxSelectMultipleWithTooltip, CheckboxSelectMultipleWithObjTooltip

# http://www.neverfriday.com/sweetfriday/2008/09/-a-long-time-ago.html
class FileValidationError(forms.ValidationError):
    def __init__(self):
        super(FileValidationError, self).__init__('Document types accepted: ' + ', '.join(ValidFileField.valid_file_extensions))

class ValidFileField(forms.FileField):
    """A validating document upload field"""
    valid_file_extensions = ['odt', 'pdf', 'doc', 'xls', 'txt', 'csv', 'kml', 'kmz', 'jpeg', 'jpg', 'png', 'gif', 'zip']

    def __init__(self, *args, **kwargs):
        super(ValidFileField, self).__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        f = super(ValidFileField, self).clean(data, initial)
        if f:
            ext = splitext(f.name)[1][1:].lower()
            if ext in ValidFileField.valid_file_extensions:
                # check data['content-type'] ?
                return f
            raise FileValidationError()


class InputWithUnit(Input):
    """Modified Input class that accepts a "unit" parameter, and stores the
    value in the unit attribute.
    This is allows additional data associated with a field to be exposed to the
    template renderer. Later improvements would be to stick this value on the
    field itself rather than the widget. Also, make it a dictionary rather than
    a single value, so other arbitrary values can be brough forward.
    """
    def __init__(self, attrs=None, unit=None):
        super(InputWithUnit, self).__init__(attrs)
        self.unit = str(unit)

class TextInputWithUnit(forms.TextInput, InputWithUnit):
    pass

class ScenarioForm(FeatureForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)

    # Boolean field is the anchor, and used as the base name for rendering the form.
    # - Help_text on the boolean is included in the popup text "info" icon.
    # - Label is used as the icon label

    ecoregion = forms.BooleanField(label="Ecoregion", required=False, help_text="Hexes within a given ecoregion", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 565, 'layer_title': "Show Ecoregion Outlines"}))
    ecoregion_input = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={'class': 'parameters'}),
        choices=(
            ('West Cascades', 'West Cascades'),
            ('Willamette Valley', 'Willamette Valley')
        ), initial='Willamette Valley')


    # acropora_pa = forms.BooleanField(label="Dense Acropora patches", required=False, help_text="Planning units that contain at least part of a known dense Acropora patch.", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 440, 'layer_title': "Show Dense Acropora patches"}))
    # acropora_pa_input = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'parameters'}), choices=(('Y', 'Include'), ('N', 'Exclude')), initial='Y')
    #
    # coa_name = forms.BooleanField(label="Anchoring (Berhinger data)", required=False, help_text="Planning units that contain numbers of anchored boats based on a point density analysis at 500 m radius around each anchored boat observed.", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 415, 'layer_title': "Show Anchored Boat Density (2012-2014)"}))
    # coa_name_input = forms.ChoiceField(
    #     required=False,
    #     widget=forms.Select(attrs={'class': 'parameters', 'pre_text': 'at least'}),
    #     choices=(('Low', 'Low'),
    #              ('Medium', 'Medium'),
    #              ('High', 'High'),
    #              ('Very High', 'Very High')),
    #     initial='Low')
    #
    # anchorage = forms.BooleanField(label="Anchorage Areas", required=False, help_text="Planning units that overlap presently designated anchorages.", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 334, 'layer_title': 'Show Commercial Anchorage Areas'}))
    # anchorage_input = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'parameters'}), choices=(('Y', 'Include'), ('N', 'Exclude')), initial='Y')
    #
    # boat_use = forms.BooleanField(label="Boater Use Intensity (OFR 2015)", required=False, help_text="Planning units that contain at least one entry for boating in the 2015 OFR survey", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    #     #, 'layer_id': 418, 'layer_title': "Show Boater Use"}))
    # boat_use_min = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # boat_use_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # boat_use_input = forms.FloatField(widget=DualSliderWidget('boat_use_min', 'boat_use_max', min=1, max=420, step=10))
    #
    # coral_bleach = forms.BooleanField(label="Coral Bleaching", required=False, help_text="Planning units that contain at least one FRRP site with a value greater than 0 in the site bleaching index.(FRRP data)", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 401, 'layer_title': "Show Coral Bleaching"}))
    # coral_bleach_min = forms.FloatField(required=False, initial=2, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # coral_bleach_max = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # coral_bleach_input = forms.FloatField(widget=DualSliderWidget('coral_bleach_min', 'coral_bleach_max', min=0, max=10, step=0.5))
    #
    # coral_cover = forms.BooleanField(label="Coral Percent Cover", required=False, help_text="The maximum value of percent coral cover in all compiled benthic survey sites within the Planning Unit", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 405, 'layer_title': "Show Coral Percent Cover"}))
    # coral_cover_min = forms.FloatField(required=False, initial=2, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # coral_cover_max = forms.FloatField(required=False, initial=20, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to', 'post_text': 'percent'}))
    # coral_cover_input = forms.FloatField(widget=DualSliderWidget('coral_cover_min', 'coral_cover_max', min=0, max=34, step=1))
    #
    # coral_density = forms.BooleanField(label="Coral Density", required=False, help_text="The maximum value of coral density (coral per square meter) in all compiled benthic survey sites within the Planning Unit", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 407, 'layer_title': "Show Coral Density"}))
    # coral_density_min = forms.FloatField(required=False, initial=2, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # coral_density_max = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to', 'post_text': 'per m²'}))
    # coral_density_input = forms.FloatField(widget=DualSliderWidget('coral_density_min', 'coral_density_max', min=0, max=13, step=0.5))
    #
    # coral_disease = forms.BooleanField(label="Coral Disease", required=False, help_text="Planning units that contain at least one FRRP site with a value greater than 0 in the site disease index.(FRRP data)", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 402, 'layer_title': "Show Coral Disease"}))
    # coral_disease_min = forms.FloatField(required=False, initial=2, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # coral_disease_max = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # coral_disease_input = forms.FloatField(widget=DualSliderWidget('coral_disease_min', 'coral_disease_max', min=0, max=6, step=0.5))
    #
    # coral_resilience = forms.BooleanField(label="Coral Resilience Index (FRRP)", required=False, help_text="Planning units where a coral resilience index was estimated based on coral density, bleaching occurrrence, and disease prevalence. (FRRP database)", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 403, 'layer_title': "Show Coral Resilience"}))
    # coral_resilience_min = forms.FloatField(required=False, initial=-1, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # coral_resilience_max = forms.FloatField(required=False, initial=1, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # coral_resilience_input = forms.FloatField(widget=DualSliderWidget('coral_resilience_min', 'coral_resilience_max', min=-2, max=1, step=1))
    #
    # coral_richness = forms.BooleanField(label="Number of Coral Species", required=False, help_text="The maximum value of number of coral species in all compiled benthic survey sites within the Planning Unit", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 406, 'layer_title': "Show Number of Coral Species"}))
    # coral_richness_min = forms.FloatField(required=False, initial=2, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # coral_richness_max = forms.FloatField(required=False, initial=10, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # coral_richness_input = forms.FloatField(widget=DualSliderWidget('coral_richness_min', 'coral_richness_max', min=0, max=15, step=1))
    #
    # coral_soft = forms.BooleanField(label="Soft Coral Percent Cover", required=False, help_text="The maximum value of percent Soft Coral cover in all compiled benthic survey sites within the Planning Unit", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 409, 'layer_title': "Show Soft Coral Percent Cover"}))
    # coral_soft_min = forms.FloatField(required=False, initial=2, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # coral_soft_max = forms.FloatField(required=False, initial=20, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to', 'post_text': 'percent'}))
    # coral_soft_input = forms.FloatField(widget=DualSliderWidget('coral_soft_min', 'coral_soft_max', min=0, max=38, step=1))
    #
    # depth_mean = forms.BooleanField(label="Average Depth", required=False, help_text="The average depth in a planning unit in ft. Positive sign indicates depth, negative indicates elevation", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    # depth_mean_min = forms.FloatField(required=False, initial=10, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'Depth Range (feet)'}))
    # depth_mean_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # depth_mean_input = forms.FloatField(widget=DualSliderWidget('depth_mean_min', 'depth_mean_max', min=-11, max=220, step=1))
    #
    # divefish_overlap = forms.BooleanField(label="Diving and Fishing use overlap (OFR 2015)", required=False, help_text="Planning units that contain at least one entry for both fishing and diving in the 2015 OFR survey. Negative numbers are more fishing than diving. Positive numbers are more diving than fishing. Zero is an equal amount of both activities.", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    #     #  'layer_id': 424, 'layer_title': "Show Recreational Fishing and Diving Activity Overlap"}))
    # divefish_overlap_min = forms.FloatField(required=False, initial=10, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # divefish_overlap_max = forms.FloatField(required=False, initial=200, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # divefish_overlap_input = forms.FloatField(widget=DualSliderWidget('divefish_overlap_min', 'divefish_overlap_max', min=-70, max=640, step=10))
    #
    # extdive_use = forms.BooleanField(label="Extractive Diving Use Intensity (OFR 2015)", required=False, help_text="Planning units that contain at least one entry for extractive diving in the 2015 OFR survey", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    #     #, 'layer_id': 421, 'layer_title': "Show Extractive Diving Activities"}))
    # extdive_use_min = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # extdive_use_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # extdive_use_input = forms.FloatField(widget=DualSliderWidget('extdive_use_min', 'extdive_use_max', min=0, max=70, step=10))  # spreadsheet says 1 to 65 steps of 10?
    #
    # impacted = forms.BooleanField(label="Historic impacts", required=False, help_text="Planning units that contain at least one known planned or unplanned impact including injury sites, artificial reefs and substrate, outfalls, piers, cables, tires, inlets, channels, dredged areas, spoil areas, and/or commercial ship anchorages.", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    # impacted_input = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'parameters'}), choices=(('Y', 'Include'), ('N', 'Exclude')), initial='Y')
    #
    # injury_site = forms.BooleanField(label="Injury Sites", required=False, help_text="Planning units that contain at least one known location of past grounding, anchoring, cable, or other reef injury event (FDEP database)", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': '328', 'layer_title': 'Show Reef Injury Sites'}))
    # injury_site_input = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'parameters', 'layer_id': '918', 'layer_title': 'Reef Injury Site'}), choices=(('Y', 'Include'), ('N', 'Exclude')), initial='Y')
    #
    # inlet_distance = forms.BooleanField(label="Distance from Coastal Inlet", required=False, help_text="Distance from nearest inlet in miles", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 339, 'layer_title': 'Show Inlets and Passes'}))
    # inlet_distance_min = forms.FloatField(required=False, initial=2, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # inlet_distance_max = forms.FloatField(required=False, initial=6, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to', 'post_text': 'miles'}))
    # inlet_distance_input = forms.FloatField(widget=DualSliderWidget('inlet_distance_min', 'inlet_distance_max', min=0, max=8.5, step=0.5))
    #
    # large_live_coral = forms.BooleanField(label="Large Live Corals", required=False, help_text="Planning units that contain at least one known live coral greater than 2m.", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 404, 'layer_title': "Show Large Live Corals"}))
    # large_live_coral_input = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'parameters'}), choices=(('Y', 'Include'), ('N', 'Exclude')), initial='Y')
    #
    # mooring_buoy = forms.BooleanField(label="Mooring Buoys", required=False, help_text="Planning units that contain at least one mooring buoy.", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 441, 'layer_title': 'Show Mooring Buoys'}))
    # mooring_buoy_input = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'parameters'}), choices=(('Y', 'Include'), ('N', 'Exclude')), initial='Y')
    #
    # mooring_desc = forms.BooleanField(label="Mooring (Berhinger data)", required=False, help_text="Planning units that contain numbers of moored boats based on a point density analysis at 500 m radius around each moored boat observed.", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 416, 'layer_title': "Show Moored Boat Density (2012-2014)"}))
    # mooring_desc_input = forms.ChoiceField(
    #     required=False,
    #     widget=forms.Select(attrs={'class': 'parameters', 'pre_text': 'at least'}),
    #     choices=(('Low', 'Low'),
    #              ('Medium', 'Medium'),
    #              ('High', 'High'),
    #              ('Very High', 'Very High')),
    #     initial='Low')
    #
    # outfall_distance = forms.BooleanField(label="Distance from Outfall", required=False, help_text="Distance from nearest outfall in miles", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 350, 'layer_title': 'Show Outfall Locations'}))
    # outfall_distance_min = forms.FloatField(required=False, initial=20, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # outfall_distance_max = forms.FloatField(required=False, initial=40, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to', 'post_text': 'miles'}))
    # outfall_distance_input = forms.FloatField(widget=DualSliderWidget('outfall_distance_min', 'outfall_distance_max', min=0, max=60, step=0.5))
    #
    # pier_distance = forms.BooleanField(label="Distance from Pier", required=False, help_text="Distance from nearest pier in miles", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 326, 'layer_title': 'Show Pier Locations'}))
    # pier_distance_min = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # pier_distance_max = forms.FloatField(required=False, initial=20, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to', 'post_text': 'miles'}))
    # pier_distance_input = forms.FloatField(widget=DualSliderWidget('pier_distance_min', 'pier_distance_max', min=0, max=22, step=0.5))
    #
    # pillar_presence = forms.BooleanField(label="Pillar Corals", required=False, help_text="Planning units that contain at least one known pillar coral. (FWC database)", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 398, 'layer_title': 'Show Pillar Coral Sites'}))
    # pillar_presence_input = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'parameters'}), choices=(('Y', 'Include'), ('N', 'Exclude')), initial='P')
    #
    # prcnt_art = forms.BooleanField(label="Percent Artificial Substrate", required=False, help_text="Minimum percent of mapped artificial substrate area (including dump sites, outfall pipes and designated artificial reefs) within each planning unit", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 436, 'layer_title': 'Show Artificial Habitat'}))
    # prcnt_art_min = forms.FloatField(required=False, initial=30, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'Minimum Percentage'}))
    # prcnt_art_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # prcnt_art_input = forms.FloatField(widget=DualSliderWidget('prcnt_art_min', 'prcnt_art_max', min=0, max=100, step=10))
    #
    # prcnt_reef = forms.BooleanField(label="Percent Reef", required=False, help_text="Minimum percent of mapped reef area within each planning unit", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 437, 'layer_title': 'Show Coral Reef and Hardbottom Habitat'}))
    # prcnt_reef_min = forms.FloatField(required=False, initial=30, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'Minimum Percentage'}))
    # prcnt_reef_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # prcnt_reef_input = forms.FloatField(widget=DualSliderWidget('prcnt_reef_min', 'prcnt_reef_max', min=0, max=100, step=10))
    #
    # prcnt_sand = forms.BooleanField(label="Percent Sand", required=False, help_text="Minimum percent of mapped sand area within each planning unit", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 438, 'layer_title': 'Show Sand Habitat'}))
    # prcnt_sand_min = forms.FloatField(required=False, initial=30, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'Minimum Percentage'}))
    # prcnt_sand_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # prcnt_sand_input = forms.FloatField(widget=DualSliderWidget('prcnt_sand_min', 'prcnt_sand_max', min=0, max=100, step=10))
    #
    # prcnt_sg = forms.BooleanField(label="Percent Seagrass", required=False, help_text="Minimum percent of mapped seagrass area within each planning unit", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 439, 'layer_title': 'Show Seagrass Habitat'}))
    # prcnt_sg_min = forms.FloatField(required=False, initial=30, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'Minimum Percentage'}))
    # prcnt_sg_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # prcnt_sg_input = forms.FloatField(widget=DualSliderWidget('prcnt_sg_min', 'prcnt_sg_max', min=0, max=100, step=10))
    #
    # reccom_fish = forms.BooleanField(label="Recreationally and commercially important fishes", required=False, help_text="Mean density of recreationally and commercially important fish per Secondary Sampling Unit (RVC 2012 & 2013)", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 428, 'layer_title': "Show Recreationally and commercially important fish density"}))
    # reccom_fish_min = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # reccom_fish_max = forms.FloatField(required=False, initial=500, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # reccom_fish_input = forms.FloatField(widget=DualSliderWidget('reccom_fish_min', 'reccom_fish_max', min=0, max=2275, step=1))
    #
    # recfish_use = forms.BooleanField(label="Recreational Fishing Use Intensity (OFR 2015)", required=False, help_text="Planning units that contain at least one entry for recreational fishing in the 2015 OFR survey", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    #     #, 'layer_id': 420, 'layer_title': "Show Recreational Fishing Activities"}))
    # recfish_use_min = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # recfish_use_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # recfish_use_input = forms.FloatField(widget=DualSliderWidget('recfish_use_min', 'recfish_use_max', min=0, max=100, step=10))
    #
    # reef_fish_density = forms.BooleanField(label="Relative Reef Fish Density", required=False, help_text="Mean fish density per Secondary Sampling Unit (RVC 2012 & 2013)", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 427, 'layer_title': "Show Relative Reef Fish Density"}))
    # reef_fish_density_min = forms.FloatField(required=False, initial=10, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # reef_fish_density_max = forms.FloatField(required=False, initial=500, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # reef_fish_density_input = forms.FloatField(widget=DualSliderWidget('reef_fish_density_min', 'reef_fish_density_max', min=0, max=5571, step=1))
    #
    # reef_fish_richness = forms.BooleanField(label="Number of Reef Fish Species", required=False, help_text="Number of fish species per Secondary Sampling Unit (RVC 2012 & 2013)", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 426, 'layer_title': "Show Number of Reef Fish Species"}))
    # reef_fish_richness_min = forms.FloatField(required=False, initial=2, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # reef_fish_richness_max = forms.FloatField(required=False, initial=20, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # reef_fish_richness_input = forms.FloatField(widget=DualSliderWidget('reef_fish_richness_min', 'reef_fish_richness_max', min=0, max=56, step=1))
    #
    # scuba_use = forms.BooleanField(label="Scuba Diving Use Intensity (OFR 2015)", required=False, help_text="Planning units that contain at least one entry for SCUBA diving in the 2015 OFR survey", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    #     # , 'layer_id': 419, 'layer_title': "Show Scuba Diving Activities"}))
    # scuba_use_min = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # scuba_use_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # scuba_use_input = forms.FloatField(widget=DualSliderWidget('scuba_use_min', 'scuba_use_max', min=0, max=630, step=10))
    #
    # shore_distance = forms.BooleanField(label="Distance from Shore", required=False, help_text="Distance from nearest shore in miles", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    # shore_distance_min = forms.FloatField(required=False, initial=2, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # shore_distance_max = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to', 'post_text': 'miles'}))
    # shore_distance_input = forms.FloatField(widget=DualSliderWidget('shore_distance_min', 'shore_distance_max', min=0, max=10, step=0.5))
    #
    # spear_use = forms.BooleanField(label="Spearfishing Use Intensity (OFR 2015)", required=False, help_text="Planning units that contain at least one entry for spearfishing in the 2015 OFR survey", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    #     # , 'layer_id': 422, 'layer_title': "Show Spearfishing Activities"}))
    # spear_use_min = forms.FloatField(required=False, initial=10, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # spear_use_max = forms.FloatField(required=False, initial=40, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # spear_use_input = forms.FloatField(widget=DualSliderWidget('spear_use_min', 'spear_use_max', min=0, max=50, step=10))
    #
    # sponge = forms.BooleanField(label="Sponge Percent Cover", required=False, help_text="The maximum value of percent sponge cover in all compiled benthic survey sites within the Planning Unit", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 408, 'layer_title': 'Show Percent Sponge Cover'}))
    # sponge_min = forms.FloatField(required=False, initial=2, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # sponge_max = forms.FloatField(required=False, initial=20, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to', 'post_text': 'percent'}))
    # sponge_input = forms.FloatField(widget=DualSliderWidget('sponge_min', 'sponge_max', min=0, max=32, step=1))
    #
    # total_use = forms.BooleanField(label="Total Use Intensity (OFR 2015)", required=False, help_text="Planning units that contain at least one entry in the 2015 OFR survey", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    #     # todo sublayers, 'layer_id': 417, 'layer_title': 'Show All Activities'}))
    # total_use_min = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # total_use_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # total_use_input = forms.FloatField(widget=DualSliderWidget('total_use_min', 'total_use_max', min=0, max=720, step=10))
    #
    # watersport_use = forms.BooleanField(label="Water Sports (OFR 2015)", required=False, help_text="Planning units that contain at least one entry for watersports in the 2015 OFR survey", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    #     # , 'layer_id': 423, 'layer_title': "Show Water Sports Activities"}))
    # watersport_use_min = forms.FloatField(required=False, initial=5, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': ''}))
    # watersport_use_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # watersport_use_input = forms.FloatField(widget=DualSliderWidget('watersport_use_min', 'watersport_use_max', min=0, max=60, step=10))

    # Habitat
    def get_step_1_fields(self):
        """Defines the fields that we want to show on the form in step 1, and
        the order in which they appear, and in groups of
            (parameter to test, user-min or user-selection, user-max, user-input)
        where each parameter except the first is optional.
        """
        names = (
                ('ecoregion', None, None, 'ecoregion_input'),
                # ('depth_mean', 'depth_mean_min', 'depth_mean_max', 'depth_mean_input'),
                # ('shore_distance', 'shore_distance_min', 'shore_distance_max', 'shore_distance_input'),
                # ('prcnt_reef', 'prcnt_reef_min', 'prcnt_reef_max', 'prcnt_reef_input'),
                # ('prcnt_sand', 'prcnt_sand_min', 'prcnt_sand_max', 'prcnt_sand_input'),
                # ('prcnt_sg', 'prcnt_sg_min', 'prcnt_sg_max', 'prcnt_sg_input'),
                # ('prcnt_art', 'prcnt_art_min', 'prcnt_art_max', 'prcnt_art_input'),
                # ('sponge', 'sponge_min', 'sponge_max', 'sponge_input'),
        )

        return self._get_fields(names)

    # Coral
    # def get_step_2_fields(self):
    #     names = (
    #             ('coral_density', 'coral_density_min', 'coral_density_max', 'coral_density_input'),
    #             ('coral_cover', 'coral_cover_min', 'coral_cover_max', 'coral_cover_input'),
    #             ('coral_richness', 'coral_richness_min', 'coral_richness_max', 'coral_richness_input'),
    #             ('large_live_coral', None, None, 'large_live_coral_input'),
    #             ('acropora_pa', None, None, 'acropora_pa_input'),
    #             ('pillar_presence', None, None, 'pillar_presence_input'),
    #             ('coral_bleach', 'coral_bleach_min', 'coral_bleach_max', 'coral_bleach_input'),
    #             ('coral_disease', 'coral_disease_min', 'coral_disease_max', 'coral_disease_input'),
    #             ('coral_resilience', 'coral_resilience_min', 'coral_resilience_max', 'coral_resilience_input'),
    #             ('coral_soft', 'coral_soft_min', 'coral_soft_max', 'coral_soft_input'),
    #             )
    #
    #     return self._get_fields(names)

    # Fish
    # def get_step_3_fields(self):
    #     names = (
    #             ('reef_fish_density', 'reef_fish_density_min', 'reef_fish_density_max', 'reef_fish_density_input'),
    #             ('reef_fish_richness', 'reef_fish_richness_min', 'reef_fish_richness_max', 'reef_fish_richness_input'),
    #             ('reccom_fish', 'reccom_fish_min', 'reccom_fish_max', 'reccom_fish_input'),
    #             )
    #
    #     return self._get_fields(names)

    # People
    # def get_step_4_fields(self):
    #     names = (
    #             ('total_use', 'total_use_min', 'total_use_max', 'total_use_input'),
    #             ('boat_use', 'boat_use_min', 'boat_use_max', 'boat_use_input'),
    #             ('recfish_use', 'recfish_use_min', 'recfish_use_max', 'recfish_use_input'),
    #             ('scuba_use', 'scuba_use_min', 'scuba_use_max', 'scuba_use_input'),
    #             ('extdive_use', 'extdive_use_min', 'extdive_use_max', 'extdive_use_input'),
    #             ('spear_use', 'spear_use_min', 'spear_use_max', 'spear_use_input'),
    #             ('divefish_overlap', 'divefish_overlap_min', 'divefish_overlap_max', 'divefish_overlap_input'),
    #             ('watersport_use', 'watersport_use_min', 'watersport_use_max', 'watersport_use_input'),
    #             ('anchor_desc', None, None, 'anchor_desc_input'),
    #             ('mooring_desc', None, None, 'mooring_desc_input'),
    #             )
    #
    #     return self._get_fields(names)

    # Management
    # def get_step_5_fields(self):
    #     names = (
    #             ('pier_distance', 'pier_distance_min', 'pier_distance_max', 'pier_distance_input'),
    #             ('inlet_distance', 'inlet_distance_min', 'inlet_distance_max', 'inlet_distance_input'),
    #             ('outfall_distance', 'outfall_distance_min', 'outfall_distance_max', 'outfall_distance_input'),
    #             ('mooring_buoy', None, None, 'mooring_buoy_input'),
    #             ('anchorage', None, None, 'anchorage_input'),
    #             ('injury_site', None, None, 'injury_site_input'),
    #             ('impacted', None, None, 'impacted_input'),
    #             )
    #
    #     return self._get_fields(names)

    def get_steps(self):

        return (self.get_step_1_fields(),)
        # return self.get_step_1_fields(), \
        #        self.get_step_2_fields(), \
        #        self.get_step_3_fields(), \
        #        self.get_step_4_fields(), \
        #        self.get_step_5_fields()

    def _get_fields(self, names):

        fields = []
        for name_list in names:
            group = []
            for name in name_list:
                if name:
                    group.append(self[name])
                else:
                    group.append(None)
            fields.append(group)
        return fields

    def save(self, commit=True):
        inst = super(FeatureForm, self).save(commit=False)
        if self.data.get('clear_support_file'):
            inst.support_file = None
        if commit:
            inst.save()
        return inst

    class Meta(FeatureForm.Meta):
        model = Scenario
        exclude = list(FeatureForm.Meta.exclude)
        for f in model.output_fields():
            exclude.append(f.attname)

        widgets = {

        }
