from django.contrib import admin
from django.urls import path
from rest_framework import routers
from imovel_app.views import ImoveisViewSet

router = routers.DefaultRouter()
router.register("imoveis", ImoveisViewSet, basename="Imovéis")

urlpatterns = [
    path("admin/", admin.site.urls),
]
