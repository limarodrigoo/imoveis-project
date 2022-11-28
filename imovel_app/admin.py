from django.contrib import admin

from imovel_app.models import Imovel


class Imoveis(admin.ModelAdmin):
    list_display = (
        "id",
        "limite_de_hospedes",
        "banheiros",
        "pet_friendly",
        "limpeza",
        "data_ativacao",
        "criacao",
        "atualizacao",
    )
    list_display_links = (
        "limite_de_hospedes",
        "banheiros",
        "limpeza",
        "pet_friendly",
        "atualizacao",
    )
    list_per_page: 10
    search_fields = ("id",)


admin.site.register(Imovel, Imoveis)
