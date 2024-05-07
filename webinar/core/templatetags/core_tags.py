from django import template
from django.http import HttpRequest

register = template.Library()


@register.filter(name="is_localhost")
def is_localhost(request: HttpRequest) -> bool:
    return request.META["HTTP_HOST"] == "127.0.0.1:8000"
