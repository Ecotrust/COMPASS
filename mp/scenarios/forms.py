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

    # acropora_pa = forms.BooleanField(label="Dense Acropora patches", required=False, help_text="Planning units that contain at least part of a known dense Acropora patch.", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 440, 'layer_title': "Show Dense Acropora patches"}))
    # acropora_pa_input = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'parameters'}), choices=(('Y', 'Include'), ('N', 'Exclude')), initial='Y')
    #
    # anchor_desc = forms.BooleanField(label="Anchoring (Berhinger data)", required=False, help_text="Planning units that contain numbers of anchored boats based on a point density analysis at 500 m radius around each anchored boat observed.", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 415, 'layer_title': "Show Anchored Boat Density (2012-2014)"}))
    # anchor_desc_input = forms.ChoiceField(
    #     required=False,
    #     widget=forms.Select(attrs={'class': 'parameters', 'pre_text': 'at least'}),
    #     choices=(('Low', 'Low'),
    #              ('Medium', 'Medium'),
    #              ('High', 'High'),
    #              ('Very High', 'Very High')),
    #     initial='Low')

    # Habitat
    def get_step_1_fields(self):
        """Defines the fields that we want to show on the form in step 1, and
        the order in which they appear, and in groups of
            (parameter to test, user-min or user-selection, user-max, user-input)
        where each parameter except the first is optional.
        """
        names = (
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
    def get_step_2_fields(self):
        names = (
                # ('coral_density', 'coral_density_min', 'coral_density_max', 'coral_density_input'),
                # ('coral_cover', 'coral_cover_min', 'coral_cover_max', 'coral_cover_input'),
                # ('coral_richness', 'coral_richness_min', 'coral_richness_max', 'coral_richness_input'),
                # ('large_live_coral', None, None, 'large_live_coral_input'),
                # ('acropora_pa', None, None, 'acropora_pa_input'),
                # ('pillar_presence', None, None, 'pillar_presence_input'),
                # ('coral_bleach', 'coral_bleach_min', 'coral_bleach_max', 'coral_bleach_input'),
                # ('coral_disease', 'coral_disease_min', 'coral_disease_max', 'coral_disease_input'),
                # ('coral_resilience', 'coral_resilience_min', 'coral_resilience_max', 'coral_resilience_input'),
                # ('coral_soft', 'coral_soft_min', 'coral_soft_max', 'coral_soft_input'),
                )

        return self._get_fields(names)

    # Fish
    def get_step_3_fields(self):
        names = (
                # ('reef_fish_density', 'reef_fish_density_min', 'reef_fish_density_max', 'reef_fish_density_input'),
                # ('reef_fish_richness', 'reef_fish_richness_min', 'reef_fish_richness_max', 'reef_fish_richness_input'),
                # ('reccom_fish', 'reccom_fish_min', 'reccom_fish_max', 'reccom_fish_input'),
                )

        return self._get_fields(names)

    # People
    def get_step_4_fields(self):
        names = (
                # ('total_use', 'total_use_min', 'total_use_max', 'total_use_input'),
                # ('boat_use', 'boat_use_min', 'boat_use_max', 'boat_use_input'),
                # ('recfish_use', 'recfish_use_min', 'recfish_use_max', 'recfish_use_input'),
                # ('scuba_use', 'scuba_use_min', 'scuba_use_max', 'scuba_use_input'),
                # ('extdive_use', 'extdive_use_min', 'extdive_use_max', 'extdive_use_input'),
                # ('spear_use', 'spear_use_min', 'spear_use_max', 'spear_use_input'),
                # ('divefish_overlap', 'divefish_overlap_min', 'divefish_overlap_max', 'divefish_overlap_input'),
                # ('watersport_use', 'watersport_use_min', 'watersport_use_max', 'watersport_use_input'),
                # ('anchor_desc', None, None, 'anchor_desc_input'),
                # ('mooring_desc', None, None, 'mooring_desc_input'),
                )

        return self._get_fields(names)

    # Management
    def get_step_5_fields(self):
        names = (
                # ('pier_distance', 'pier_distance_min', 'pier_distance_max', 'pier_distance_input'),
                # ('inlet_distance', 'inlet_distance_min', 'inlet_distance_max', 'inlet_distance_input'),
                # ('outfall_distance', 'outfall_distance_min', 'outfall_distance_max', 'outfall_distance_input'),
                # ('mooring_buoy', None, None, 'mooring_buoy_input'),
                # ('anchorage', None, None, 'anchorage_input'),
                # ('injury_site', None, None, 'injury_site_input'),
                # ('impacted', None, None, 'impacted_input'),
                )

        return self._get_fields(names)

    def get_steps(self):
        return self.get_step_1_fields(), \
               self.get_step_2_fields(), \
               self.get_step_3_fields(), \
               self.get_step_4_fields(), \
               self.get_step_5_fields()

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
