from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Charger modèles
with open("models/movies_model.pkl", "rb") as f:
    movie_data = pickle.load(f)

with open("models/music_model.pkl", "rb") as f:
    song_data = pickle.load(f)

# Fonction de recommandation
def recommend_movie(title, n=5):
    try:
        idx = movie_data["movies"][movie_data["movies"]["title"].str.contains(title, case=False, regex=False)].index[0]
        sim_scores = list(enumerate(movie_data["cosine_sim"][idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
        indices = [i[0] for i in sim_scores]
        return movie_data["movies"]["title"].iloc[indices].tolist()
    except:
        return ["Film introuvable"]

def recommend_song(title, n=5):
    try:
        idx = song_data["songs"][song_data["songs"]["title"].str.contains(title, case=False, regex=False)].index[0]
        sim_scores = list(enumerate(song_data["cosine_sim"][idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
        indices = [i[0] for i in sim_scores]
        return song_data["songs"]["title"].iloc[indices].tolist()
    except:
        return ["Chanson introuvable"]

# Routes
@app.route("/", methods=["GET", "POST"])
def home():
    recommendations_movies = []
    recommendations_songs = []
    film = ""
    song = ""
    if request.method == "POST":
        film = request.form.get("film")
        song = request.form.get("song")
        if film:
            recommendations_movies = recommend_movie(film)
        if song:
            recommendations_songs = recommend_song(song)
    return render_template("home.html", 
                           film=film, 
                           song=song,
                           recommendations_movies=recommendations_movies,
                           recommendations_songs=recommendations_songs)

if __name__ == "__main__":
    app.run(debug=True)
