from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    # con widget=forms.PasswordInput no va a dejar ver lo que escribimos, le indicamos que son campos de contraseña. Permite ponerle una mascara
    
    class Meta: # contiene la informacion que va a trabajar por detras
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:'' for k in fields} # existe la posibilidad de generar informacion listas, dicc, tuplas; todo esto basandose en un for y usando lo del for de manera que quede guardado
        # help text son todos los txt que nos aparecen como:
        # Your password can’t be too similar to your other personal information.
        # # Your password must contain at least 8 characters.
        # # Your password can’t be a commonly used password.
        # # Your password can’t be entirely numeric.