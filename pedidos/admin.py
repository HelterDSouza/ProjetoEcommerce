from django.contrib import admin

from .models import ItemPedido, Pedido

# Register your models here.


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    pass


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
