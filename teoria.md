# Teoría Django

## ¿Qué es Django?

Es un framework escrito en python. Un framework es un marco de trabajo que nos dará un conjunto de herramientas, librerias, estructuras, que facilitan todo el proceso de trabajo.
Esto hace que el desarrollo sea más ágil, reutilizable y que esté bien estructurado.

## Patrón de arquitectura

MTV es una variante de MVC .

### MVC (model view controller - modelo vista controlador)

![Alt text](../django_openbootcamp/screenshots/image-1.png)

Se puede ver que le usuario realiza una petición a una URL, lo que hace el sistema es, acudir al diccionario de URLs donde asocia a cada URL con un controlador, el controlador, es el que sabe lo que tiene que realizar (contiene toda la parte lógica). El controlador debe trabajar con ciertos datos, estos datos los obtiene por medio de la comunicación con el modelo (abstracción de los datos que tenemos en la BD), este modelo, puede ser tratado como una clase, lo que permite que el modelo de arquitectura se abstraiga de la BD. El modelo está conectado a la base de datos e interactua con ella por medio de un ORM.El ORM (object relational mapping), es el encargado de reacionar todas las acciones con el modelo a acciones que se escriben/leen sobre la base de datos.
El controlador una vez que obtiene los datos, los pasa a la vista, quien es la encargada de tomar los datos y mostrar la información en la pantalla.

### MTV (model template view - modelo plantilla vista)

![Alt text](../django_openbootcamp/screenshots/image-2.png)

El controlador pasa a tener el nombre de "vista" y la vista pasa a tener el nombre de "plantilla".

## Estructura de archivos 

nombre_proyecto
   |__nombre_proyecto
   |   |__ __init__.py
   |   |__asgi.py
   |   |__settings.py
   |   |__urls.py
   |__manage.py

* manage.py: nos permite gestionar el proyecto
* asgi.py, wsgi.py: son archivos auxiliares
* urls.py: archivo en el que se encontrarán todas las URLs y su relación con las vistras que gestionan a las urls. En el se escriben todas las rutas y las vistas que las controlan.
* settings.py: permite establecer las configuraciones del paquete.

## Configuración DB y Rutas

Para crear la estructura de BD necesaria. Lo que hace Django es migrar los modelos de datos que tiene a nuestro sistema de permanencia de datos.

Debemos estar dentro del entorno de la estructura de archivos (carpeta general del proyecto).

```python
    python manage.py migrate
```

El comando debe ejecutarse cada vez que modifiquemos el modelo de datos. Esto permite que la estructura de datos tenga su backup/cobertura en la BD del sistema que tenemos trabajando por detrás.

Siempre que sea posible, por convención, debemos llamar a la vista igual que a la URL. Es decir, si yo tengo una vista "saludo", la URL en lo posible debe  llamarse "saludo/"

```python
    path("saludo/", vista.saludo)
```

## Rutas con parámetros

Las rutas con parámetros, lo que nos permite hacer, es crear rutas dinámicas y dejar de utilizar rutas estáticas como se encuentran declaradas por default en el archivo urls.py.

Un ejemplo puede ser:
```python
    path('adulto/<int:edad>/<int:altura>')
    """En este caso, se quiere llamar a la función 'adulto' y pasarle como parámetro la edad de una persona, para saber si la misma es o no mayor de edad.
    Todo parámetro que se va a recibir, debe estar escrito entre los sigonos mayor (>) y menor (<) y debe contener el tipo de dato del valor que se va a recibir. Se pueden agregar tantos parámetros como se necesiten por medio del uso de la barra (/)"""
```

##  Uso de Plantillas / Templates

Para retornar información, dejamos de utilizar HttpResponse, pasamos a devolver un template encargado de mostrar la información al usuario. 

Las plantillas no son más que un código de texto aislado dentro de un archivo, el cual tendrá extensión ".html". Las plantillas contendrán la parte visual de nuestro proyecto, permiten separar la parte visual de la parte lógica del proyecto.

Son útiles debido a que no solo hacen la separación mencionada anteriormente, si no que también nos permiten estructurar todo para no tener código HTML repetido.

