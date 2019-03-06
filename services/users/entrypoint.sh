#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z users-db 5432; do
  sleep 0.1
done

ls

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0