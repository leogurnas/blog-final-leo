 Blog Final - Proyecto Django

Este es mi proyecto final del curso de Django: una aplicación tipo blog donde los usuarios pueden registrarse, crear y editar páginas, y mantener un perfil con avatar y biografía.

 Funcionalidades

- Registro, inicio y cierre de sesión de usuarios
- Vista protegida de perfil con edición de avatar, bio, web y cumpleaños
- Creación, edición y eliminación de páginas (solo para usuarios logueados)
- Herencia de templates con `base.html`
- Navegación con Navbar
- Página "Acerca de mí"
- Soporte para subida de imágenes
- Formulario de cambio de contraseña
- Protecciones con `@login_required` y `LoginRequiredMixin`

🔧 Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/leogurnas/blog-final-leo.git
cd blog-final-leo


Crear entorno virtual:
python -m venv env
Instalar dependencias:
pip install -r requirements.txt
Migraciones y superusuario:
python manage.py migrate
python manage.py createsuperuser
Ejecutar el servidor:
python manage.py runserver

