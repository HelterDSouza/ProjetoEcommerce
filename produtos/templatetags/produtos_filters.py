from django import template
from utils.utils import cart_total_prices, cart_total_quantity

register = template.Library()


@register.filter
def format_price(value: int) -> str:

    return f"R$ {value:.2f}".replace(".", ",")


@register.filter(name="cart_total_quantity")
def produto_cart_total_quantity(value):
    return cart_total_quantity(value)


@register.filter(name="cart_total_prices")
def produto_cart_total_prices(value):
    return cart_total_prices(value)
