import os, django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from imovel_app.models import Imovel
from anuncios_app.models import Anuncio
import uuid

plataformas = ["airbnb", "hoteis.com", "booking.com"]


def create_db(qtd_imoveis):
    for _ in range(qtd_imoveis):
        hospedes = random.randint(1, 10)
        banheiros = random.randint(1, 5)
        pet_friendly = bool(random.getrandbits(1))
        limpeza = round(random.uniform(50, 150), 2)
        i = Imovel(
            limite_de_hospedes=hospedes,
            banheiros=banheiros,
            pet_friendly=pet_friendly,
            limpeza=limpeza,
        )
        i.save()
        for _ in range(random.randint(3, 5)):
            plataforma = random.choice(plataformas)
            taxa = round(random.uniform(50, 300), 2)
            a = Anuncio(imovel=i, plataforma=plataforma, taxa_plataforma=taxa)
            a.save()


create_db(50)
print("Criado")
