# API-Housing-Price-Prediction
### Documentation pour le Repository de l'API

#### 📖 Description du Projet
Ce repository contient le code source de l'API de prédiction des prix des maisons utilisant FastAPI. Cette API prend en entrée diverses caractéristiques d'une maison et renvoie le prix prédit.

#### 🚀 Installation
Suivez les étapes ci-dessous pour installer et exécuter l'API en local.

1. **Cloner le Repository :**
   ```bash
   git clone https://github.com/abrahamkoloboe27/API-Housing-Price-Prediction.git
   cd API-Housing-Price-Prediction
   ```

2. **Créer et Activer un Environnement Virtuel :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

3. **Installer les Dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l'API :**
   ```bash
   uvicorn api:app --reload
   ```

#### 📝 Utilisation
Une fois l'API en cours d'exécution, vous pouvez envoyer des requêtes POST à l'endpoint `/predict` avec les caractéristiques de la maison pour obtenir une prédiction de prix.

#### 📄 Exemple de Requête
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{
    "feature1": value1,
    "feature2": value2,
    ...
}'
```

#### 🔗 Liens Utiles
- [Documentation de FastAPI](https://fastapi.tiangolo.com/)
- [Repository GitHub](https://github.com/abrahamkoloboe27/API-Housing-Price-Prediction)

#### 📧 Contact
Pour toute question ou suggestion, veuillez contacter Abraham KOLOBOE à l'adresse email [abklb27@gmail.com](mailto:abklb27@gmail.com).
