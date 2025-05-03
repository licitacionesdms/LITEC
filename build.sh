#!/usr/bin/env bash

# Instala dependencias si usas algún archivo externo adicional (opcional)
# pip install -r requirements.txt

# Aplica migraciones a la base de datos
python manage.py migrate

# Recolecta archivos estáticos (CSS, JS, imágenes...) en /staticfiles
python manage.py collectstatic --noinput
