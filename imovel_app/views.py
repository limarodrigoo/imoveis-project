from rest_framework import viewsets, generics, filters
from imovel_app.models import Imovel
from django_filters.rest_framework import DjangoFilterBackend
from imovel_app.serializer import ImovelSerializer


class ImoveisViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Imóveis"""

    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["id", "limite_de_hospedes", "banheiros"]
    search_fields = ["id", "limite_de_hospedes", "banheiros"]
    filterset_fields = ["pet_friendly"]
