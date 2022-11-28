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
        self.assertEquals(Imovel.objects.count(), 2)

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
