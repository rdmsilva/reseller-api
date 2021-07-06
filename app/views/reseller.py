from http import HTTPStatus

from flask import Blueprint, request
from flask import jsonify
from flask_jwt_extended import jwt_required

from app.models.reseller import Reseller
from app.schemas.reseller import ResellerSchema
from app.services.reseller import get_reseller_by_id, save_new_reseller

reseller = Blueprint('reseller', __name__, url_prefix='/v1')


@reseller.route('/reseller/<int:id>', methods=['GET'])
@jwt_required()
def get_reseller(id):
    result = get_reseller_by_id(id)

    if not result:
        return jsonify(msg='reseller not found'), HTTPStatus.NOT_FOUND

    return jsonify(result.to_dict())


@reseller.route('/reseller', methods=['POST'])
def post_reseller():
    if not request.is_json:
        return jsonify(msg='no body request'), HTTPStatus.BAD_REQUEST

    data = request.json.get('data')

    errors = ResellerSchema().validate(data)
    if errors:
        return jsonify(msg=errors), HTTPStatus.BAD_REQUEST

    reseller_id = save_new_reseller(Reseller(**data))

    return jsonify(msg='saved', id=reseller_id), HTTPStatus.CREATED
