# Snippet API REST

Proyecto para prueba técnica de Snippet, el cual es una API REST realizada con Python,
Django y Django Rest Framework.

# Enfoque Utilizado

El proyecto se ha realizado utilizando una adaptación de "Clean Architecture", donde se separa
la lógica de negocio de la lógica de presentación, esto se ve reflejado de la siguiente forma:

- views => Vistas, Recepción de las peticiones, se aboca solo al trabajo de la petición y la respuesta. 
Invoca a los casos de uso.
- use cases => Casos de uso, se aboca a la lógica de negocio y los serializers, es aquí donde se aplican
las modificaciones a la data que no requieran interacción directa con la base de datos. Invoca a los repositorios.
- repositories => Repositorios, se aboca a la base de datos. Se encarga de realizar las respectivas consultas a
la base de datos, sea haciendo uso de la ORM o de consultas personalizadas, pero jamás modifica la data in situ.

Esta arquitectura permite el reconocimiento de los errores y la corrección de los mismos en la capa que corresponde
de manera directa, ahora, así se ha planteado para este proyecto, pero puede ser mejorable dependiendo del objetivo
(véase el uso de las clases, encapsulación, etc).

Se ha hecho uso de gitflow para el manejo de versiones, para que sea más fácil mantener el proyecto.

El proyecto está completamente realizado en inglés a excepción de este archivo con el
objetivo de una mayor comprensión de lo aquí explicado y del nombre de los
atributos de las tablas dado la documentación entregada, esto debido a que se asume que
dicha documentación puede haber sido planteada de esa manera para ser consumida de otro lugar
o directamente esta se espera en español, cabe mencionar que bajo normalidad estos atributos
también serían en inglés. Así mismo se intenta modificar las tablas lo menos posible en donde
el único cambio hecho es una añadidura del atributo "eliminado" en la tabla "book",
este atributo es añadido con el fin de "eliminar" el libro sin que este sea realmente eliminado
de la base de datos y de esta manera evitar la pérdida de información de los datos previos a su
eliminación (véase que los préstamos pierdan la respectiva referencia a este libro), por lo tanto,
bajo este atributo es que se discrimina si interactuar o no con estos libros en las distintas acciones
del backend.

Se ha utilizado get_or_create junto a 3 atributos distintivos para evitar la creación de un libro
que ya existe en la base de datos, esto es con el fin de mantener la restricción dada en la documentación.
Esta medida no se ha implementado, pero si se llega a añadir/crear un libro que haya sido eliminado
(atributo "eliminado" = True), se puede implementar de manera sencilla que en vez de generar conflicto, el libro vuelva 
a estar activo, no se ha llevado a cabo dado que esto implica decisiones de negocio mayores (conservaría la misma id).
Así mismo se puede hacer uso de update_or_create para, dados los atributos distintivos, actualizar el resto, nuevamente 
esto, como los atributos distintivos, se encuentran sujetos a decisiones de negocio.

Se añade un seeder con el fin de facilitar las cosas, este llena la base de datos con los datos mínimos de inicio, 
funciona con el siguiente comando:
- python manage.py seed_database
Utilizando la flag --mode=clear para borrar la base de datos y volver a llenarla.
Utilizando la flag --mode=refresh para rellenarla siempre y cuando no encuentre ya el usuario default a crear.
Este comando se ha agregado con refresh en el docker-compose, por lo que al correr el comando de inicio del proyecto y
cada vez que se (re)inicie se aplicará este comando.

## IMPORTANTE
Para la creación de usuarios y de préstamos (No se ha implementado soporte en la API REST para estas entidades)
hacer uso del administrador de Django, para ingresar entrar a la url localhost:8000/admin/ y autenticarse con los siguientes datos:
- username: admin
- password: admin  


## Entorno

Para las variables de entorno duplicar los archivos ".env.example" y ".env.db.example", eliminar ".example" y reemplazar
las variables de entorno, vienen unas por defecto que se han utilizado para el desarrollo de este proyecto, pero es
totalmente factible elegir unas propias.

## JSON Postman

Se añade el siguiente link con el JSON de Postman que contiene la colección de endpoints
de este proyecto (Importar en Postman).

- https://www.getpostman.com/collections/cb1e223c76a1b242b88b

## Comandos Disponibles

### Build

- `docker-compose build` para realizar el build o rebuild de los servicios.

### Correr la app en local

Usar `docker-compose up` para builds, (re)crear, iniciar, los servicios.
Entonces este será accesible desde [http://localhost:8000](http://localhost:8000)
en tu explorador favorito.

## Tecnologías involucradas

- Docker
- Python
- Django
- PostgreSQL
- Django Rest Framework

## Comandos útiles de Django

- Create superuser
    - python manage.py createsuperuser
- Create a new app:
    - django-admin startapp user
- Create a migration
    - python manage.py makemigrations
- Migrate
    - python manage.py migrate
- Migrate Through Docker
    - sudo docker-compose run --rm django sh -c "python manage.py migrate"
