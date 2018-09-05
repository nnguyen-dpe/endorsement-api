# Rest view model for api requests and responses
from flask_restplus import fields
from apis.api import api
from apis.exceptions import ApiError

_endorsement = api.model('Endorsement', {
    'developer': fields.String(required=True, readOnly=True),
    'skill': fields.String(required=True, readOnly=True),
    'count': fields.Integer(required=False)
})

_endorsement_list = api.model('EndorsementCollection', {
    'totalRecords': fields.Integer(required=True),
    'items': fields.List(fields.Nested(_endorsement))
})

_err = api.model('Error', {
    'errorCode': fields.String(required=True, description='Error types',
                               enum=ApiError._member_names_),
    'errorDescription': fields.String(required=True)
})
