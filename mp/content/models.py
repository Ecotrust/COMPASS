from django.db import models
from tinymce.models import HTMLField

class Content(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=255)
    description = models.TextField()
    content = HTMLField()
