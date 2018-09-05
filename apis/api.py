from flask_restplus import Api
from apis.exceptions import NotFoundException, InvalidRequestException, ApiError

desc = """
A microservice to endorse developer skills
"""

api = Api(
    version='1.0', 
    title='Endorsement API', 
    description=desc,
    tags='endorsement'
)

@api.errorhandler
def default_exception_handler(error):
    return {
        'errorCode': ApiError.InternalServerError.name,
        'errorDescription': error.message
    }, 500

@api.errorhandler(NotFoundException)
def notfound_exception_handler(error):
    return {
        'errorCode': ApiError.NotFound.name,
        'errorDescription': error.message
    }, 404

@api.errorhandler(InvalidRequestException)
def invalidrequest_exception_handler(error):
    return {
        'errorCode': ApiError.InvalidRequest.name,
        'errorDescription': error.message
    }, 400

