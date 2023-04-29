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
    path('saludar/<str:nobre>/<str:apellido>', views.saludar, name = 'saludar'),
    path('mi-primer-template/', views.mi_primer_template, name = 'mi_primer_template'),
    path('prueba-template/', views.prueba_template, name = 'prueba_template'),
    path('crear-animal/',views.crear_animal, name = 'crear_animal'),
    path('animales/',views.lista_animales, name = 'listar_animales'),
    path('prueba-render/',views.prueba_render, name = 'prueba_render'),
    
]
