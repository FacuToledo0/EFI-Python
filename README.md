## EFI PYTHON PARTE II
Este proyecto tiene como objetivo crear una API sobre la base de los modelos de un proyecto que consiste en el desarrollo de una aplicación web para gestionar un local de venta de celulares. La API debe permitir: un login
y creación de usuarios, endpoints para obtener los objetos de todos los modelos (marca, modelo, proveedor, etc), endpoint para poder crear un objeto nuevo (limitado a usuarios admin), documentacion de los enpoints y al menos un modelo debe contener otro anidado.
La implementación se realiza usando Marshmallow para serialización y validación de datos.


## TECNOLOGÍAS UTILIZADAS:

- **Python**: Lenguaje de programación principal utilizado para desarrollar el proyecto.
- **Flask**: Framework ligero para el desarrollo de aplicaciones web.
- **Flask-SQLAlchemy**: ORM (Object Relational Mapper) que permite interactuar con la base de datos mediante objetos de Python en lugar de consultas SQL.
- **Flask-Migrate**: Herramienta que facilita la gestión de migraciones de bases de datos con `Alembic`, permitiendo realizar cambios estructurales sin pérdida de datos.
- **Flask-CORS**: Extensión que permite manejar solicitudes de diferentes orígenes (CORS).
- **Flask-JWT-Extended**: Extensión que facilita la implementación de autenticación y autorización mediante JSON Web Tokens (JWT).
- **Flask-Marshmallow**: Extensión utilizada para la serialización y validación de datos en la API.
- **Werkzeug**: Biblioteca que proporciona especialmente utilidades para manejar datos sensibles de forma segura, como el hash de contraseñas.
- **dotenv**: Permite cargar variables de entorno desde un archivo `.env` para configurar la aplicación de manera flexible, lo que ayuda a mantener las configuraciones sensibles (como contraseñas y URIs de bases de datos) fuera del código fuente haciendo el proyecto más seguro.


## INSTALACIÓN DEL PROYECTO:

Clonar el repositorio:  
`git clone git@github.com:FacuToledo0/EFI-Python.git`  

Crear un entorno virtual:  
`python3 -m venv env` 

Activar el entorno virtual 
`source env/bin/activate`  

Instalar requerimientos:  
`pip install -r requirements.txt`  

Crear una base de datos (con el entotno activado):  
`sudo /opt/lampp/lampp start`  

Inicializa la base de datos
`flask db init `// Solo la primera vez que inicies el proyecto

Comando para hacer una migración
`flask db migrate -m "nombre de la migracion"`

Comando para actualizar la migración
`flask db upgrade` 

Correr el programa:  
`flask run --reload` 

Para que el proyecto funcione correctamente, cada vez que lo iniciemos hay que correr estos comandos desde la consola:
`source env/bin/activate`
`sudo /opt/lampp/lampp start`
`flask run --reload`
