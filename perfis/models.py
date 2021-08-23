from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from perfis.choices import Estados


# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        choices=Estados.choices,
        default=Estados.RIO_DE_JANEIRO,
    )

    class Meta:
        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfis")

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

    def clean(self) -> None:
        return super().clean()

    def get_absolute_url(self):
        return reverse("perfil_detail", kwargs={"pk": self.pk})
