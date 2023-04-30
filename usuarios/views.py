from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import redirect

from usuarios.forms import MiFormularioDeCreacion

# Create your views here.
# Todo lo referente a Seguridad en Django es "Contrib"

# El orden de los from es:
    # 1ro python
    # 2do framework
    # 3ro nuestro archivo

# el django_login es un alias sobre el login que importamos de django. Ya que sino se estan pisando con nuestra funcion def... O podes cambiar el nombre a la funcion o lo que hicimos que es darle un alias a lo importado.


def login(request):
    
    if request.method == 'POST':
        formulario =AuthenticationForm(request, data=request.POST)
        # Para un AuthenticationForm debemos pasar siempre un request aparte y despues una data
        
        if formulario.is_valid():
            # Vamos a consultar cual es el usuario
            nombre_usuario = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario, password = contraseña)
            # Esto nos permite obtener el usuario que estan en nuestra app y que tenga el usuario y la contra
            django_login(request, usuario)
            
            return redirect('inicio:inicio')
        
        else:
            return render(request,'usuarios/login.html', {'formulario': formulario})
            
    
    formulario = AuthenticationForm()
    #  AuthenticationForm, es un formulario predeterminado por django
    return render(request,'usuarios/login.html', {'formulario': formulario})


def registro(request):
    
    if request.method == "POST":
        # formulario =UserCreationForm(request.POST)
        formulario =MiFormularioDeCreacion(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
        else:
            return render(request, 'usuarios/registro.html',{'formulario':formulario})
        
    # formulario =UserCreationForm()
    formulario =MiFormularioDeCreacion()
    return render(request, 'usuarios/registro.html', {'formulario':formulario})