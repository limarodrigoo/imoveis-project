from rest_framework import viewsets, filters
from reservas_app.models import Reserva
from reservas_app.serializer import ReservaSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class ReservaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as reservas"""

    queryset = Reserva.objects.all().order_by("codigo_reserva")
    serializer_class = ReservaSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["preco_total", "id"]
    search_fields = ["id"]
