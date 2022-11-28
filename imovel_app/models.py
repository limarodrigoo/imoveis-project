from django.db import models
from django.utils import timezone


class Imovel(models.Model):
    limite_de_hospedes = models.PositiveIntegerField(default=0)
    banheiros = models.PositiveIntegerField()
    pet_friendly = models.BooleanField()
    limpeza = models.DecimalField(max_digits=6, decimal_places=2)
    data_ativacao = models.DateField(default=timezone.localdate, blank=True)
    criacao = models.DateTimeField(default=timezone.now, blank=True)
    atualizacao = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.id}"
