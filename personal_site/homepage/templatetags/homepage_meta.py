from django import template
from django.urls import reverse

register = template.Library()


NAVBAR_LINKS = (
    ("Home", "homepage:home"),
    ("Dashboard", "homepage:dashboard"),
)


@register.simple_tag
def navbar_links():
    return [(name, reverse(url)) for name, url in NAVBAR_LINKS]
