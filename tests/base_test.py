import os
from unittest import TestCase

from flask.testing import FlaskClient

# os.environ['env'] = 'test'


class SetUpTestCase(TestCase):
    app: FlaskClient = None

    @classmethod
    def setUpClass(cls) -> None:
        # from settings import ROOT_PATH
        # from alembic.config import Config
        # from alembic import command
        #
        # alembic_cfg = Config(file_=f'{ROOT_PATH}/alembic.ini')
        # alembic_cfg.set_main_option('script_location', f'{ROOT_PATH}/alembic')
        # command.upgrade(alembic_cfg, 'head')

        from app.app import create_app
        app = create_app()
        app.config['DEBUG'] = True
        cls.app = app.test_client()

    @classmethod
    def tearDownClass(cls) -> None:
        pass
        # from settings import ROOT_PATH
        # db_file = f'{ROOT_PATH}/tests/test.db'
        # if os.path.exists(db_file):
        #     os.remove(db_file)
