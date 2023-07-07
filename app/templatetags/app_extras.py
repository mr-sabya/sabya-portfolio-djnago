from django import template
from datetime import date

register = template.Library()


@register.simple_tag
def calculate_age(birth_day):
    today = date.today()
    return today.year - birth_day.year - ((today.month, today.day) < (birth_day.month, birth_day.day))