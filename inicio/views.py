from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from  inicio.models import Animal


def mi_vista(request):
    print('Pase por aca!!! REY') #sale en la terminal, en el momento en que se ejecute
    return HttpResponse('<h1>Mi Primera Vista</h1>')

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
    archivo = open(r'C:\Users\sandolcetti\Documents\Coder House\Python\Clases\Clase 17\Proyecto_Django\templates\mi_primer_templates.html', 'r')
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
    
    template = loader.get_template(r'mostrar_fecha.html')
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
    
    template = loader.get_template(r'prueba_template.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)
    # una vez que generamos la funcion, falta generar la URL


def crear_animal (request):
    
    animal = Animal (nombre = 'Ricardito', edad = 3)
    print(animal.nombre)
    print(animal.edad) # para que se vea por la terminal
    animal.save() # cumple la misma funcion que el save de la terminal
    datos ={'animal':animal} #en la llave de ese contexto vaya ese animal
    template = loader.get_template(r'crear_animal.html')
    template_renderizado = template.render(datos)
    return HttpResponse(template_renderizado)