* separar visual de lógico
* permite estructurar mejor el código
* podemos modularizar mucho mejor el contenido.

El lugar desde el cual se van a cargar los archivos HTML, se configura en el archivo 'settings.py', en el apartado llamado 'TEMPLATES'. Dentro de este apartado, podemos encontrar una lista con el nombre 'DIRS', dentro de ella, debemos poner el/los directorio/s donde se alamcenarán los archivos HTML para que cuando los necesite, sepa donde debe ir a buscarlos.

Para mostrar templates y manejar archivos, se utiliza la funcionalidad de django 'render'

```python
   from django.shortcuts import render

   render(request, template_name, context)
   """render necesita 3 parámetros: el request para no romper el ciclo y saber que información se pidió; el nombre del template que se quiere mostrar y el contexto, ya que no siempre trabajaremos con archivos estáticos"""
```
render(request, 'simple.html',{})
* el request es lo que generalmente recibimos como parámetro en la función definida en el archivo views.py.
* como tenemos configurado que los templates van a buscarse dentro del directorio 'templates', no debemos poner nada más que el nombre del archivo html. En caso de que fuese más complejo, debemos poner la ruta completa. Ej: simple.html se encuentra dentro de la carpeta 'vistas', la cual está en la carpeta 'templates', la ruta nos quedaría 'vistas/simple.html'
* el contexto es un diccionario, en este caso lo pasamos vacío porque el archivo html no requiere ninguna info para mostrar lo que contiene.

## Contexto en plantillas (contenido dinámico)

Para pasar contexto, lo que podemos hacer para que quede más limpio, es crear una variable llamada 'context',la cual será un diccionario (tiene elementos de tipo clave, valor), en el cual se encontraran los datos que debe mostrar el html.

Para en el html poder indicar lo que se quiere mostrar, debemos poner el nombre de la clave dentro de dobles llaves ('{{}}')

Dentro de la variable contexto podemos pasar también objetos, lo cual luego nos permite interactuar con sus métodos dentro del html

```python
   def dinamico(request, name):
      context = {'name': name}
       return render(request, 'dinamico.html', context)
```
```html
   <h1>Hola {{name}}</h1> 
   <!-- lo que hace en este caso, es mostrar el valor contenido dentro de la clave 'name' del diccionario que fue pasado por parámeto -->
```

## Bucles y condicionales en plantillas

No debemos delegar acciones de visualización a nuestras vistas y tampoco acciones de lógica a nuestras plantillas, debido a que estariamos rompiendo con lo que propone django y el código sería más desordenado.

* visualización -> template
* logica -> vistas

Para poder recorrer estructuras dentro de la plantilla y así mostar toda la información dinámicamente, lo que debemos hacer, dentro del archivo html, es utilizar {% %}, eso es lo que nos permite poner bucles y condicionales.

Por lo tanto para mostrar información de un array en la plantilla, el código sería:

```python
   def dinamico(request, name):
      categories = ['code', 'design', 'marketing', 'CEO', 'manager']
      context = {'name': name, 'categories': categories}
      return render(request, 'dinamico.html', context)
```
```html
   <body>
    <h1>Hola {{name}}</h1>
    <h3>Categories</h3>
    <ul>
        {% for category in categories %}
            {% if category == 'code' %}
                <li><b>{{category}}</b></li>
            {% else %}
                <li>{{category}}</li>
            {% endif %}
        {% endfor %}
    </ul>
   </body>
```

## Comentarios y filtros

La forma de escribir un comentario dentro de un archivo HTML en django que no se vea a la hora de inspeccionar el código en la web, se utilizan llaves y numerales 
```django
    {# Este es un comentario de una sola líena #}

    {% comment %}
        hola buenas tardes, soy un comentario de múltiples líneas en django
    {% endcomment %}
```

Los filtros nos sirven para acceder a ciertas funcionalidades/módulos. Para utilizar un filtro, simplemente ponemos un pipe ('|'). Los filtros pueden anidarse según necesidades.

