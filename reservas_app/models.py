from django.db import models
from anuncios_app.models import Anuncio
from django.utils import timezone
import uuid


class Reserva(models.Model):
    codigo_reserva = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    anuncio_id = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    preco_total = models.DecimalField(max_digits=6, decimal_places=2)
    comentario = models.CharField(max_length=256)
    qtd_hospedes = models.PositiveIntegerField()
    criacao = models.DateTimeField(default=timezone.now, blank=True)
    atualizacao = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.codigo_reserva}"
