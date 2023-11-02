from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def display_stars(value, stars_max=5):
    """Display a given number of stars as rating."""

    if value > stars_max:
        result = '<i class="fa fa-star" style="color: darkblue;"></i>' * stars_max
        return mark_safe(result)
    elif value < 1:
        result = '<i class="fa fa-star" style="color: lightgrey;"></i>' * stars_max
        return mark_safe(result)

    result = (
        '<i class="fa fa-star" style="color: darkblue;"></i>' * value +
        '<i class="fa fa-star" style="color: lightgrey;"></i>' * (
            stars_max - value)
    )
    return mark_safe(result)

