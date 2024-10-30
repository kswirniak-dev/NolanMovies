from flask import Flask, render_template

app = Flask(__name__)

import requests

url = "https://api.themoviedb.org/3/movie/"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwY2QwNzlmNWYyY2Y1YmZmMDkyZmIxYzBiZmFhOTYxZiIsIm5iZiI6MTcyNzU0MjM1OC4yNTE2NjEsInN1YiI6IjY2ZjgzMWM5MzkzY2RhMWQxZGNjMjM0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KMUJ9o8Y2Nsz-ygVRHWtcT89pXr91MqtVf7u66lyACI"
}


@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    response = requests.get(url + movie_id, headers=headers)
    return render_template("movie.html", movie=response.text)


app.run(host="0.0.0.0", port=5001)
