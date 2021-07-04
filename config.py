import os


class DevConfig:
    DEBUG = True
    DB_URI = 'mysql+pymysql://dev:dev@localhost/reseller-db'
    ENCRYPTED_KEY = '393b3126-4fe4-4698-9610-c6b73b4c276c'


class TestConfig:
    DEBUG = True
    DB_URI = f'sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests/test.db")}'
    ENCRYPTED_KEY = '123546789'


config_app = {
    'test': TestConfig,
    'dev': DevConfig
}
