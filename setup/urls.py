from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from imovel_app.views import ImoveisViewSet, ListaImoveisAnuncio
from anuncios_app.views import AnuncioViewSet
from reservas_app.views import ReservaViewSet

router = routers.DefaultRouter()
router.register("imoveis", ImoveisViewSet, basename="Imovéis")
router.register("anuncios", AnuncioViewSet, basename="Anuncios")
router.register("reservas", ReservaViewSet, basename="Reservas")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("imoveis/<int:pk>/anuncios/", ListaImoveisAnuncio.as_view()),
]
