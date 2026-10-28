# Taller: Módulos, funciones y decoradores de Django

**Curso:** Desarrollo de Aplicaciones Web I  
**Docente:** Jose Javier Torres Vanstrahlen

## 1. Introducción

Django es un framework de Python que permite desarrollar aplicaciones web. En este taller se creó un endpoint para gestionar tareas mediante los métodos HTTP GET, POST, PUT y DELETE, utilizando una vista basada en clase y respuestas en formato JSON.

## 2. Módulos utilizados

| Módulo | Descripción |
|---|---|
| `json` | Módulo de Python que permite convertir datos JSON en objetos de Python mediante `json.loads()`. |
| `django.http` | Módulo de Django del que se importa `JsonResponse`, utilizado para devolver respuestas HTTP en formato JSON. |
| `django.views` | Módulo que proporciona la clase `View`, utilizada como base para crear vistas basadas en clase. |
| `django.urls` | Módulo que proporciona `path()` e `include()`, utilizados para definir y conectar las rutas del proyecto. |
| `django.views.decorators.csrf` | Módulo que proporciona el decorador `csrf_exempt`, utilizado para excluir una vista de la comprobación CSRF. |

## 3. Funciones y métodos utilizados

| Función o método | Descripción |
|---|---|
| `JsonResponse()` | Devuelve una respuesta HTTP con datos en formato JSON. |
| `as_view()` | Convierte una clase de vista en una vista que Django puede utilizar en sus rutas. |
| `path()` | Define una ruta y la conecta con una vista. |
| `include()` | Permite incorporar las rutas de una aplicación al archivo de rutas principal. |
| `get()` | Procesa las solicitudes HTTP GET para consultar las tareas. |
| `post()` | Procesa las solicitudes POST para crear tareas. |
| `put()` | Procesa las solicitudes PUT para actualizar una tarea. |
| `delete()` | Procesa las solicitudes DELETE para eliminar una tarea. |
| `json.loads()` | Convierte los datos JSON recibidos en objetos de Python. |
| `max()` | Obtiene el valor máximo de una colección; se utiliza para generar el siguiente identificador. |
| `append()` | Agrega una nueva tarea a la lista. |
| `remove()` | Elimina una tarea de la lista. |

## 4. Decorador utilizado

### `csrf_exempt`

Es un decorador de Django que excluye una vista de la comprobación de protección CSRF.

En este proyecto se utilizó para permitir las pruebas de los métodos POST, PUT y DELETE sin enviar un token CSRF. Aunque facilitó las pruebas, en aplicaciones reales debe evaluarse cuidadosamente su uso, ya que desactiva una protección de seguridad para la vista correspondiente.

## 5. Fuentes de investigación

1. **Django Software Foundation.** *Base views.*  
   https://docs.djangoproject.com/en/6.1/ref/class-based-views/base/

2. **Django Software Foundation.** *Request and response objects.*  
   https://docs.djangoproject.com/en/6.1/ref/request-response/

3. **Django Software Foundation.** *URL dispatcher.*  
   https://docs.djangoproject.com/en/6.1/topics/http/urls/

4. **Django Software Foundation.** *Cross Site Request Forgery protection.*  
   https://docs.djangoproject.com/en/6.1/ref/csrf/

5. **Python Software Foundation.** *JSON — JSON encoder and decoder.*  
   https://docs.python.org/3/library/json.html
