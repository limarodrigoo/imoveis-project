from rest_framework import serializers
from imovel_app.models import Imovel
from anuncios_app.models import Anuncio


class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = "__all__"

class ListaImoveisAnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = ["id", "imovel", "plataforma", "taxa_plataforma"]
