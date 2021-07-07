#!/bin/bash

coverage run --omit='*/venv/*,*/tests/*' -m unittest discover &&
coverage report --omit='*/venv/*,*/tests/*' &&
coverage html --omit='*/venv/*,*/tests/*'

xdg-open htmlcov/index.html