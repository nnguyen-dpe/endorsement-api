# Define api routes for namespace
import logging
import time

from flask import request
from flask_restplus import Resource, Namespace
from datetime import datetime
from apis.api import api
from apis.views import _endorsement, _endorsement_list, _err, ApiError
from apis.parsers import _get_endorse_req, _post_endorse_req
from apis.service import _srv
from apis.exceptions import NotFoundException, InvalidRequestException

ns = Namespace(
    name='endorsement', 
    description="Endorsement api for developer skills"
)

log = logging.getLogger(__name__)


@ns.route('/health')
class HealthCheck(Resource):
    @api.response(200, 'Health check ok')
    def get(self):
        return {
            'message': 'Health checked at: ' + str(datetime.now())
        }, 200

@ns.route('/endorsement')
@api.response(400, 'Invalid request', _err)
@api.response(500, 'Internal server error', _err)
class EndorsementCollection(Resource):
    @api.marshal_with(_endorsement_list)
    @api.response(200, 
        'The search was performed successfully', _endorsement_list)
    @api.expect(_get_endorse_req)
    @api.doc(description='Get one or more endorsement', id='getEndorsement')
    def get(self, **kwargs):
        args = _get_endorse_req.parse_args(request)
        return _srv.search(args), 200
    

@ns.route('/endorsement/<string:action>', doc={'params': {'action': 'vote up or down'}})
@api.response(404, 'Resource not found', _err)
@api.response(500, 'Internal server error', _err)
class Endorsement(Resource):
    @api.expect(_endorsement)
    @api.doc(description='Vote up or down', id='vote')
    def post(self, action):        
        try:
            _post_endorse_req.parse_args(request)
            data = request.json
            return _srv.vote(data, action), 200
        except:
            return {
                'errorCode': 'InvalidRequest',
                'errorDescription': 'Bad'
            }, 400

