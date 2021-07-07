import os


class DevConfig:
    DEBUG = True
    DB_URI = 'mysql+pymysql://dev:dev@localhost/reseller-db'
    ENCRYPTED_KEY = '393b3126-4fe4-4698-9610-c6b73b4c276c'
    SALT = '9c04c6d6-ce25-486d-9751-bbbd892673be'
    JWT_SECRET_KEY = 'ca52e637-e8d9-4de3-a2b4-85c9d99c471d'
    CASHBACK_URL = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback'
    TOKEN_CASHBACK = 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'


class TestConfig:
    DEBUG = True
    DB_URI = f'sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests/test.db")}'
    ENCRYPTED_KEY = '123546789'
    SALT = '123456789'
    JWT_SECRET_KEY = '123456789'
    CASHBACK_URL = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback'
    TOKEN_CASHBACK = 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'


config_app = {
    'test': TestConfig,
    'dev': DevConfig
}
