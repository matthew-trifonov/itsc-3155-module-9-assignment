# TODO: Feature 1
from app import app
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_list_all_movies():

    client = app.test_client()
    response = client.get('/movies')
    assert response.status_code == 200

    data = response.data.decode('utf-8')
    assert 'All Movies' in data

def test_list_all_movies_with_data():
    repo = get_movie_repository()

    test_movies = [
        Movie(1, 'The Shawshank Redemption', 'Frank Darabont', 9.3),
        Movie(2, 'The Godfather', 'Francis Ford Coppola', 9.2),
        Movie(3, 'The Godfather: Part II', 'Francis Ford Coppola', 9.0),
    ]
    for movie in test_movies:
        repo.create_movie(movie.title, movie.director, movie.rating)
    
    client = app.test_client()
    response = client.get('/movies')
    assert response.status_code == 200

    data = response.data.decode('utf-8')
    repo.get_all_movies()


    for id in repo.get_all_movies().keys():
        assert repo.get_movie_by_id(id).title in data
        assert repo.get_movie_by_id(id).director in data
        assert str(repo.get_movie_by_id(id).rating) in data

def test_list_all_movies_without_data():
    repo = get_movie_repository()
    repo.clear_db()
    
    client = app.test_client()
    response = client.get('/movies')
    assert response.status_code == 200

    data = response.data.decode('utf-8')
    assert '<td>' not in data
    