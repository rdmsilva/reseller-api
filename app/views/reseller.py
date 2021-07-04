from datetime import datetime
from http import HTTPStatus

from flask import Blueprint, request
from flask import jsonify
from sqlalchemy.exc import IntegrityError

from app.models.base import async_session
from app.models.reseller import Reseller
from app.schemas.reseller import ResellerSchema

reseller = Blueprint('reseller', __name__, url_prefix='/v1')


@reseller.route('/reseller/<id>', methods=['GET'])
def get_reseller(id):
    with async_session() as session:
        result = session.query(Reseller).filter_by(cpf=id).first()
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

        reseller = Reseller(**data)
        reseller.created_at = datetime.now()
        reseller.save()
    except IntegrityError as err:
        return jsonify({'message': err.orig.args[1]}), HTTPStatus.CONFLICT

    return jsonify({'message': 'saved'}), HTTPStatus.CREATED
