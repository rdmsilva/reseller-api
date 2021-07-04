from datetime import datetime
from http import HTTPStatus

from flask import Blueprint, request
from flask import jsonify
from sqlalchemy.exc import IntegrityError

from app.models.base import async_session
from app.models.purchase import Purchase
from app.schemas.purchase import PurchaseSchema

purchase = Blueprint('purchase', __name__, url_prefix='/v1')


@purchase.route('/purchase/<cpf>', methods=['GET'])
def get_purchase(id):
    with async_session() as session:
        result = session.query(Purchase).filter_by(cpf=id).all()
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

        purchase = Purchase(**data)
        purchase.created_at = datetime.now()
        purchase.status = 'Aprovado' if purchase.cpf == '15350946056' else 'Em validação'
        purchase.save()
    except IntegrityError as err:
        return jsonify({'message': err.orig.args[1]}), HTTPStatus.CONFLICT

    return jsonify({'message': 'saved'}), HTTPStatus.CREATED
