# TODO: Feature 5
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_edit_movie(test_app):
    # Creates test movie and assigns it to test single movie.
    test_movie = movie_repository.create_movie("Back to the Future", "Robert Zemeckis", 4)

    response = test_app.get(f'/movies/{test_movie.movie_id}/edit')
    assert response.status_code == 200

    response = test_app.post(f'/movies/{test_movie.movie_id}', data={
        "name": "test movie name",
        "director-name": "test director name",
        "select-rating": 3
    }, follow_redirects=True)
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert 'test movie name' in data
    assert 'test director name' in data
    

    
