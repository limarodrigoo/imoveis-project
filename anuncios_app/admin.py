from django.contrib import admin
from anuncios_app.models import Anuncio


class Anuncios(admin.ModelAdmin):
    list_display = (
        "id",
        "imovel",
        "plataforma",
        "taxa_plataforma",
        "criacao",
        "atualizacao",
    )
    list_display_links = (
        "plataforma",
        "taxa_plataforma",
        "atualizacao",
    )
    search_fields = ("id",)


admin.site.register(Anuncio, Anuncios)
