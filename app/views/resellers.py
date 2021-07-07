from http import HTTPStatus

import requests
from flask import Blueprint, request
from flask import jsonify
from flask_jwt_extended import jwt_required

from app.models.app_models import Reseller
from app.schemas.reseller import ResellerSchema
from app.services.reseller import get_reseller_by_id, save_new_reseller
from settings import CASHBACK_URL, TOKEN_CASHBACK

reseller = Blueprint('resellers', __name__, url_prefix='/v1')


@reseller.route('/resellers/<id>/cashback', methods=['GET'])
@jwt_required()
def cashback(id):
    reseller = get_reseller_by_id(id)

    if not reseller:
        return jsonify(msg='reseller not found'), HTTPStatus.BAD_REQUEST

    try:
        response = requests.get(f'{CASHBACK_URL}?cpf={reseller.cpf}', headers={'token': TOKEN_CASHBACK})
        contents = response.json()
        return jsonify(contents['body']), HTTPStatus.OK
    except Exception:
        return jsonify(msg='service unavailable'), HTTPStatus.SERVICE_UNAVAILABLE


@reseller.route('/resellers', methods=['POST'])
def post_reseller():
    if not request.is_json:
        return jsonify(msg='no body request'), HTTPStatus.BAD_REQUEST

    data = request.json.get('data')

    errors = ResellerSchema().validate(data)
    if errors:
        return jsonify(msg=errors), HTTPStatus.BAD_REQUEST

    reseller_id = save_new_reseller(Reseller(**data))

    return jsonify(msg='saved', id=reseller_id), HTTPStatus.CREATED
