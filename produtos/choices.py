from django.db import models


class TipoProduto(models.TextChoices):
    VARIAVEL: str = "V", "Variável"
    SIMPLES: str = "S", "Simples"
