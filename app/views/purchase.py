from http import HTTPStatus

from flask import Blueprint, request
from flask import jsonify
from flask_jwt_extended import jwt_required

from app.models.purchase import Purchase
from app.schemas.purchase import PurchaseSchema
from app.services.purchase import save_new_purchase, update_purchase, get_purchase_by_id, APPROVED

purchase = Blueprint('purchase', __name__, url_prefix='/v1')


@purchase.route('/purchase/<id>', methods=['GET'])
@jwt_required()
def get_purchase(id):
    result = get_purchase_by_id(id)
    if not result:
        return jsonify(msg='purchases not found'), HTTPStatus.NOT_FOUND
    return jsonify(result.to_dict())


@purchase.route('/purchase', methods=['POST'])
@jwt_required()
def post_purchase():
    if not request.is_json:
        return jsonify(msg='no body request'), HTTPStatus.BAD_REQUEST

    data = request.json.get('data')

    errors = PurchaseSchema().validate(data)

    if errors:
        return jsonify(msg=errors), HTTPStatus.BAD_REQUEST

    purchase_id = save_new_purchase(Purchase(**data))
    status_code = HTTPStatus.CREATED

    return jsonify(msg='saved', id=purchase_id), status_code


@purchase.route('/purchase', methods=['PUT'])
@jwt_required()
def put_purchase():
    if not request.is_json:
        return jsonify(msg='no body request'), HTTPStatus.BAD_REQUEST

    data = request.json.get('data')

    errors = PurchaseSchema().validate(data)

    if errors:
        return jsonify(msg=errors), HTTPStatus.BAD_REQUEST

    actual = get_purchase_by_id(id=data['id'])

    if not actual:
        return jsonify(msg='purchase not found'), HTTPStatus.BAD_REQUEST

    if actual.status == APPROVED:
        return jsonify(msg='purchase is already approved'), HTTPStatus.BAD_REQUEST

    updated = update_purchase(actual, data)

    return jsonify(updated.to_dict()), HTTPStatus.OK
