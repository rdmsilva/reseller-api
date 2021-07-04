from http import HTTPStatus

from flask import Blueprint, request
from flask import jsonify
from sqlalchemy.exc import IntegrityError

from app.models.reseller import Reseller
from app.schemas.reseller import ResellerSchema
from app.services.reseller import get_reseller_by_cpf, save_new_reseller

reseller = Blueprint('reseller', __name__, url_prefix='/v1')


@reseller.route('/reseller/<cpf>', methods=['GET'])
def get_reseller(cpf):
    result = get_reseller_by_cpf(cpf)
    if not result:
        return jsonify({'message': 'reseller not found'}), HTTPStatus.NOT_FOUND
    return jsonify(result.to_dict())


@reseller.route('/reseller', methods=['POST'])
def post_reseller():
    if not request.is_json:
        return jsonify({'msg': 'no body request'}), HTTPStatus.BAD_REQUEST

    data = request.json.get('data')

    try:
        errors = ResellerSchema().validate(data)
        if errors:
            return jsonify({'message': errors}), HTTPStatus.BAD_REQUEST

        reseller_id = save_new_reseller(Reseller(**data))

    except IntegrityError as err:
        return jsonify({'message': err.orig.args[1]}), HTTPStatus.CONFLICT

    return jsonify({'message': 'saved', 'id': reseller_id}), HTTPStatus.CREATED
