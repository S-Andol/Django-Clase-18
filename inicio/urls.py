from django.urls import path
# from django_clase_18.views import mi_vista, mostrar_fecha
# otra forma de pedir eso:
from inicio import views

# patrones de URL
urlpatterns = [ 
    # path('',mi_vista),
    path ('', views.mi_vista),
    # Pero al hacer eso tambien tenemos que modificar los path
    # path('mostrar-fecha/', mostrar_fecha),
    
    # paty('nombre de como llamamos a la funcion en la pagina', views.'nombre de la funcion')
    path('mostrar-fecha/', views.mostrar_fecha),
    path('saludar/<str:nobre>/<str:apellido>', views.saludar),
    path('mi-primer-template/', views.mi_primer_template),
    path('prueba-template/', views.prueba_template),
    path('crear-animal/',views.crear_animal),
    
]
