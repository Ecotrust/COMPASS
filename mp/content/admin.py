from django.contrib import admin
from models import *
# from django.forms import CheckboxSelectMultiple

class ContentAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'name', 'description')

admin.site.register(Content, ContentAdmin)
