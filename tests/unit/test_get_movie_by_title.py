# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_title():
    # Create a new blank movie repository instance and clear
    repo = get_movie_repository()
    repo.clear_db()

    # Add some movies to the repository
    repo.create_movie('The Shawshank Redemption', 'Frank Darabont', 9.3)
    repo.create_movie('The Godfather', 'Francis Ford Coppola', 9.2)

    movie1 = repo.get_movie_by_title('The Godfather')
    assert movie1.title == 'The Godfather'
    assert repo.get_movie_by_title('Harry Potter') == None

