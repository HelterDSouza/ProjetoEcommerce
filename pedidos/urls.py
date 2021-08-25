from django.urls import path

from . import views

app_name = "perdidos"


urlpatterns = [
    path(
        "pagar/",
        views.PagarView.as_view(),
        name="pedidos-pagar",
    ),
    path(
        "fecharpedido/",
        views.FecharPedidoView.as_view(),
        name="pedidos-fecharpedido",
    ),
    path(
        "detalhe/<int:pk>/",
        views.PedidoDetailView.as_view(),
        name="pedidos-detalhes",
    ),
]
