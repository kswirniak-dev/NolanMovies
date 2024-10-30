from random import choice
import requests
from nolan_movies import movies

url = "https://api.themoviedb.org/3/search/movie?"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwY2QwNzlmNWYyY2Y1YmZmMDkyZmIxYzBiZmFhOTYxZiIsIm5iZiI6MTcyNzU0MjM1OC4yNTE2NjEsInN1YiI6IjY2ZjgzMWM5MzkzY2RhMWQxZGNjMjM0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KMUJ9o8Y2Nsz-ygVRHWtcT89pXr91MqtVf7u66lyACI"
}


def find_all_nolan_movie_ids():
    movies_ids = []
    for film in movies:
        response = get_search_result_by_title_and_year(film)
        movie_id = get_single_movie_id_from_search_result(response.json(), film)
        if movie_id is not None:
            movies_ids.append(movie_id)
    return movies_ids


def get_search_result_by_title_and_year(film):
    querystring = {"query": film["title"], "include_adult": "false", "year": str(film["year"])}
    return requests.get(url, headers=headers, params=querystring)


def get_single_movie_id_from_search_result(search_result, film):
    if search_result is None:
        raise TypeError
    if search_result == {}:
        raise ValueError
    for result in search_result["results"]:
        if result["original_title"] == film["title"] and result["release_date"][:4] == str(film["year"]):
            return result["id"]

