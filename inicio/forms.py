# Creamos los formularios
from django import forms


class BaseAnimalFormulario(forms.Form):
    nombre = forms.CharField (max_length=20) 
    edad =  forms.IntegerField()
    cant_dientes = forms.IntegerField(required=False)

class CreacionAnimalFormulario(forms.Form):
    ...
class ModificarAnimalFormulario(forms.Form):
    ...

class BuscarAnimal(forms.Form):
    nombre = forms.CharField (max_length=20, required=False) 
    # edad =  forms.IntegerField()