"""django_clase_18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from django_clase_18.views import mi_vista, mostrar_fecha
# otra forma de pedir eso:
# from inicio import views

# patrones de URL
urlpatterns = [
    # path('',mi_vista),
    # path ('', views.mi_vista),
    # Pero al hacer eso tambien tenemos que modificar los path
    # path('mostrar-fecha/', mostrar_fecha),
    
    # paty('nombre de como llamamos a la funcion en la pagina', views.'nombre de la funcion')
    # path('mostrar-fecha/', views.mostrar_fecha),
    # path('saludar/<str:nobre>/<str:apellido>', views.saludar),
    # path('mi-primer-template/', views.mi_primer_template),
    # path('prueba-template/', views.prueba_template),
    
    
    # path("", include('inicio.urls')), # este path te redirige a las url de inicio.
    path('inicio/', include('inicio.urls')), # Basicamente condicionamos a la pagina para que cuando querramos ir a inicio, estemos obligados a colocarlo arriba.
    # http://127.0.0.1:8000/inicio/
    
    path('admin/', admin.site.urls),
]
