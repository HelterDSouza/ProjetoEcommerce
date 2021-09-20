from django.urls import path

from . import views

app_name = "perdidos"


urlpatterns = [
    path(
        "",
        views.PagarView.as_view(),
        name="pedidos-pagar",
    ),
    path(
        "salvarpedido/",
        views.SalvarPedidoView.as_view(),
        name="pedidos-salvarpedido",
    ),
    path(
        "detalhe/<int:pk>/",
        views.PedidoDetailView.as_view(),
        name="pedidos-detalhes",
    ),
]
