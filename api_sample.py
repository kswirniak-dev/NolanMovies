from random import choice
from nolan_movies import movies
import requests


url = "https://moviesdatabase.p.rapidapi.com/titles/search/title/"

headers = {
    "x-rapidapi-key": "e8d20accfcmsha56e9687fd72e3bp1d01fcjsnc10ecd2969a4",
    "x-rapidapi-host": "moviesdatabase.p.rapidapi.com"
}

film = choice(movies)
querystring = {"exact": "true", "year": str(film['year']), "titleType": "movie"}
response = requests.get(url + film['title'], headers=headers, params=querystring)
print(response.json())
