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
        self.reserva = Reserva.objects.create(
            anuncio_id=self.anuncio,
            check_in="2022-10-21",
            check_out="2022-10-28",
            preco_total=123.23,
            comentario="bom",
            qtd_hospedes=2,
        )

    def test_list_reservation(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_reservation(self):

        data = {
            "anuncio_id": self.anuncio.id,
            "check_in": "2022-11-21",
            "check_out": "2022-11-28",
            "comentario": "ok",
            "preco_total": 199,
            "qtd_hospedes": 4,
        }

        response2 = self.client.post(self.list_url, data=data)
        self.assertEquals(response2.status_code, status.HTTP_201_CREATED)

    def test_wrong_post_reservation(self):
        wrong_data = {
            "anuncio_id": self.anuncio.id,
            "check_in": "2022-11-28",
            "check_out": "2022-11-21",
            "comentario": "ok",
            "preco_total": 199,
            "qtd_hospedes": 4,
        }
        response = self.client.post(self.list_url, data=wrong_data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_reservation(self):
        data = {
            "anuncio_id": self.anuncio.id,
            "check_in": self.reserva.check_in,
            "check_out": self.reserva.check_out,
            "comentario": self.reserva.comentario,
            "qtd_hospedes": self.reserva.qtd_hospedes,
            "preco_total": 500,
        }
        url = "/reservas/%s/" % (self.reserva.codigo_reserva)
        response = self.client.patch(url, data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_reserva(self):
        url = "/reservas/%s/" % (self.reserva.codigo_reserva)
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
