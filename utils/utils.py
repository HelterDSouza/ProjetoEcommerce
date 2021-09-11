def cart_total_quantity(carrinho):
    return sum([item.get("quantidade") for item in carrinho.values()])


def cart_total_prices(carrinho: dict):
    total = 0

    for item in carrinho.values():
        if item.get("preco_quantitativo_promocional"):
            total += item.get("preco_quantitativo_promocional")
            continue

        total += item.get("preco_quantitativo")

    return total
