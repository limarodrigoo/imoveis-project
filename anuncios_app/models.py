from django.db import models
from imovel_app.models import Imovel
from django.utils import timezone


class Anuncio(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    plataforma = models.CharField(max_length=30)
    taxa_plataforma = models.DecimalField(max_digits=6, decimal_places=2)
    criacao = models.DateTimeField(default=timezone.now, blank=True)
    atualizacao = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.id}"
