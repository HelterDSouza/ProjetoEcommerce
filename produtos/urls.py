from django.urls import path

from . import views

app_name = "produtos"


urlpatterns = [
    path(
        "",
        views.ProdutoListView.as_view(),
        name="produtos-lista",
    ),
    path(
        "addcarrinho/",
        views.AddCarrinhoView.as_view(),
        name="produtos-addcarrinho",
    ),
    path(
        "removecarrinho/",
        views.RemoverCarrinhoView.as_view(),
        name="produtos-removecarrinho",
    ),
    path(
        "carrinho/",
        views.CarrinhoView.as_view(),
        name="produtos-carrinho",
    ),
    path(
        "resumocompra/",
        views.ResumoComprarView.as_view(),
        name="produtos-resumoCompra",
    ),
    path(
        "<slug:slug>/",
        views.ProdutoDetailView.as_view(),
        name="produtos-detalhe",
    ),
]
