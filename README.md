# Curso Django OpenBootcamp

## Entorno virtual
Para este curso, voy a estar utilizando el framework venv para gestionar el entorno virtual de desarrollo. 
Para crear un entorno virtual, se deben ejecutar desde la consola los siguientes comandos:
```python
    python -m venv nombre_proyecto
    """nombre_proyecto puede ser un directorio ya existe, ya que en caso de que el mismo exista, se crearan todas las carpetas necesarias dentro de dicho directorio. Pero si el directorio no existe, lo crea y le agrega todas las carpetas necesarias."""

    source nombre_proyecto/Scripts/activate 
    """Este comando lo que hace, es iniciar el entorno virtual, siempre que querramos trabajar con él, debemos iniciarlo primero, caso contrario no podremos utilizar los paquetes o frameworks que hayamos instalado dentro del mismo."""

    deactivate """Lo que hace este comando es desactivar el entorno virtual"""
```
## Instalación de Django

Para instalar Django, en mi caso lo primero que hago es activar el entorno virtual, para no ocupar espacio en la memoria de mi PC y que quede todo lo que voy a utilizar en este curso en un único lugar (el entorno virutal).
Para realizar la instalación de Django, se debe ejecutar desde la terminal el siguiente comando (El entorno vitual debe estar activado y debemos asegurarnos de que estamos trabajando dentro de él):

```python
    pip install django
    """Instala el framework Django"""
```

## Archivo ".gitignore"

Este archivo lo voy a utilizar para manejar los archivos y carpetas que no quiero que se pushen a github.
