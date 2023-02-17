from flask_restx import Resource, Namespace
from models import DirectorSchema, Director
from setup_db import db

directors_ns = Namespace('director')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = db.session.query(Director).all()
        return directors_schema.dump(all_directors), 200