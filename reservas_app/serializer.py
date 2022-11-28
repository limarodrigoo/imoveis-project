from rest_framework import serializers
from reservas_app.models import Reserva
from reservas_app.validators import *


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = [
            "codigo_reserva",
            "anuncio_id",
            "check_in",
            "check_out",
            "comentario",
            "qtd_hospedes",
            "preco_total",
        ]
    def validate(self, data):
        if data_invalida(data['check_in'], data['check_out']):
            raise serializers.ValidationError({"check_out":"A data de check-out deve ser posterior a de check-in"})
        return data
