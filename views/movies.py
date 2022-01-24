from flask_restx import Resource, Namespace

from models import MovieSchema, Movie
from setup_db import db



movies_ns = Namespace('movie')
movie_schema = MovieSchema()
movie_schema = MovieSchema(many=True)

@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
        all_movies = db.session.query(Movie).all()
        return movie_schema.dump(all_movies), 200

