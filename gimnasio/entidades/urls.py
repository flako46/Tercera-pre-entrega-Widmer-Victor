from django.urls import path
from entidades.views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('trainer/', trainer, name="trainer"),
    path('why/', why, name="why"),
    path('contact/', contact, name="contact"),
    path('suplementos/', suplementos, name="suplementos"),
    path('acerca/', acerca, name="acerca"),
    
    #### ENTRENADORES
    #path('entrenadores/', entrenadores, name="entrenadores"),
    path('entrenadores_form/', entrenadores_forms, name="entrenadores_form"),
    path('entrenadores/', entrenadores_list.as_view(), name="entrenadores"),
    path('entrenadores_create/', entrenadores_create.as_view(), name="entrenadores_create"),
    path('entrenadores_update/<int:pk>/', entrenadores_update.as_view(), name="entrenadores_update"),
    path('entrenadores_delete/<int:pk>/', entrenadores_delete.as_view(), name="entrenadores_delete"),
    
    #### MEMBRESIAS
    path('membresias_form/', membresias_forms, name="membresias_form"),
    path('membresias/', membresias_list.as_view(), name="membresias"),
    path('membresias_create/', membresias_create.as_view(), name="membresias_create"),
    path('membresias_update/<int:pk>/', membresias_update.as_view(), name="membresias_update"),
    path('membresias_delete/<int:pk>/', membresias_delete.as_view(), name="membresias_delete"),
    
    ##### CLIENTES
    path('clientes_form/', clientes_forms, name="clientes_form"),
    path('clientes/', clientes, name="clientes"),
    path('buscar_clientes/',buscar_clientes, name="buscar_clientes"),
    path('encontrar_clientes/',encontrar_clientes, name="encontrar_clientes"),
    path('clientesUpdate/<id_clientes>/', clientesUpdate, name="clientesUpdate"),
    path('clientesDelete/<id_clientes>/', clientesDelete, name="clientesDelete"),
    
    #### login logout   registracion
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),
    
    ####### editar perfil y AVATAR
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view() , name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
    
]