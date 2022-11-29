from rest_framework.test import APITestCase
from django.urls import reverse
from imovel_app.models import Imovel
from rest_framework import status


class ImovelTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Imovéis-list")
        self.imovel1 = Imovel.objects.create(
            limite_de_hospedes=3, banheiros=1, pet_friendly=False, limpeza=32.2
        )
        self.imovel2 = Imovel.objects.create(
            limite_de_hospedes=6, banheiros=2, pet_friendly=True, limpeza=52.5
        )

    def test_list_imoveis(self):
        """Teste para verificar requisiçaõ GET imoveis"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_imovel(self):
        """Test para verificar requisitao POST imoveis"""
        data = {
            "limite_de_hospedes": 1,
            "banheiros": 1,
            "pet_friendly": False,
            "limpeza": 30,
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_create_wrong_imovel(self):
        data = {
            "limite_de_hospedes": "Teste",
            "banheiros": 2,
            "pet_friendly": False,
            "limpeza": 35,
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_imovel(self):
        data = {
            "limite_de_hospedes": 4,
            "pet_friendly": True,
        }
        response = self.client.patch("/imoveis/%d/" % (self.imovel1.id), data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_imovel(self):
        response = self.client.delete("/imoveis/%d/" % (self.imovel1.id))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
