from rest_framework import viewsets, filters
from reservas_app.models import Reserva
from reservas_app.serializer import ReservaSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class ReservaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as reservas"""

    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    ordering_fields = ["preco_total"]
