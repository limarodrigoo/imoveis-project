from rest_framework import viewsets, generics, filters
from imovel_app.models import Imovel
from anuncios_app.models import Anuncio
from django_filters.rest_framework import DjangoFilterBackend
from imovel_app.serializer import ImovelSerializer, ListaImoveisAnuncioSerializer


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


class ListaImoveisAnuncio(generics.ListAPIView):
    """Lista anuncios por imoveis"""

    def get_queryset(self):
        queryset = Anuncio.objects.filter(imovel=self.kwargs["pk"])
        return queryset

    serializer_class = ListaImoveisAnuncioSerializer
