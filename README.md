Proyecto Blog Django — Playground Final Project
Descripción
Este proyecto es una aplicación web tipo blog desarrollada en Python con el framework Django. Cuenta con funcionalidades completas de administración, perfiles de usuario, registro y autenticación, páginas de contenido y mensajería entre usuarios.

El objetivo es cumplir con los requerimientos funcionales indicados en el enunciado, implementando buenas prácticas como uso de vistas basadas en clases, mixins, herencia de templates y manejo de formularios con imágenes.

Funcionalidades principales
Home: Vista principal con bienvenida y navegación.

About: Página “Acerca de mí” con información estática sobre el dueño de la página en la ruta /about/.

Pages: Listado de páginas (o posts) del blog en /pages/ con mensaje "No hay páginas aún" cuando está vacío.

Detalle de página: Vista detalle con toda la información de la página, accediendo desde /pages/<id>/.

CRUD completo de páginas: Crear, actualizar y borrar páginas solo para usuarios autenticados.

Autenticación: Registro, login, logout.

Perfil: Vista y edición de datos del usuario, incluyendo avatar, biografía y cambio de contraseña.

Mensajería: Sistema para que los usuarios puedan enviarse mensajes privados.

Admin: Registro completo de modelos en el panel administrador de Django.

Formularios con imágenes: Manejo correcto de subida y despliegue de imágenes.

Manejo de sesiones y permisos: Uso de decoradores y mixins para controlar acceso.

Herencia de templates: Plantilla base con barra de navegación para facilitar la navegación.

Modelo principal
El modelo principal Page (o Post, según preferencia) contiene al menos:

Título (CharField)

Subtítulo o categoría (CharField)

Contenido enriquecido con CKEditor (RichTextField)

Imagen destacada (ImageField)

Fecha de creación/publicación (DateField)

Estructura del proyecto
accounts/: App para manejo de usuarios (registro, login, perfil).

pages/: App principal con modelo Page y CRUD.

messenger/: App para mensajería interna entre usuarios.

templates/: Plantillas HTML con herencia y fragmentos reutilizables.

static/: Archivos estáticos como CSS, JS, imágenes del proyecto.

media/: Carpeta para almacenar imágenes subidas por usuarios (excluida del repo).

Tecnologías usadas
Python 3.x

Django 4.x

Django CKEditor para contenido enriquecido

Bootstrap 5 (opcional para estilos y responsive)

SQLite para desarrollo (db.sqlite3 ignorada en Git)

Git para control de versiones
