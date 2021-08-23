from django.contrib import admin

# Register your models here.
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "preco_marketing",
        "preco_marketing_promocional",
        "tipo",
    ]
