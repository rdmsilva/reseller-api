from alembic import command
from alembic.config import Config

from settings import ROOT_PATH


if __name__ == '__main__':
    alembic_cfg = Config(file_=f'{ROOT_PATH}/alembic.ini')
    alembic_cfg.set_main_option('script_location', f'{ROOT_PATH}/alembic')
    command.upgrade(alembic_cfg, 'head')
