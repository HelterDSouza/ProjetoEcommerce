from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from produtos.choices import TipoProduto

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(
        max_length=255,
    )
    descricao_curta = models.TextField()
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to="produtos_imagens/%Y/%m/",
        blank=True,
        null=True,
    )
    slug = models.SlugField(unique=True)
    preco_marketing = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    preco_marketing_promocional = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
    )
    tipo = models.CharField(
        choices=TipoProduto.choices,
        default=TipoProduto.VARIAVEL,
        max_length=1,
    )

    class Meta:
        verbose_name = _("produto")
        verbose_name_plural = _("produtos")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("produto_detail", kwargs={"pk": self.pk})
