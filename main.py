from flask import Flask

import settings
from app.ext.log import logger

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'


if __name__ == '__main__':
    logger.info(f'Run appliation version={settings.VERSION}')
    app.run(debug=True)
