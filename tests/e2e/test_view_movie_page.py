# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_get_single_movie(test_app):
    # Creates test movie and assigns it to test single movie.
    test_movie = movie_repository.create_movie("Back to the Future", "Robert Zemeckis", 4)
    

    # 
    response = test_app.get(f'/movies/{test_movie.movie_id}')
    data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert 'Back to the Future' in data

    response = test_app.get(f'/movies/{test_movie.movie_id}/edit')
    assert response.status_code == 200