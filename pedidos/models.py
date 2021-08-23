from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from pedidos.choices import PedidoStatus

# Create your models here.


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        choices=PedidoStatus.choices,
        default=PedidoStatus.CRIADO,
        max_length=1,
    )

    class Meta:
        verbose_name = _("pedido")
        verbose_name_plural = _("pedidos")

    def __str__(self):
        return f"Pedido N. {self.pk}"

    def get_absolute_url(self):
        return reverse("pedido_detail", kwargs={"pk": self.pk})


# TODO Usar GenericRelations
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    variacao = models.CharField(max_length=255)
    variacao_id = models.PositiveIntegerField()
    preco = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    preco_promocional = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)

    class Meta:
        verbose_name = _("Item do Pedido")
        verbose_name_plural = _("Itens do Pedido")

    def __str__(self):
        return f"Item do {self.pedido}"

    def get_absolute_url(self):
        return reverse("itempedido_detail", kwargs={"pk": self.pk})
