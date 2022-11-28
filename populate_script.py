import os, django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from imovel_app.models import Imovel
from anuncios_app.models import Anuncio
from reservas_app.models import Reserva
from faker import Faker

plataformas = ["airbnb", "hoteis.com", "booking.com"]


def create_db(qtd_imoveis):
    Faker.seed(0)
    fake = Faker("pt-br")
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
            if bool(random.getrandbits(1)):
                random_month = random.randint(1, 12)
                random_day = random.randint(1, 21)
                random_plus_days = random.randint(1, 5)
                check_in = "2022-%d-%d" % (random_month, random_day)
                check_out = "2022-%d-%d" % (random_month, random_day + random_plus_days)
                preco_total = round(random.uniform(120, 999), 2)
                qtd_hospedes = random.randint(1, hospedes)
                r = Reserva(
                    anuncio_id=a,
                    check_in=check_in,
                    check_out=check_out,
                    preco_total=preco_total,
                    comentario=fake.catch_phrase(),
                    qtd_hospedes=qtd_hospedes,
                )
                r.save()


create_db(50)
print("Criado")
