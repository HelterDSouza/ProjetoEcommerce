from django.contrib import admin

# Register your models here.
from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    model = Produto
    inlines = [VariacaoInline]
    list_display = [
        "nome",
        "preco_marketing",
        "preco_marketing_promocional",
        "tipo",
    ]


@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    model = Variacao
