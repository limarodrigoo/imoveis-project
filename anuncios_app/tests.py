from rest_framework.test import APITestCase
from django.urls import reverse
from anuncios_app.models import Anuncio
from imovel_app.models import Imovel
from rest_framework import status


class AnuncioTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Anuncios-list")
        self.imovel = Imovel.objects.create(
            limite_de_hospedes=2,
            banheiros=1,
            pet_friendly=False,
            limpeza=30,
        )
        self.anuncio1 = Anuncio.objects.create(
            imovel=self.imovel, plataforma="airbnb", taxa_plataforma=59
        )
        self.anuncio2 = Anuncio.objects.create(
            imovel=self.imovel, plataforma="booking.com", taxa_plataforma=77
        )

    def test_list_anuncios(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_anuncios(self):
        data = {"imovel": self.imovel.id, "plataforma": "airbnb", "taxa_plataforma": 55}
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_wrong_post_anuncios(self):
        wrong_data = {
            "imovel": self.imovel.id,
            "plataforma": "airbnb",
            "taxa_plataforma": "não sei",
        }
        response = self.client.post(self.list_url, data=wrong_data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_anuncios(self):
        data = {"taxa_plataforma": 55}
        url = "/anuncios/%d/" % (self.anuncio1.id)
        response = self.client.patch(url, data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_anuncio(self):
        url = "/anuncios/%d/" % (self.anuncio1.id)
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
