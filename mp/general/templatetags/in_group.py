from django import template
# from django.utils.encoding import force_unicode
try:
    from django.utils.encoding import force_unicode  # Django in Python 2
except ImportError:
    from django.utils.encoding import force_text as force_unicode  # Django in Python 3

register = template.Library()

@register.filter
def in_group(user, groups):
    """Returns a boolean if the user is in the given group, or comma-separated
    list of groups.

    Usage::

        {% if user|in_group:"Friends" %}
        ...
        {% endif %}

    or::

        {% if user|in_group:"Friends,Enemies" %}
        ...
        {% endif %}

    """
    group_list = force_unicode(groups).split(',')
    return bool(user.groups.filter(name__in=group_list).values('name'))
