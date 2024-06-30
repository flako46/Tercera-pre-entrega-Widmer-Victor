from django.urls import path
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('trainer/', trainer, name="trainer"),
    path('why/', why, name="why"),
    path('contact/', contact, name="contact"),
    path('suplementos/', suplementos, name="suplementos"),
    
    path('entrenadores/', entrenadores, name="entrenadores"),
    path('membresias/', membresias, name="membresias"),
    
    ####   FORMULARIOS
    path('entrenadores_form/', entrenadores_forms, name="entrenadores_form"),
    path('membresias_form/', membresias_forms, name="membresias_form"),
    path('clientes_form/', clientes_forms, name="clientes_form"),
    path('clientes/', clientes, name="clientes"),
    
    ##### BUSCAR
    path('buscar_clientes/',buscar_clientes, name="buscar_clientes"),
    path('encontrar_clientes/',encontrar_clientes, name="encontrar_clientes"),
]