# TODO: Feature 2

from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_create_movie(test_app):
    test_movie = movie_repository.create_movie("Movie name","Movie director", 3)
    response = test_app.post('/movies', data={
        "name": "test movie name",
        "director-name": "test director name",
        "select-rating": 3
    }, follow_redirects=True)

    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    #uncomment after succesful implementation of movies page
    #assert 'test movie name' in data
    #assert 'test director name' in data
    #assert 'test rating' in data

def test_create_movie_validation(test_app):
    response = test_app.post('/movies')
    assert response.status_code == 400   

#add test to assert there are no movies to display