#!/bin/bash

echo "Criando migrations..."
python manage.py makemigrations

echo "Fazendo as migrations..."
python manage.py migrate

echo "Rodando servidor"
python manage.py runserver 0.0.0.0:8000

echo "Fim!"