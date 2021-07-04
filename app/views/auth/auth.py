from http import HTTPStatus

from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__, url_prefix='/v1')


@auth.route('/auth', methods=['GET'])
def login():
    return jsonify({'message': 'ok'}), HTTPStatus.OK
