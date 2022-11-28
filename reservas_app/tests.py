from rest_framework.test import APITestCase
from django.urls import reverse
from reservas_app.models import Reserva
from imovel_app.models import Imovel
from anuncios_app.models import Anuncio
from rest_framework import status


class ImovelTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Reservas-list")
        self.imovel = Imovel.objects.create(
            limite_de_hospedes=2,
            banheiros=1,
            pet_friendly=False,
            limpeza=30,
        )
        self.anuncio = Anuncio.objects.create(
            imovel=self.imovel, plataforma="airbnb", taxa_plataforma=59
        )

    def test_post_reservation(self):
        wrong_data = {
            "anuncio_id": 1,
            "check_in": "2022-11-28",
            "check_out": "2022-11-21",
            "preco_total": 199,
            "comentario": "ok",
            "qtd_hospedes": 4,
        }
        data = {
            "anuncio_id": 1,
            "check_in": "2022-11-21",
            "check_out": "2022-11-28",
            "preco_total": 199,
            "comentario": "ok",
            "qtd_hospedes": 4,
        }
        response = self.client.post(self.list_url, data=wrong_data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        response2 = self.client.post(self.list_url, data=data)
        print(response2.data)
        self.assertEquals(response2.status_code, status.HTTP_201_CREATED)
