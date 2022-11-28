from rest_framework import serializers
from anuncios_app.models import Anuncio

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = [
            "id",
            "imovel",
            "plataforma",
            "taxa_plataforma",
        ]