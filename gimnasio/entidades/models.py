from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    sabor = models.CharField(max_length=50)
    presentacion = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidades = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Entrenadores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
    class Meta:
        verbose_name = "Entrenador"
        verbose_name_plural = "Entrenadores"
        ordering = ["-apellido", "nombre",]
        
class Membresias(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField()
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} , {self.apellido}"
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre", "apellido", "dni", "email", "telefono"]
    
