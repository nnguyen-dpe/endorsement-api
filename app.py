import os

from database import db
from flask import Flask
from apis.api import api
from apis.routes import ns as endorsement_ns

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/endorsementdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api.add_namespace(endorsement_ns, '/api/v1')
api.init_app(app)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
