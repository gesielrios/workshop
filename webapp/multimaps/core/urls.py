from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mapa', views.mapa, name='mapa'),
    path('filtro', views.filtro_periodo, name='filtro'),
]
