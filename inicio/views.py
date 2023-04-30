from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Animal
from django.shortcuts import render, redirect
from inicio.forms import CreacionAnimalFormulario, BuscarAnimal, ModificarAnimalFormulario

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

def mi_vista(request):
    print('Pase por aca!!! REY') #sale en la terminal, en el momento en que se ejecute
    # return HttpResponse('<h1>Mi Primera Vista</h1>')
    return render(request,'inicio/index.html')

# def mostrar_fecha(request):
#     return HttpResponse(f'<p>{datetime.now()}</p>')

# Otra forma de hacerlo seria...
# def mostrar_fecha(request): # Esta es una version de mostrar fecha con HttpResponse.
#     dt = datetime.now()
#     dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
#     return HttpResponse(f'<p>{dt_formateado}</p>')

# def saludar(request):
#     return HttpResponse('<h1>Hola Richard</h1>')

def saludar(request, nombre, apellido):
    return HttpResponse(f'<h1>{nombre} {apellido}</h1>')

#Template
# creamos el html, le colocamos un titulo con una descripcion

# le decimos a nuestra vista que queresmos usar nuestro archivo
# Para copiarlo, click secundario sobre mi archivo .html > "copiar ruta de acceso" y lo pegamos despues del open. Ademas le agregamos un read para leerlo.
def mi_primer_template(request):
    # recordar tambien agregar la "r" adelante porque sino me va a tomar las \U como 
    archivo = open(r'C:\Users\sandolcetti\Documents\Coder House\Python\Clases\Clase 19\Django_Clase_19_Playground\templates\mi_primer_templates.html', 'r')
    # archivo = open(r'mostrar_fecha.html', 'r')
    
    # Convertimos nuestro archivo leido y lo transformamos en un template. 
    # Recordar llamarlo arriba de django.template import Template
    template = Template(archivo.read())
    
    # Cerramos el archivo
    archivo.close()
    
    # Solo queda generar un contexto.
    # Recordar llamarlo arriba de django.template import Template
    contexto = Context()
    # contexto es la informacion que vamos a ver en nuestro template
    
    # Ahora al template lo renderizamos y le pasamos un contexto
    template_renderizado = template.render(contexto)
    # Renderizar = plasmar, imprimir
    
    return HttpResponse(template_renderizado)

# Version con template
# El beneficio que tiene esto es la facilidad, ya que podes crear todo desde el html
def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    # archivo = open(r'mostrar_fecha.html', 'r')
    # template = Template(archivo.read())
    # archivo.close()
    # contexto = Context({'fecha': dt_formateado})
    # template_renderizado = template.render(contexto)
    # return HttpResponse(template_renderizado)
    
    
    # De esta forma nos ahorramos todas las lineas de arriba
    
    template = loader.get_template(r'inicio/mostrar_fecha.html')
    # datos = {'fecha': dt_formateado} # esta es una forma tambien de colocar el diccionario
    # template_renderizado = template.render({datos})
    template_renderizado = template.render({'fecha': dt_formateado}) # a este render no le pasamos el contexto sino el diccionario.
    
    return HttpResponse(template_renderizado)
    

# Otra version pero mas corta

