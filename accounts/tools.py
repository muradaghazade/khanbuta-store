# ** Python Imports **
import re

# ** Django Imports **
from django.core.exceptions import ValidationError

def get_or_none(m, *args, **kwargs):
    try:
        return m.objects.get(*args, **kwargs)
    except Exception as e:
        return None


def url_field_validator(value):
    pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        # domain...
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if not pattern.match(value):
        raise ValidationError('Send valid url')
    return True
