from django import template

register = template.Library()


@register.filter
def format_price(value: int) -> str:

    return f"R$ {value:.2f}".replace(".", ",")
