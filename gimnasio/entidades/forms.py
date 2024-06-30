from django import forms

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
    