def prueba_template(request):
    
    datos = {
        'nombre':'Pepito',
        'apellido':'Grullo',
        'edad': 10,
        'años': [
            1995,2004, 2014, 2017, 2021, 2022
        ]
        
    }
    
    template = loader.get_template(r'inicio/prueba_template.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)
    # una vez que generamos la funcion, falta generar la URL

#  Versión 1 de Crear Animal
# def crear_animal (request):
    
#     animal = Animal (nombre = 'Ricardito', edad = 3)
#     print(animal.nombre)
#     print(animal.edad) # para que se vea por la terminal
#     animal.save() # cumple la misma funcion que el save de la terminal
    
    
    
#     datos ={'animal':animal} #en la llave de ese contexto vaya ese animal
#     template = loader.get_template(r'inicio/crear_animal.html')
#     template_renderizado = template.render(datos)
#     return HttpResponse(template_renderizado)

# Versión 2 de Crear Animal
# def crear_animal(request):
#     if request.method == "POST":
#         animal = Animal (nombre = request.POST['nombre'], edad = request.POST['edad'])
#         animal.save()
#     return render(request, 'inicio/crear_animal_v2.html')
        
    # print(type(request))
    # print(type(request.POST))
    # print(request.POST)

def prueba_render(request):
    datos = {'nombre':'Pepe'}
    # template = loader.get_template(r'prueba_render.html')
    # template_renderizado = template.render(datos)
    # return HttpResponse(template_renderizado)

    return render(request, r'inicio/prueba_render.html', datos) # el no pasarle el dicc datos no me va a aparecer "pepe"

# Version 3 de Crear Animal

def crear_animal(request):
    if request.method == "POST":
        formulario = CreacionAnimalFormulario(request.POST)
        
        if formulario.is_valid():
        # limita al usuario a colocar cosas que estan malas como en la edad
            datos_correctos = formulario.cleaned_data
            
            
            animal = Animal (nombre = datos_correctos['nombre'], edad = datos_correctos['edad'])
            animal.save()

            return redirect('inicio:listar_animales')
            
    formulario = CreacionAnimalFormulario()
    return render(request, 'inicio/crear_animal_v3.html',{'formulario': formulario})


def lista_animales(request):
    nombre_a_buscar = request.GET.get('nombre',None)
    
    if nombre_a_buscar:
        # animales = Animal.objects.filter(nombre=nombre_a_buscar)
        animales = Animal.objects.filter(nombre__icontains = nombre_a_buscar)
        # icontains, me permite cuando filtro buscar por caracteres que contengan esa letra por ejemplo
    else:
        animales = Animal.objects.all()
    formulario_busqueda = BuscarAnimal()
    return render(request, 'inicio/lista_animales.html',{'animales':animales,'formulario':formulario_busqueda})


def eliminar_animal(request, id_animal):
    animal_a_eliminar = Animal.objects.get(id=id_animal)
    animal_a_eliminar.delete()
    return redirect('inicio:listar_animales')

def mostrar_animal(request, id_animal):
    animal_a_mostrar = Animal.objects.get(id=id_animal)
    return render(request, 'inicio/mostrar_animal.html',{'animal_a_mostrar':animal_a_mostrar})

def modificar_animal(request, id_animal):
    animal_a_modificar = Animal.objects.get(id=id_animal)
    
    if request.method == "POST":
        formulario = ModificarAnimalFormulario(request.POST)
        if formulario.is_valid():
            data_limpia = formulario.cleaned_data
            
            animal_a_modificar.nombre =data_limpia['nombre']
            animal_a_modificar.nombre =data_limpia['edad']
            animal_a_modificar.save()
            
            return redirect('inicio:listar_animales')
        else:
            return render(request,'inicio/modificar_animal.html', {'formulario': formulario, 'id_animal':id_animal})

    formulario = ModificarAnimalFormulario(initial={'nombre': animal_a_modificar.nombre, 'edad':animal_a_modificar.edad})
    return render(request,'inicio/modificar_animal.html', {'formulario': formulario, 'id_animal':id_animal})


# CBV para animales (Clase Basadas en Vistas)

class ListaAnimales(ListView):
    model = Animal
    template_name ='inicio/CBV/lista_animales.html'


class CrearAnimal(CreateView):
    model = Animal
    template_name = 'inicio/CBV/crear_animal_v3.html'
    success_url = '/inicio/animales/'
    fields = ['nombre', 'edad']
    # Si por esas casualidades no pasamos formularios entonces tenemos que...
    # form = le pasamos el formulario que queremos qe use 

class ModificarAnimal(UpdateView):
    model = Animal
    template_name = 'inicio/CBV/modificar_animal.html'
    success_url = '/inicio/animales/'
    fields = ['nombre', 'edad', 'cant_dientes']
    

class EliminarAnimal(DeleteView):
    model = Animal
    template_name ='inicio/CBV/eliminar_animal.html'
    success_url = '/inicio/animales/'
    

class MostrarAnimal(DetailView):
    model = Animal
    template_name = 'inicio/CBV/mostrar_animal.html'