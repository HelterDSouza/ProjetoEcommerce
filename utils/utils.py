def total_cart_quantity(carrinho):
    return sum([item.get("quantidade") for item in carrinho.values()])
