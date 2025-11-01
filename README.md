# Films & Musiques – Recommandation ML + Flask

##  Résumé du projet
Ce projet est une application web de recommandation de films et de musiques construite avec flask et du Machine Learning.  
Elle permet de suggérer des contenus similaires selon les préférences de l’utilisateur, grâce à des modèles entraînés localement.

Les modèles de recommandation sont sauvegardés sous forme de fichiers `.pkl` après entraînement, puis chargés automatiquement par l’application Flask.

---

##  Technologies utilisées
- Python 
- Flask  
- Pandas, NumPy  
- Scikit-learn  
- HTML / CSS / JavaScript 

---

## Entraînement des modèles

Les fichiers de modèles (`movies_model.pkl`, `music_model.pkl`) **ne sont pas inclus** dans ce dépôt à cause de la limite GitHub (100 Mo).  
Tu peux les **recréer toi-même** en suivant les étapes ci-dessous 👇

###  1. Aller dans le dossier `models/`
cd models
recréer (`movies_model.pkl`, `music_model.pkl`) 
```bash



python train_models.py
pip install -r requirements.txt
python app.py

