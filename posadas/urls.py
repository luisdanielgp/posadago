from django.conf.urls import url
from django.contrib import admin
from .views import ListarPosadas

urlpatterns = [
    url(r'^posadas/$', ListarPosadas.as_view(), name="listarPosadas")
]
