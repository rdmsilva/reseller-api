from datetime import datetime
from http import HTTPStatus

from flask import Blueprint, request
from flask import jsonify

from app.models.reseller import Reseller

reseller = Blueprint('reseller', __name__, url_prefix='/v1')


@reseller.route('/reseller', methods=['GET'])
def get_reseller():
    return jsonify({'reseller': {'id': 1}})


@reseller.route('/reseller', methods=['POST'])
def post_reseller():

    if not request.is_json:
        return jsonify({'msg': 'no body request'}), HTTPStatus.BAD_REQUEST

    data = request.json.get('data')

    reseller = Reseller(**data)
    reseller.created_at = datetime.now()
    reseller.save()

    return jsonify({'message': 'saved'}), HTTPStatus.OK
