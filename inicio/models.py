from django.db import models

# Create your models here.

# Models es una funcionalidad que viene con django

class Animal(models.Model): # al ponele models.Model, le estamos diciendo a los atribujos que hereden ciertas caracteristicas.
    # Atributos
    nombre = models.CharField (max_length=20) # aca decis que "nombre" va a ser un "campo de caracteres", siempre pasarle el maximo caracteres que va a tener
    edad =  models.IntegerField() # edad es una campo de numeros enteros. A este no va a ser necesario que le pasemos un valor.

    def __str__(self):
        return f'Soy {self.nombre}, tengo {self.edad}'

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField () # que sea del tipo fecha
    def __str__(self):
        return f'Soy {self.nombre}, {self.apellido}'