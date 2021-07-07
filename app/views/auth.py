from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from app.services.reseller import get_reseller_by_cpf, password_is_valid

auth = Blueprint('auth', __name__, url_prefix='/v1')


@auth.route('/auth', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify(msg='missing authorization'), HTTPStatus.BAD_REQUEST

    user = get_reseller_by_cpf(cpf=auth.username)

    if not user:
        return jsonify(msg='user not found'), HTTPStatus.UNAUTHORIZED

    if password_is_valid(auth.password, user):
        return jsonify(token=create_access_token(identity=user.cpf), id=user.id)

    return jsonify(msg='user or password is wrong'), HTTPStatus.UNAUTHORIZED
