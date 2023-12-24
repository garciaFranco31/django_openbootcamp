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