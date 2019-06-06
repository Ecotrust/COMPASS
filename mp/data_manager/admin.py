from django.contrib import admin
from data_manager.models import *
from django.forms import CheckboxSelectMultiple, ModelForm

class TOCAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

    formfield_overrides = {
        models.ManyToManyField: {'widget': admin.widgets.FilteredSelectMultiple('Themes', False) }
    }

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "themes":
            kwargs["queryset"] = TOCTheme.objects.all().order_by('name')
        return super(TOCAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

class TOCThemeForm(ModelForm):
    # fields = ['display_name','name','description','subthemes','layers','order']
    class Meta:
        model = TOCTheme
        fields = '__all__'
        widgets = {
            'subthemes': admin.widgets.FilteredSelectMultiple('Subthemes', False),
            'layers': admin.widgets.FilteredSelectMultiple('Layers', False)
        }

class TOCThemeAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'name', 'TOC', 'order', 'id')
    form = TOCThemeForm

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "layers":
            kwargs["queryset"] = Layer.objects.filter(is_sublayer=False).order_by('name').order_by('order')
        return super(TOCThemeAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

class TOCSubThemeAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'name', 'TOCTheme', 'order', 'id')

    formfield_overrides = {
        models.ManyToManyField: {'widget': admin.widgets.FilteredSelectMultiple('Layers', False) }
    }

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "layers":
            kwargs["queryset"] = Layer.objects.filter(is_sublayer=False).order_by('name').order_by('order')
        return super(TOCSubThemeAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'name', 'id')
    pass


class LayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'layer_type', 'url')
    search_fields = ['name', 'layer_type', 'url']
    ordering = ('name',)
    exclude = (
        'slug_name',
        'shareable_url',
        'proxy_url',
        # 'arcgis_layers',
        # 'wms_slug',
        'sublayers',
        'themes',
        'is_sublayer',
        'legend',
        'legend_title',
        'legend_subtitle',
        'utfurl',
        'utfjsonp',
        'summarize_to_grid',
        'filterable',
        # 'proj',
        'data_overview',
        'bookmark',
        'map_tiles',
        'kml',
        'attribute_title',
        'attribute_fields',
        'compress_display',
        'attribute_event',
        'lookup_field',
        'lookup_table',
        'vector_color',
        'vector_fill',
        'vector_graphic',
        'opacity'
    )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "sublayers":
            kwargs["queryset"] = Layer.objects.order_by('name').order_by('order')
        if db_field.name == "themes":
            kwargs["queryset"] = Theme.objects.order_by('name').order_by('order')
        if db_field.name == "attribute_fields":
            kwargs["queryset"] = AttributeInfo.objects.order_by('field_name')
        return super(LayerAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

class AttributeInfoAdmin(admin.ModelAdmin):
    list_display = ('field_name', 'display_name', 'precision', 'order')

class LookupInfoAdmin(admin.ModelAdmin):
    list_display = ('value', 'color', 'dashstyle', 'fill', 'graphic')

class DataNeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class PortAdmin(admin.ModelAdmin):
    list_display = ('data_file', 'user', 'status', 'current', 'date_created')

admin.site.register(TOC, TOCAdmin)
admin.site.register(TOCTheme, TOCThemeAdmin)
admin.site.register(TOCSubTheme, TOCSubThemeAdmin)
# admin.site.register(Theme, ThemeAdmin)
admin.site.register(Layer, LayerAdmin)
admin.site.register(AttributeInfo, AttributeInfoAdmin)
admin.site.register(LookupInfo, LookupInfoAdmin)
admin.site.register(DataNeed, DataNeedAdmin)
admin.site.register(ImportEvent, PortAdmin)
