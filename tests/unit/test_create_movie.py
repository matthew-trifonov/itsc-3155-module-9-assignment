# TODO: Feature 2
from app import create_movie
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def test_create_movie():
    entered_movie_name = "Test movie name"
    entered_director_name = "Test director name"
    entered_rating = 3
    test_movie = movie_repository.create_movie(entered_movie_name,entered_director_name,entered_rating)

    assert test_movie.title == entered_movie_name
    assert test_movie.director == entered_director_name
    assert test_movie.rating == entered_rating