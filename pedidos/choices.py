from django.db import models


class PedidoStatus(models.TextChoices):
    APROVADO: str = "A", "Aprovado"
    CRIADO: str = "C", "Criado"
    REPROVADO: str = "R", "Reprovado"
    PENDENTE: str = "P", "Pendente"
    ENVIADO: str = "E", "Enviado"
    FINALIZADO: str = "F", "Finalizado"
