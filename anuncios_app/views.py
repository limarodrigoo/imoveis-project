from rest_framework import viewsets, filters
from anuncios_app.models import Anuncio
from anuncios_app.serializer import AnuncioSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AnuncioViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Anuncios"""

    queryset = Anuncio.objects.all().order_by('id')
    serializer_class = AnuncioSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["taxa_plataforma", "id"]
    search_fields = ["plataforma", "id"]
