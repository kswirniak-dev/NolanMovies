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
        querystring = {"query": film["title"], "include_adult": "false", "year": str(film["year"])}
        response = requests.get(url, headers=headers, params=querystring)
        for result in response.json()["results"]:
            if result["original_title"] == film["title"] and result["release_date"][:4] == str(film["year"]):
                movies_ids.append(result["id"])
    return movies_ids


nolan_movies_ids = find_all_nolan_movie_ids()
print(nolan_movies_ids)
print(len(nolan_movies_ids))
