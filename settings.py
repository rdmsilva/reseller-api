import os

from config import config_app

ENV = os.getenv('env', 'local')

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

PROJECT = 'reseller-api'
VERSION = '0.0.1'
LOG_LEVEL = 'INFO'

DEBUG = config_app[ENV].DEBUG

CASHBACK_URL = config_app[ENV].CASHBACK_URL
TOKEN_CASHBACK = config_app[ENV].TOKEN_CASHBACK

DB_URI = config_app[ENV].DB_URI
ENCRYPTED_KEY = config_app[ENV].ENCRYPTED_KEY
SALT = config_app[ENV].SALT

JWT_SECRET_KEY = config_app[ENV].JWT_SECRET_KEY
