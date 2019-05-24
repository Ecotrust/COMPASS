from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.utils import simplejson
from content.models import *

def get_content(request):
    contents = Content.objects.all()
    content_dict = {}
    for content in contents:
        content_dict[content.name] = {
            "name": content.name,
            "display_name": content.display_name,
            "description": content.description,
            "content": content.content
        }
    return HttpResponse(simplejson.dumps(content_dict))
