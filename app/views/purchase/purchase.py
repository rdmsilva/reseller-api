from http import HTTPStatus

from flask import Blueprint, request
from flask import jsonify
from sqlalchemy.exc import IntegrityError

from app.services.purchase import save_new_purchase, get_purchase_by_cpf
from app.models.purchase import Purchase
from app.schemas.purchase import PurchaseSchema

purchase = Blueprint('purchase', __name__, url_prefix='/v1')


@purchase.route('/purchase/<cpf>', methods=['GET'])
def get_purchase(cpf):
    result = get_purchase_by_cpf(cpf)
    if not result:
        return jsonify({'message': 'purchases not found'}), HTTPStatus.NOT_FOUND
    return jsonify(result.to_dict())


@purchase.route('/purchase', methods=['POST'])
def post_purchase():
    if not request.is_json:
        return jsonify({'msg': 'no body request'}), HTTPStatus.BAD_REQUEST

    data = request.json.get('data')

    try:
        errors = PurchaseSchema().validate(data)
        if errors:
            return jsonify({'message': errors}), HTTPStatus.BAD_REQUEST

        purchase_id = save_new_purchase(Purchase(**data))

    except IntegrityError as err:
        return jsonify({'message': err.orig.args[1]}), HTTPStatus.CONFLICT

    return jsonify({'message': 'saved', 'id': purchase_id}), HTTPStatus.CREATED
