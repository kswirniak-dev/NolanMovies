from random import choice

from flask import Flask, render_template

app = Flask(__name__)

import requests

url = "https://api.themoviedb.org/3/movie/"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwY2QwNzlmNWYyY2Y1YmZmMDkyZmIxYzBiZmFhOTYxZiIsIm5iZiI6MTcyNzU0MjM1OC4yNTE2NjEsInN1YiI6IjY2ZjgzMWM5MzkzY2RhMWQxZGNjMjM0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KMUJ9o8Y2Nsz-ygVRHWtcT89pXr91MqtVf7u66lyACI"
}

movie_ids = [804706, 456684, 43629, 11660, 77, 320, 272, 1124, 155, 27205,
             49026, 157336, 352114, 374720, 577922, 872585]


@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    response = requests.get(url + movie_id, headers=headers)
    return render_template("movie.html", movie=response.json())


@app.route("/")
def index():
    response = requests.get(url + str(choice(movie_ids)), headers=headers)
    return render_template("movie.html", movie=response.json())


app.run(host="0.0.0.0", port=5001)
