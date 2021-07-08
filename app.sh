#!/bin/bash

echo "upgrade database"
alembic revision --autogenerate
alembic upgrade head

echo "starting app"
gunicorn --bind 0.0.0.0:5000 main:app
