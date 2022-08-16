from django import template

register = template.Library()


@register.filter
def clean_slug(value):
    """Removes all values of arg from the given string"""
    return value.replace(" ", "-")
