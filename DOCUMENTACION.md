## DOCUMENTACIÓN DE ENDPOINTS: 


#### NOTA GENERAL:
Todos los endpoints requieren que el usuario esté autenticado y tenga permisos de administrador para realizar acciones específicas. En caso de errores, se proporcionan mensajes claros que indican el problema.

##### LOGIN : 


##### MÉTODO POST / AUTENTICACIÓN
Endpoint : /login

Cuerpo de la solicitud: 
```json
    {
    "username":"nombre",
    "password":"contraseña"
    }
```
Respuesta: 
```json
    {
    "token":"token_de_autenticacion"
    }
```

#### USERS: 


##### MÉTODO POST 

Endpoint : /users

Cuerpo de la solicitud: 
```json
    {
    "username":"Facundo",
    "password":"1234"
    }
```
Respuesta:
```json 
{
  "Mensaje": "Usuario creado correctamente",
  "Usuario": {
    "username": "usuario nuevo",
    "is_admin": true
  }
}
```
Mensajes de error:  
    `403 Forbidden`: Solo el admin puede crear nuevos usuarios.  
    `500 Internal Server Error`: Fallo la creación del nuevo usuario.  
 

##### MÉTODO GET

Si el usuario que inicio sesión es administrador, se devuelve la lista completa con detalles de cada usuario. Si el usuario no es administrador, se devuelve una versión minimalista de los datos del usuario.

##### MÉTODO DELETE

Endpoint : /users/<id>/borrar

Respuesta:
```json
{
  "200 OK": "Usuario eliminado correctamente."
}
```
Mensajes de error:   
    `403 Forbidden`: Solo el admin puede eliminar usuarios.  
    `404 Not found`:Usuario no encontrado.  
    `500 Internal Server Error`: Fallo al eliminar el usuario.  

##### MÉTODO PUT 

Endpoint : /users/<id>/editar

Cuerpo de la solicitud: 
```json
    {
    "username":"editar_usuario",
    "password": "editar_contraseña"
    }
```
Respuesta:
```json
{
  "200  OK": "Usuario actualizado correctamente."
}
```
Mensajes de error:   
    `403 Forbidden`: No tienes permiso para actualizar usuarios.  
    `404 Not found`:Usuario no encontrado.  
    `500 Internal Server Error`: Error al actualizar el usuario.  


#### MARCA: 


##### MÉTODO POST


Endpoint : /marca

Cuerpo de la solicitud: 
```json
    {
    "nombre":"nombre"
    }
```
Respuesta:
```json
"marcas":
    {
      "id": 1,
      "nombre": "Samsumg"
    }
```
Mensajes de error:   
    `403 Forbidden`: No está autorizado para crear marcas.  
    `403 Forbidden`: No está autorizado para editar marca.  
 


##### MÉTODO GET 


Endpoint : /marca

Respuesta: 
```json
{
  "marcas": [
    {
      "id": 1,
      "nombre": "Samsung"
    },
    {
      "id": 2,
      "nombre": "Apple"
    },
    {
      "id": 3,
      "nombre": "Motorola"
    },
  ]
}
```

#### MODELO: 

##### MÉTODO POST: 


Endpoint : /modelo

Endpoint : /modelo/<id>/borrar

Respuesta:
```json
{
  "200  OK": "Modelo eliminado correctamente."
}
```

Mensajes de error:   
    `400 Bad Request`: Debe proporcionar 'telefono_id' y 'cantidad'.  
    `400 Bad Request`: Cantidad debe ser un número entero.  
    `400 Bad Request`: Datos inválidos  
    `403 Forbidden`: No está autorizado para acceder a esta ruta.  
    `403 Forbidden`: No está autorizado para borrar stock.  
    

##### MÉTODO GET: 


Endpoint : /modelo_list

Respuesta:
```json
[
  {
    "accesorios": [
      {
        "id": 1,
        "nombre": "Iphone 11"
      },
      {
        "id": 3,
        "nombre": "Iphone 12"
      },
      ...
    ]
  }
]
```

#### ACCESORIOS: 

##### MÉTODO POST: 

Endpoint : /accesorios

Cuerpo de la solicitud: 
```json
    {
    "nombre":"nombre"
    }
```
Respuesta: 
```json
    {
     "201 Created": "Accesorio creado exitosamente"
    }
```
Mensaje de error:
```json 
{
    "403 Forbidden": "No está autorizado para crear accesorios."
}
```

##### MÉTODO DELETE: 
Endpoint : /accesorio/<id>/borrar

Respuesta: 
```json
{
  "200 OK":"Accesorio eliminado correctamente."
}
```
Mensaje de error: 
```json
{
    "403 Forbidden": "Solo el administrador puede eliminar accesorios."
}
```

##### MÉTODO PUT 

Endpoint : /accesorio/<id>/editar

Cuerpo de la solicitud: 
```json
    {
    "nombre":"editar_accesorio"
    }
```
Respuesta:
```json
{
  "200  OK": "Accesorio editado con éxito."
}
```
Mensaje de error:   
```json
{
    "403 Forbidden": "No está autorizado para editar accesorio"  
}
```

##### MÉTODO GET: 

Endpoint : /accesorios_list

Respuesta: 
```json
{
  "200 OK": {
    "accesorios": [
      {
        "id": 1,
        "nombre": "Cargador Samsung"
      },
      {
        "id": 3,
        "nombre": "Funda Apple original"
      },
      ...
    ]
  }
}
```

#### FABRICANTE: 


