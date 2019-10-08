from django.contrib.sites.models import Site
from settings import *

def get_domain(port=8010):
    try:
        #domain = Site.objects.all()[0].domain
        domain = Site.objects.get(id=SITE_ID).domain
        if 'localhost' in domain:
            domain = 'localhost:%s' %port
        if DEFAULT_PROTOCOL:
            domain = DEFAULT_PROTOCOL + domain
        else:
            domain = 'https://' + domain
    except:
        domain = '..'
    #print(domain)
    return domain
