from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def mi_vista(request):
    print('Pase por aca!!! REY') #sale en la terminal, en el momento en que se ejecute
    return HttpResponse('<h1>Mi Primera Vista</h1>')

# def mostrar_fecha(request):
#     return HttpResponse(f'<p>{datetime.now()}</p>')

# Otra forma de hacerlo seria...
def mostrar_fecha(request):
    dt = datetime.now()
    dt_formateado = dt.strftime("%A %d %B %Y %I:%M")
    return HttpResponse(f'<p>{dt_formateado}</p>')

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