##### MÉTODO POST: 
Endpoint : /fabricante

Cuerpo de la solicitud: 
```json
    {
    "nombre_fabricante":"fabricante",
    "pais_origen":"pais"
    }
```
Respuesta: 
```json
{
  "200": "Fabricante creado exitosamente"
}
```

##### MÉTODO PUT:
Endpoint: /fabricante/<id>/editar

Respuesta: 
```json
{
  "200": "El fabricante esta editado con éxito."
}
```


Mensajes de error:     
    `403 Forbidden`: No está autorizado para editar el fabricante.      


##### MÉTODO GET: 
Endpoint : /fabricante_list

Respuesta: 
```json
{
  "200 OK": {
    "fabricantes": [
      {
        "id": 1,
        "nombre_fabricante": "Fabricante 1",
        "pais_origen": "Argentina"
      },
      {
        "id": 3,
        "nombre_fabricante": "Fabricante 2",
        "pais_origen": "España"
      },
    ]
  }
}
```

##### MÉTODO DELETE: 
Endpoint : /fabricante/<id>/borrar

Respuesta: 
```json
{
  "200 OK":"Fabricante eliminado correctamente."
}
```
Mensaje de error: 
```json
{
    "403 Forbidden": "Solo el administrador puede eliminar fabricantes."
}
```

#### PROVEEDOR: 


##### MÉTODO POST: 
Endpoint : /proveedor

Cuerpo de la solicitud: 
```json
    {
    "nombre_proveedor":"proveedor",
    "contacto":"contacto"
    }
```
Respuesta: 
```json
{
  "200": "Proveedor creado exitosamente"
}
```

##### MÉTODO PUT:
Endpoint: /proveedor/<id>/editar

Respuesta: 
```json
{
  "200": "El proveedor esta editado con éxito."
}
```


Mensajes de error:     
    `403 Forbidden`: No está autorizado para editar el proveedor.      


##### MÉTODO GET: 
Endpoint : /proveedor_list

Respuesta: 
```json
{
  "200 OK": {
  "proveedores": [
    {
      "contacto": "3468-504500",
      "id": 1,
      "nombre_proveedor": "ImportApple"
    }
  ]
}
}
```

##### MÉTODO DELETE: 
Endpoint : /proveedor/<id>/borrar

Respuesta: 
```json
{
  "200 OK":"Proveedor eliminado correctamente."
}
```
Mensaje de error: 
```json
{
    "403 Forbidden": "Solo el administrador puede eliminar proveedores."
}
```


#### EQUIPO: 


##### MÉTODO POST: 


Endpoint: /equipo

Cuerpo de la solicitud: 
```json
    {
  "anio_fabricacion":"2023",
  "precio":"5000000",
  "marca_id":1, // ID de la marca
  "modelo_id":1, //ID del modelo
  "proveedor_id":1, // ID del proveedor
  "fabricante_id":1, // ID del fanricante
  "accesorio_id":1 // ID del accesorio
    }
```
Respuesta: 
```json
{
   "200 OK": "Celular creado exitosamente."
}
```

##### MÉTODO GET: 
Endpoint: /equipo_list

Respuesta: 
```json
{
  "equipos": [
    {
      "accesorio": {
        "id": 5,
        "tipo_accesorio": "Cargador 200W"
      },
      "accesorio_id": 5,
      "anio_fabricacion": 2023,
      "fabricante": {
        "id": 4,
        "nombre_fabricante": "Fabricante 3",
        "pais_origen": "Brasil"
      },
      "fabricante_id": 4,
      "id": 1,
      "marca": {
        "id": 140,
        "nombre": "Apple"
      },
      "marca_id": 140,
      "modelo": {
        "id": 2,
        "nombre": "Iphone 11"
      },
      "modelo_id": 2,
      "precio": 1200,
      "proveedor": {
        "contacto": "3468-504500",
        "id": 1,
        "nombre_proveedor": "ImportApple"
      },
      "proveedor_id": 1
    },
    {
      "accesorio": {
        "id": 8,
        "tipo_accesorio": "Airpods"
      },
      "accesorio_id": 8,
      "anio_fabricacion": 2024,
      "fabricante": {
        "id": 6,
        "nombre_fabricante": "Fabricante 5",
        "pais_origen": "Estados Unidos"
      },
      "fabricante_id": 6,
      "id": 2,
      "marca": {
        "id": 140,
        "nombre": "Apple"
      },
      "marca_id": 140,
      "modelo": {
        "id": 5,
        "nombre": "Iphone 14"
      },
      "modelo_id": 5,
      "precio": 1200000,
      "proveedor": {
        "contacto": "3468-504500",
        "id": 1,
        "nombre_proveedor": "ImportApple"
      },
      "proveedor_id": 1
    },
    {
      "accesorio": {
        "id": 2,
        "tipo_accesorio": "Funda"
      },
      "accesorio_id": 2,
      "anio_fabricacion": 2020,
      "fabricante": {
        "id": 1,
        "nombre_fabricante": "Fabricante 1",
        "pais_origen": "Argentina"
      },
      "fabricante_id": 1,
      "id": 3,
      "marca": {
        "id": 140,
        "nombre": "Apple"
      },
      "marca_id": 140,
      "modelo": {
        "id": 4,
        "nombre": "Iphone 13"
      },
      "modelo_id": 4,
      "precio": 500000,
      "proveedor": {
        "contacto": "3468-504500",
        "id": 1,
        "nombre_proveedor": "ImportApple"
      },
      "proveedor_id": 1
    }
  ]
}
```