```python
    <h5>Total de ctegorías: {{categories|length}}</h5>
    """En este caso, se está imprimeiendo la longitud de la lista de categorías en pantalla"""
    <h5>Total de ctegorías: {{categories|filtro1|filtro2}}</h5>
```

## Archivos estáticos

Permite enriquecer el contenido utilizando imagenes, archivos css o archivos javascript.
La importación de los archivos estáticos se realiza por medio del archivo settings.py, en el apartado donde se encuentra la constante llamada 'STATIC_URL'.
Se debe crear en el directorio raíz del proyecto, una carpeta de nombre 'static', la cual será la ruta default donde se irán a buscar los archivos estáticos.

En el archivo HTML se indica que se cargarán archivos estáticos, antes de la etiqueta DOCTYPE que marca el inicio de la estructura HTML.

```python
    {% load static %}
    """Está linea de código que se pone al inicio del arhivo HTML indica que el mismo va a necesitar cargar archivos estáticos para poder trabajar"""
    <!DOCTYPE html>
    ...
```

No se deben utilizar imports como lo hacemos cuando trabajamos únicamente con HTML, CSS y JS de forma convencional.

El archivo CSS debe ser importado en el HTML de la siguiente forma:
```html
    <head>
        ...
        <link rel="stylesheet" href="{% static 'style.css' %}">
    </head>
```

Para que todo termine de funcionar correctamente, dentro del archivo 'settings.py', debemos poner debajo de la constente 'STATIC_URL', lo siguiente:
```python
    STATICFILES_DIRS = [
        BASE_DIR/"static", 
        'var/www/static'
    ]
```
Básicamente es un array en donde vamos a indicar dónde se encuentran los archivos que vamos a necesitar utilizar. También con la línea 'var/www/static' vamos a dejar todo preparado para el momento en el que hagamos un deploy.

La ruta que indicamos como estática, iniciará dentro del directorio raíz 'static'.

## Herencia de plantillas

herramienta que permite no solo modularizar la estructura del codigo HTMl, si no que tambien permite evitar la reutilizacion de codigo. permitiendo que no haya duplicidad de etiquetas o estructuras en el codigo.

Cuando declaramos una plantilla, podemos indicar que hereda de una plantilla padre, cierta estructura. Podemos generar un layout general del contenido y posteriormente las nuevas plantillas, deberan extender el contenido del layout y ademas especifique el detalle de cada uno de los elementos y particularidades que no comparte con el resto de las plantillas.

Para eso, creamos un nuevo directorio dentro de la carpeta 'templates', la cual generalmente recibe el nombre de 'layout' y dentro se debe crear una plantilla, la cual debera contener todas las partes comunes que van a compartir el resto de las plantillas que heredaran de ella.

Debemos indicar en la plantilla HTML padre que parte de ella sera extensible, es decir, que parte podra ser modificada por las plantillas hijas. Esto lo hacemos utilizando un bloque, el cual se declara de la siguiente forma: 

```python
 ... #parte del contenido HTML
 <main>
    """main es la etiqueta que va a modificar cada pagina"""
    {%block nombre_bloque%} {% endblock %}
 </main>
 ... #parte del contenido HTML
```

Esto tambien puede utilziarse para que cada pagina tenga su propio archivo CSS.

Para hacer que las paginas hijas extiendan de la pagina padre, lo que debemos hacer, al inicio, es declarar el bloque: 
```python
    {% extends "./layout/base.html" %}
```

En las plantillas hijas no es necesario rellenar todos los bloques de contenido de la plantilla padre, es decir si solamente necesito rellenar el bloque de contenido, pero no el de scripts, relleno solamente el de contenido, eso no genera ningun tipo de problemas.

Para completar un bloque en llas plantillas hijas, lo que se debe hacer es declarar el bloque, junto con el contenido que quiero insertar en el mismo:

```python
    """En este caso, solamente estoy rellenando los bloqes de 'title' y 'content'"""
    {% block title %} Herencia {% endblock %}

    {% block content %}
        <h1>Herencia</h1>
    {% endblock  %}
```