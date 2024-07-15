from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class entrenadores_form(forms.Form):
    nombre = forms.CharField(max_length=50, required =True) #se pone required porse ese dato es obligatorio
    apellido = forms.CharField(max_length=50, required =True)
    
class membresias_form(forms.Form):
    nombre = forms.CharField(max_length=50, required =True) #se pone required porse ese dato es obligatorio
    precio = forms.CharField(max_length=50, required =True)   
    
class clientes_form(forms.Form):
    nombre = forms.CharField(max_length=50, required =True)
    apellido = forms.CharField(max_length=50, required =True)
    dni = forms.IntegerField(required =True)
    email = forms.EmailField(required =True)
    telefono = forms.IntegerField(required =True)
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required =True)
    first_name = forms.CharField(label="Nombre", max_length=50, required =True)
    last_name = forms.CharField(label="Apellido", max_length=50, required =True)
    
    class Meta:
        model = User # va a usar el modelo User
        fields = ["email", "first_name", "last_name"] # aca se pone lo que se puede cambiar
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    
    