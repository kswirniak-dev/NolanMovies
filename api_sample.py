import requests
from nolan_movies import movies

url = "https://moviesdatabase.p.rapidapi.com/titles/search/title/"

headers = {
    "x-rapidapi-key": "e8d20accfcmsha56e9687fd72e3bp1d01fcjsnc10ecd2969a4",
    "x-rapidapi-host": "moviesdatabase.p.rapidapi.com"
}

for title in movies:
    response = requests.get(url + title, headers=headers)
    print(response.json())
