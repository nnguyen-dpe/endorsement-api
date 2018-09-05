from flask_restplus import reqparse

_get_endorse_req = reqparse.RequestParser()
_get_endorse_req.add_argument(
    name='developer', type=str, required=False, location='args',
    help='Filter by the developer\'s id')
_get_endorse_req.add_argument(
    name='skill', type=str, required=False, location='args',
    help='Filter by the developer\'s skill')


_post_endorse_req = reqparse.RequestParser()
_post_endorse_req.add_argument(
    'developer', type=str, required=True, location='json', help='Developer id is required'
)
_post_endorse_req.add_argument(
    'skill', type=str, required=True, location='json', help='Skill name is required'
)
