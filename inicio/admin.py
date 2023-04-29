from django.contrib import admin
from inicio.models import Animal, Persona

# Register your models here.

admin.site.register(Animal)
admin.site.register(Persona)

# Otra forma de hacerlo:
# admin.site.register([Animal,Persona])