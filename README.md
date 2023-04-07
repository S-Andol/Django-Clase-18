# Django-Clase-18


http://127.0.0.1:8000/

# Vamos a generar un mostrar_fecha.html
primero comentamos la funcion anterior 
y comenzamos a generar una nueva funcion pero para trabajarla desde html
copiamos y pegamos lo mismo que tiene "mi_primer_templates" en "mostrar_fecha"


Generamos la función copiando parte del mostrar mostrar_fecha anterior y nos robamos tambien de la funcion mi_primer_templates

Pero solo la direccion en el "open"

Para que otra persona no tenga problemas a la hora de abrir el archivo vamos ir a "settings.py" y agregamos en la parte de "TEMPLATES" y modificamos:

'DIRS': [BASE_DIR/'templates'],

Vamos a views.py y comenzamos a trabajar:

archivo = open(r'mostrar_fecha.html', 'r')

contexto = Context({'fecha': dt_formateado})

# Cargamos un loader, lo importamos desde django.

from django.template import Template, Context, loader



# Podemos subdividir nuestro paquete en varios paquetitos, con funcionalidades y demas

python manage.py startapp inicio

<!-- Nos descarga una carpeta con ciertos datos -->

# Copiamos todo lo que tenemos en views.py
Lo pegamos en la nueva views.py que se genera dentro de "inicio"
RECORDAR
    Debemos cambiar en urls.py el llamado del 
    
    from django_clase_18 import views
    por el de:
    from inicio import views

Recordar volver a correr el servidor

python manage.py runserver

# Crear archivos urls para cada app
Es recomendable crear archivos con urls.py en cada app (como la de "inicio")

Copiamos el urls.py que ya tenemos armado y lo pegamos en el nuevo.

Eliminamos: 
<!--"""django_clase_18 URL Configuration

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
from django.contrib import admin-->
Y tambien eliminamos:
<!--path('admin/', admin.site.urls),-->

# Eliminamos inicio import views
Buscamos:
from inicio import views
en la carpeta de "django_clase_18" y lo eliminamos.


# Eliminamos todo lo que tiene urlpatterns
Vamos a urls.py de "django_clase_18" y eliminamos todo a excepcion de:
ELIMINADO:
path ('', views.mi_vista),
path('mostrar-fecha/', views.mostrar_fecha),
path('saludar/<str:nobre>/<str:apellido>', views.saludar),
path('mi-primer-template/', views.mi_primer_template),
path('prueba-template/', views.prueba_template),

DEJAMOS:
path('admin/', admin.site.urls),

Guardamos y probamos, nos da error.
# OJO
El programa si lo recargamos, nos da error.
Esto pasa porque el programa siempre va a buscar en el primer archivo creado de urls.
Hay que cambiarlo. 

debemos agregar en url de django_clase_18:

path("str","direccion de base")
path("", include('inicio.urls)) <!--Le agregamos el "include"para que use el archivo urls.py de la carpeta "inicio"-->

RECORDAR tambien agegarlo en el import
from django.urls import path,include


1:29:00

# Comenzamos a crear modelos
Los modelos son principalmente clases... por ahora

# Creamos las class
Ponemos todo lo que queresmos de las class

# Colocamos inicio en installed
Nos dirigimos a settings.py
Buscamos INSTALLED_APPS
Y le agregamos 'inicio'

Vemos que no pasa nada...
# Python manage.py makemigrations
Crea un archivo dentro de la carpeta 'migrations' y django hace un codigo donde las difentes Bases de Datos se entiendan para poder crear las tablas que hagamos como un 'modelo'

# Migracion de makemigrations
Ahora lo que queda es hacer un:
python manage.py runserver
Donde nos indica que falta migrar la migracion que hicimos en "migrations"

# hacemos la migracion
python manage.py migrate    

# Observamos db.sqlite3
Si miramos la bd, vemos que ya estan las tablas de "inicio_animal" e "inicio_persona"

# Resumen de estos pasos
Cada vez que trabajemos con los modelos, terminamos de hacer todos los cambios y hacemos un makemigrations para despues al final el migrate. Y listo


# CREAR INFORMACION en BD.
1° Creamos una nueva vista en views.py
2° Creamos un template que se llame "crear_animal.html"
3° Copiamos los datos de "mi_primer"templates", modificamos lo que queremos
4° Lanzo en consola pyhton manage.py runserver
Listo


# CTRL+C = SALIMOS/TUMBAMOS DEL SERVER

# Nos movemos a la terminal interna
python manage.py shell

# Creamos de otra forma un anumal.
1° Escribimos en consola: 
from inicio.models import Animal
" del archivo inicio archivo models importamos animal"

2° Le pasamos por consola la informacion que necesita: 
animal1 = Animal(nombre='perrito', edad = 4)

3° probamos varios comandos en consola para verificar.
animal1
"nos dice que es una consola"
animal1.nombre
"perrito"
animal1.edad
"4"

4° Guardar informacion en nuestra base de datos
animal1.save()

Colocamos otro ejemplo
animal2 = Animal(nombre= 'Elmer', edad = 15)
animal2
animal2.save()

Si revisamos el archivo db.sqlite3 vemos que estan ingresados los dos animales en inicio.animal
RECORDAR ACTUALIZAR LA BASE DE DATOS... ESTA EL SIMBOLO DENTRO DE LA BASE A LA IZQUIERDA SUPERIOR.

Para cerrar el shell
exit()

# Creamos un animal desde el archivos views.py

Como ya teniamos creada nuestra funcion:


def crear_animal (request):
    
    animal = Animal (nombre = 'Ricardito', edad = 3)
    print(animal.nombre)
    print(animal.edad) # para que se vea por la terminal
    animal.save() # cumple la misma funcion que el save de la terminal
    datos ={'animal':animal} #en la llave de ese contexto vaya ese animal
    template = loader.get_template(r'crear_animal.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)


Solo nos queda colocar arriba de todo:
from  inicio.models import Animal

# Creamos un parrafo en crear_animal.html
Vamos a html y le creamos un parrago con la funcion 

<p>{{animal.nombre}}{{animal.edad}}</p>