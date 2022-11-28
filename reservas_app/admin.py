from django.contrib import admin

from reservas_app.models import Reserva


class Reservas(admin.ModelAdmin):
    list_display = (
        "codigo_reserva",
        "anuncio_id",
        "check_in",
        "check_out",
        "comentario",
        "qtd_hospedes",
        "preco_total",
    )
    list_display_links = (
        "check_in",
        "check_out",
        "comentario",
        "qtd_hospedes",
        "preco_total",
    )
    search_fields = ("codigo_reserva",)


admin.site.register(Reserva, Reservas)
