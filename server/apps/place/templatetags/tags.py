from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_yandex_api_key():
    return settings.YANDEX_API_KEY
