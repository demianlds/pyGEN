Manual técnico de pyGEN:

Técnologias utilizadas: Django (Basado en Python), HTML, CSS, Bootstrap

Rudimentos:

1. Crea la carpeta contenedora y entorno virtual

mkdir control_stock
cd control_stock

Configura un entorno virtual:

python3 -m venv *nombre entorno virtual*

# source *nombre entorno virtual*/bin/activate  
# .\*nombre entorno virtual*\Scripts\activate EN WINDOWS


Instala Django y SQLite (incluido en Python):
# pip install django

2. Crear el proyecto en Django
Inicia un proyecto Django:
django-admin startproject *nombre entorno virtual* .

3. Crea una aplicación dentro del proyecto:

En Django, las aplicaciones son módulos específicos de funcionalidad.

# python manage.py startapp *nombre de la aplicación*

Registra la nueva aplicación:

# Abre *proyecto*/settings.py y añade *nombre de aplicación* en la lista de INSTALLED_APPS:

4. Diseña los modelos de base de datos
Define los modelos para las tablas.

# *nombre de la aplicación*/models.py

5. Aplica las migraciones

# python manage.py makemigrations
# python manage.py migrate

6. Configura el panel de administración

Añade los modelos al administrador de Django para gestionarlos desde la interfaz gráfica:

# Archivo: *nombre aplicación*/admin.py
