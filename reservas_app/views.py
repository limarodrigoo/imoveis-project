from rest_framework import viewsets
from reservas_app.models import Reserva
from reservas_app.serializer import ReservaSerializer

# Create your views here.
class ReservaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as reservas"""

    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
