from django import template
from utils.utils import total_cart_quantity

register = template.Library()


@register.filter
def format_price(value: int) -> str:

    return f"R$ {value:.2f}".replace(".", ",")


@register.filter
def total_cart_qnd(value):
    return total_cart_quantity(value)
