import requests
from nolan_movies import movies

url = "https://moviesdatabase.p.rapidapi.com/titles/search/title/"

headers = {
    "x-rapidapi-key": "e8d20accfcmsha56e9687fd72e3bp1d01fcjsnc10ecd2969a4",
    "x-rapidapi-host": "moviesdatabase.p.rapidapi.com"
}

for film in movies:
    querystring = {"exact": "true", "year": str(film['year']), "titleType": "movie"}
    response = requests.get(url + film['title'], headers=headers, params=querystring)
    print(response.json())
