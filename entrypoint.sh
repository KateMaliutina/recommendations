#!/bin/bash

echo "Wait PostgreSQL..."
while ! nc -z recommendations-db 5432; do
  sleep 1
done

echo "Database is ready. Applying migrations..."
alembic upgrade head

echo "FastAPI is running..."
exec uvicorn app.main:app --host 0.0.0.0 --port 80
