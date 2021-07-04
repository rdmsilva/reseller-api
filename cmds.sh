pip install alembic
alembic init .
alembic upgrade head
coverage run -m unittest discover && coverage report --omit='*/venv/*'
coverage html --omit='*/venv/*'