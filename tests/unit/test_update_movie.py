# TODO: Feature 5
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def test_update_movie():
    entered_movie_name = "Test movie name"
    entered_director_name = "Test director name"
    entered_rating = 3
    test_movie = movie_repository.create_movie(entered_movie_name,entered_director_name,entered_rating)
    test_movie_id = test_movie.movie_id

    new_movie_name = "New movie name"
    new_director_name = "New movie director"
    new_rating = 4

    test_movie = movie_repository.update_movie(test_movie_id,new_movie_name,new_director_name,new_rating)

    assert test_movie.title == new_movie_name
    assert test_movie.director == new_director_name
    assert test_movie.rating == new_rating
    
    assert movie_repository.get_movie_by_title(new_movie_name) == test_movie
    assert movie_repository.get_movie_by_id(test_movie_id) == test_movie 