from django.urls import path
# from django_clase_18.views import mi_vista, mostrar_fecha
# otra forma de pedir eso:
from inicio import views

app_name = 'inicio'

# patrones de URL
urlpatterns = [ 
    # path('',mi_vista),
    path ('', views.mi_vista, name = 'inicio'),
    # Pero al hacer eso tambien tenemos que modificar los path
    # path('mostrar-fecha/', mostrar_fecha),
    
    # paty('nombre de como llamamos a la funcion en la pagina', views.'nombre de la funcion')
    path('mostrar-fecha/', views.mostrar_fecha, name = 'mostrar_fecha'),
    path('saludar/<str:nombre>/<str:apellido>', views.saludar, name = 'saludar'),
    path('mi-primer-template/', views.mi_primer_template, name = 'mi_primer_template'),
    path('prueba-template/', views.prueba_template, name = 'prueba_template'),
    path('prueba-render/',views.prueba_render, name = 'prueba_render'),
    
    # Animales con vistas
    # path('animales/',views.lista_animales, name = 'listar_animales'),
    # path('animales/crear/',views.crear_animal, name = 'crear_animal'),
    # path('animales/<int:id_animal>/eliminar/',views.eliminar_animal, name = 'eliminar_animal'),
    # path('animales/<int:id_animal>/modificar/',views.modificar_animal, name = 'modificar_animal'),
    # path('animales/<int:id_animal>/',views.mostrar_animal, name = 'mostrar_animal'),
    
    # Animales con CBV
    path('animales/',views.ListaAnimales.as_view(), name = 'listar_animales'),
    path('animales/crear/',views.CrearAnimal.as_view(), name = 'crear_animal'),
    path('animales/<int:pk>/',views.MostrarAnimal.as_view(), name = 'mostrar_animal'),
    path('animales/<int:pk>/eliminar/',views.EliminarAnimal.as_view(), name = 'eliminar_animal'),
    path('animales/<int:pk>/modificar/',views.ModificarAnimal.as_view(), name = 'modificar_animal'),
    # "PK" es el identificador, ya que la clase basa en vista no va a entender nuestro id_animal
]
