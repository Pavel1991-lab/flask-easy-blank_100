from flask_restx import Resource, Namespace
from flask import request
from models import MovieSchema, Movie
from setup_db import db



movies_ns = Namespace('movie')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
        year = request.args.get('year')
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        movie_schema = MovieSchema(many=True)
        st = Movie.query
        if year:
            st = st.filter(Movie.year == year)
        if director_id:
            st = st.filter(Movie.director_id == director_id)
        if genre_id:
            st = st.filter(Movie.genre_id == genre_id)
        movies = st.all()
        return movie_schema.dump(movies), 200


@movies_ns.route('/<int:uid>')
class MoviesView(Resource):
    def get(self, uid:int):
        movie =  Movie.query.get(uid)
        if not movie:
            return 'Такого фильма нету', 404
        return movie_schema.dump(movie), 200



