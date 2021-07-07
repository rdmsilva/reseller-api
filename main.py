import settings
from app.app import create_app
from log import logger
from settings import DEBUG

app = create_app()


@app.route('/home')
def home():
    return 'home'


if __name__ == '__main__':
    logger.info(f'Run application version={settings.VERSION}')
    app.run(debug=DEBUG, host='0.0.0.0', port=5000)
