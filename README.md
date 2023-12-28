# Curso Django OpenBootcamp

## Entorno virtual
Para este curso, voy a estar utilizando el framework venv para gestionar el entorno virtual de desarrollo. 
Para crear un entorno virtual, se deben ejecutar desde la consola los siguientes comandos:
```python

    #Instalar venv utilizando pip
    pip install venv

    #nombre_pryecto puede ser un directorio existente o no. En caso de que el directorio exista, se crean las carpetas 
    #necesarias dentro de ese directorio. En caso de que el directorio no exista, lo crea y dentro de él
    #crea todas las carpetas correspondientes a venv.
    python -m venv nombre_proyecto

    #Para poder iniciar el entorno virtual (debido a que si no lo hacemos, no podremos trabajar) con él
    #debemos ejecutar el comando:
    source nombre_proyecto/Scripts/activate 

    #Cuando querramos cerrar el entorno virtual, debemos ejecutar el comando:
    deactivate
```
## Instalación de Django

Para instalar Django, en mi caso lo primero que hago es activar el entorno virtual, para no ocupar espacio en la memoria de mi PC y que quede todo lo que voy a utilizar en este curso en un único lugar (el entorno virutal).
Para realizar la instalación de Django, se debe ejecutar desde la terminal el siguiente comando (El entorno vitual debe estar activado y debemos asegurarnos de que estamos trabajando dentro de él):

```python
    #Instalar Django
    pip install django
```

## Archivo ".gitignore"

Este archivo lo voy a utilizar para manejar los archivos y carpetas que no quiero que se pushen a github.

# Iniciando con Django

### Creación de un nuevo proyecto

Para crear un nuevo proyecto, lo que debemos hacer es posicionarnos en la carpeta en la que deseamos crear el nuevo proyecto y desde la terminal, ejecutar el comando

```python
    #Crear un nuevo proyecto django
    django-admin startproject nombre_proyecto
```

Esto lo que hace, es crear una carpeta con diferentes archivos .py y un archivo "manage.py". Todo esto tiene ya por default una estructura de proyecto.

### Ejecutar servidor

```python
    #Ejecutando este comando, inicializamos el servidor de trabajo. Debemos estar posicionados en la carpeta raíz del proyecto
    python manage.py runserver

    #Para detener/interrumpir el servidor se debe utilizar la combinación de teclas
   """ Ctrl + C""" 
```



