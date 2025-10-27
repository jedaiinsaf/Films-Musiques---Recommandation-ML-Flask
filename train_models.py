import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# ---- FILMS ----
movies = pd.read_csv("data/movies.csv")
tfidf_movies = TfidfVectorizer(stop_words="english")
tfidf_matrix_movies = tfidf_movies.fit_transform(movies['genres'])
cosine_sim_movies = cosine_similarity(tfidf_matrix_movies, tfidf_matrix_movies)

with open("models/movies_model.pkl", "wb") as f:
    pickle.dump({"movies": movies, "cosine_sim": cosine_sim_movies}, f)

print("✅ Modèle films créé")

# ---- MUSIQUES ----
songs = pd.read_csv("data/songs.csv")
songs["combined"] = songs["artist"] + " " + songs["genre"]
tfidf_songs = TfidfVectorizer(stop_words="english")
tfidf_matrix_songs = tfidf_songs.fit_transform(songs["combined"])
cosine_sim_songs = cosine_similarity(tfidf_matrix_songs, tfidf_matrix_songs)

with open("models/music_model.pkl", "wb") as f:
    pickle.dump({"songs": songs, "cosine_sim": cosine_sim_songs}, f)

print("✅ Modèle musiques créé")
