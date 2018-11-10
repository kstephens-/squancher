import logging
import types
from flask import (
    Blueprint,
    current_app,
    jsonify,
    make_response,
    request
)
from flask_restful import Api, Resource
from .models import Document
from .schemas import DocumentSchema
from ..extensions import pgdb
from ..utils import api_route
from ..squancher import Squancher

logger = logging.getLogger(__name__)

bp = Blueprint('api', __name__,
               template_folder='../templates',
               static_folder='../static/bundle')

api = Api(bp)
api.route = types.MethodType(api_route, api)


@bp.route('/api/squanch', methods=['POST'])
def squanch_test():

    try:
        body = request.get_json()

        sq = Squancher()
        return jsonify({'text': sq.squanch(body['text'])})

    except Exception as e:
        logger.exception(e)
        return make_response(
            jsonify(error='Error while squanching text'), 500
        )
