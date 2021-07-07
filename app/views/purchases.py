from http import HTTPStatus

from flask import Blueprint, request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.schemas.purchase import PurchaseSchema
from app.services.purchase import save_new_purchase, update_purchase, delete_purchase, \
    find_all_purchases, validated_auth_cpf

purchase = Blueprint('purchases', __name__, url_prefix='/v1')


@purchase.route('/purchases', methods=['GET'])
@jwt_required()
def get_all_purchase():
    auth_cpf = get_jwt_identity()

    result = find_all_purchases(auth_cpf)

    if not result:
        return jsonify(body=[], msg='reseller does not have purchases'), HTTPStatus.OK

    return jsonify(body=result), HTTPStatus.OK


@purchase.route('/purchases', methods=['POST'])
@jwt_required()
def post_purchase():
    if not request.is_json:
        return jsonify(msg='no body request'), HTTPStatus.BAD_REQUEST

    data = request.json.get('data')

    errors = PurchaseSchema().validate(data)

    if errors:
        return jsonify(msg=errors), HTTPStatus.BAD_REQUEST

    auth_cpf = get_jwt_identity()

    if auth_cpf != int(data['cpf']):
        return jsonify(msg='purchase cpf must be the same that reseller'), HTTPStatus.UNAUTHORIZED

    purchase_id = save_new_purchase(data)
    status_code = HTTPStatus.CREATED

    return jsonify(msg='saved', id=purchase_id), status_code


@purchase.route('/purchases', methods=['PUT'])
@jwt_required()
def put_purchase():
    if not request.is_json:
        return jsonify(msg='no body request'), HTTPStatus.BAD_REQUEST

    auth_cpf = get_jwt_identity()
    data = request.json.get('data')
    response = update_purchase(data, auth_cpf)
    return response


@purchase.route('/purchases/<purchase_id>', methods=['DELETE'])
@jwt_required()
def del_purchase(purchase_id):
    auth_cpf = get_jwt_identity()
    response = delete_purchase(purchase_id, auth_cpf)
    return response
