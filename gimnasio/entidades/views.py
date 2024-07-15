from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
#los mixines trabajando sobre las clases
from django.contrib.auth.decorators import login_required
#los decoradores trabajando sobre las funciones

# Creando mi web de gimnasio.
def home(request):
    return render(request, "entidades/index.html")

def trainer(request):
    return render(request, "entidades/trainer.html")

def why(request):
    return render(request, "entidades/why.html")

def acerca(request):
    return render(request, "entidades/acerca.html")

@login_required
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
#____ Entrenadores
@login_required
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

#____ Membresias
@login_required
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
#___ Clientes

@login_required
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

#### BUSCAR #### Solo hecho para la clase clientes.
@login_required
def buscar_clientes(request):
    return render(request, "entidades/buscar_clientes.html")

@login_required
def encontrar_clientes(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clientes = Clientes.objects.filter(apellido__icontains=patron)
        contexto ={'clientes': clientes}
    else:
        contexto = {'clientes': Clientes.objects.all()}
        
    return render(request, "entidades/clientes.html", contexto)

### CREACION DE CRUDs
@login_required
def clientesUpdate(request, id_clientes):
    clientes = Clientes.objects.get(id=id_clientes)
    if request.method == "POST":
        mi_form = clientes_form(request.POST)
        if mi_form.is_valid():
            clientes.nombre = mi_form.cleaned_data.get("nombre")
            clientes.apellido = mi_form.cleaned_data.get("apellido")
            clientes.dni = mi_form.cleaned_data.get("dni")
            clientes.email = mi_form.cleaned_data.get("email")
            clientes.telefono = mi_form.cleaned_data.get("telefono")
            clientes.save()
            contexto = {"clientes": Clientes.objects.all() }
            return render(request, "entidades/clientes.html", contexto)
    else:
        mi_form = clientes_form(initial={"nombre": clientes.nombre, "apellido": clientes.apellido, "dni": clientes.dni, "email": clientes.email, "telefono": clientes.telefono})
    
    return render (request, "entidades/clientes_form.html", {"form": mi_form})

@login_required
def clientesDelete(request, id_clientes):
    clientes = Clientes.objects.get(id=id_clientes)
    clientes.delete()
    contexto = {"clientes": Clientes.objects.all() }
    return render(request, "entidades/clientes.html", contexto)

##classs based view

class membresias_list(LoginRequiredMixin, ListView):
    model = Membresias
    
class membresias_create(LoginRequiredMixin, CreateView):
    model = Membresias
    fields = ["nombre", "precio"]
    success_url = reverse_lazy("membresias")
    
class membresias_update(LoginRequiredMixin, UpdateView):
    model = Membresias
    fields = ["nombre", "precio"]
    success_url = reverse_lazy("membresias")
    
class membresias_delete(LoginRequiredMixin, DeleteView):
    model = Membresias
    success_url = reverse_lazy("membresias")

#### CBV seccion entrenadores
class entrenadores_list(LoginRequiredMixin, ListView):
    model = Entrenadores
    
class entrenadores_create(LoginRequiredMixin, CreateView):
    model = Entrenadores
    fields = ["nombre", "apellido"]
    success_url = reverse_lazy("entrenadores")
    
class entrenadores_update(LoginRequiredMixin, UpdateView):
    model = Entrenadores
    fields = ["nombre", "apellido"]
    success_url = reverse_lazy("entrenadores")
    
class entrenadores_delete(LoginRequiredMixin, DeleteView):
    model = Entrenadores
    success_url = reverse_lazy("entrenadores")

##### log in log out registracion
def loginRequest(request):
    if request.method == "POST": # si es la primera vez que ingresamos el mtogo va a ser get, sino post.
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #buscar avatar
            try: 
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            ######
            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
        
    return render(request, "entidades/login.html", {"form": miForm})


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()     
        
    return render(request, "entidades/registro.html", {"form": miForm})

##### edicion de perfiles / avatar
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserChangeForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "entidades/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambiar_clave.html"
    success_url = reverse_lazy("home")
    
    
####AGREGANDO AVATAR
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)): #itero por todos los avatares viejos y los borro
                    avatarViejo[i].delete()
            ###### guardar avatar
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            #### enviar imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #############################
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})
        
            
    
    
        