# Teoría Django

## ¿Qué es Django?

Es un framework escrito en python. Un framework es un marco de trabajo que nos dará un conjunto de herramientas, librerias, estructuras, que facilitan todo el proceso de trabajo.
Esto hace que el desarrollo sea más ágil, reutilizable y que esté bien estructurado.

## Patrón de arquitectura MTV (model template view - modelo plantilla vista)

Es una variante de MVC (model view controller - modelo vista controlador).

### MVC

![Alt text](image-1.png)

Se puede ver que le usuario realiza una petición a una URL, lo que hace el sistema es, acudir al diccionario de URLs donde asocia a cada URL con un controlador, el controlador, es el que sabe lo que tiene que realizar (contiene toda la parte lógica). El controlador debe trabajar con ciertos datos, estos datos los obtiene por medio de la comunicación con el modelo (abstracción de los datos que tenemos en la BD), este modelo, puede ser tratado como una clase, lo que permite que el modelo de arquitectura se abstraiga de la BD. El modelo está conectado a la base de datos e interactua con ella por medio de un ORM.El ORM (object relational mapping), es el encargado de reacionar todas las acciones con el modelo a acciones que se escriben/leen sobre la base de datos.
El controlador una vez que obtiene los datos, los pasa a la vista, quien es la encargada de tomar los datos y mostrar la información en la pantalla.

### MTV

![Alt text](image-2.png)

El controlador pasa a tener el nombre de "vista" y la vista pasa a tener el nombre de "plantilla".
