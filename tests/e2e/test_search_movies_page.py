# TODO: Feature 3
from app import app
from src.repositories.movie_repository import get_movie_repository

# Base test for search movies
def test_search_movies():
    repo = get_movie_repository()
    client = app.test_client()
    response = client.get('/movies/search')
    data = response.data.decode('utf-8')
    #Test that page is rendered
    assert response.status_code == 200
    response = client.get('/movies/search?title=The+Godfather')
    data = response.data.decode('utf-8')
    #ensures that nothing shows up if there is no movie by a certain name
    assert '<h1>Result</h1>' not in data  
    repo.create_movie('The Godfather', 'Francis Ford Coppola', 3)
    response = client.get('/movies/search?title=The+Godfather')
    data = response.data.decode('utf-8')
    #ensures that results shows up if there is a movie by a certain name
    assert '<h1>Result</h1>' in data  