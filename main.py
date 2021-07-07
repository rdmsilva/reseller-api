from flask import jsonify

import settings
from app.app import create_app
from app.exceptions import CustomException
from log import logger
from settings import DEBUG

app = create_app()


@app.errorhandler(CustomException)
def handle_custom_exception(error):
    return jsonify(msg=error.msg), error.status_code


if __name__ == '__main__':
    logger.info(f'Run application version={settings.VERSION}')
    app.run(debug=DEBUG)
