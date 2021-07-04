import settings
from app.app import create_app
from log import logger

app = create_app()

if __name__ == '__main__':
    logger.info(f'Run application version={settings.VERSION}')
    app.run(debug=True)
