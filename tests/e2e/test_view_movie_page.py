# TODO: Feature 4
from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_get_single_movie(test_app):
    test_movie = movie_repository.create_movie("Back to the Future", "Robert Zemeckis", 4)
    test_single_movie = movie_repository.get_movie_by_id(test_movie.movie_id)

    assert test_single_movie.movie_id == test_movie.movie_id
    assert test_single_movie.title == "Back to the Future"
    assert test_single_movie.director == "Robert Zemeckis"
    assert test_single_movie.rating == 4

