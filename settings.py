import os

from config import config_app

PROJECT = 'reseller-api'
VERSION = '0.0.1'
LOG_LEVEL = 'INFO'

ENV = os.getenv('env', 'dev')

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DB_URI = config_app[ENV].DB_URI
ENCRYPTED_KEY = config_app[ENV].ENCRYPTED_KEY
SALT = config_app[ENV].SALT
JWT_SECRET_KEY = config_app[ENV].JWT_SECRET_KEY
