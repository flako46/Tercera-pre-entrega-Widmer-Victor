from django.shortcuts import render
from .models import *
from .forms import *


# Creando mi web de gimnasio.
def home(request):
    return render(request, "entidades/index.html")

def trainer(request):
    return render(request, "entidades/trainer.html")

def why(request):
    return render(request, "entidades/why.html")

def clientes(request):
    contexto = {"clientes": Clientes.objects.all()}
    return render(request, "entidades/clientes.html", contexto)

def contact(request):
    return render(request, "entidades/contact.html")

def suplementos(request):
    contexto = {"suplementos": Producto.objects.all()}
    return render(request, "entidades/suplementos.html", contexto)

def entrenadores(request):
    contexto = {"entrenadores": Entrenadores.objects.all()}
    return render(request, "entidades/entrenadores.html", contexto)

def membresias(request):
    contexto = {"membresias": Membresias.objects.all()}
    return render(request, "entidades/membresias.html", contexto)

# ____ Formularios
def entrenadores_forms(request):
    if request.method == "POST": #pregunto si ya vienen los datos cargados
        mi_form = entrenadores_form(request.POST)
        if mi_form.is_valid():
            entrenadores_nombre = mi_form.cleaned_data.get("nombre")
            entrenadores_apellido = mi_form.cleaned_data.get("apellido")
            entrenador = Entrenadores(nombre=entrenadores_nombre, apellido=entrenadores_apellido)
            entrenador.save()
            contexto = {"entrenadores": Entrenadores.objects.all() }
            return render(request, "entidades/entrenadores.html", contexto)
          
         
            
    else: #creo un formulario vacio aca
        mi_form = entrenadores_form()
        
    return render(request, "entidades/entrenadores_form.html", {"form": mi_form})

###########
def membresias_forms(request):
    if request.method == "POST": #pregunto si ya vienen los datos cargados
        mi_form = membresias_form(request.POST)
        if mi_form.is_valid():
            membresias_nombre = mi_form.cleaned_data.get("nombre")
            membresias_precio = mi_form.cleaned_data.get("precio")
            membresia = Membresias(nombre=membresias_nombre, precio=membresias_precio)
            membresia.save()
            contexto = {"membresias": Membresias.objects.all() }
            return render(request, "entidades/membresias.html", contexto)
          
         
            
    else: #creo un formulario vacio aca
        mi_form = membresias_form()
        
    return render(request, "entidades/membresias_form.html", {"form": mi_form})
#########

def clientes_forms(request):
    if request.method == "POST": #pregunto si ya vienen los datos cargados
        mi_form = clientes_form(request.POST)
        if mi_form.is_valid():
            clientes_nombre = mi_form.cleaned_data.get("nombre")
            clientes_apellido = mi_form.cleaned_data.get("apellido")
            clientes_dni = mi_form.cleaned_data.get("dni")
            clientes_email = mi_form.cleaned_data.get("email")
            clientes_telefono = mi_form.cleaned_data.get("telefono")
            cliente = Clientes(nombre=clientes_nombre, apellido=clientes_apellido, dni=clientes_dni, email=clientes_email, telefono=clientes_telefono)
            cliente.save()
            contexto = {"clientes": Clientes.objects.all() }
            return render(request, "entidades/clientes.html", contexto)
          
         
            
    else: #creo un formulario vacio aca
        mi_form = clientes_form()
        
    return render(request, "entidades/clientes_form.html", {"form": mi_form})

#### BUSCAR
def buscar_clientes(request):
    return render(request, "entidades/buscar_clientes.html")

def encontrar_clientes(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clientes = Clientes.objects.filter(apellido__icontains=patron)
        contexto ={'clientes': clientes}
    else:
        contexto = {'clientes': Clientes.objects.all()}
        
    return render(request, "entidades/clientes.html", contexto)
     
        