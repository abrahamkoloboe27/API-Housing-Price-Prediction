# main.py
import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
from pydantic import BaseModel, Field
import os

# Créer l'application avec une description détaillée
app = FastAPI(
    title="🏡 API de Prédiction des Prix des Maisons",
    description="""
Bienvenue sur l'API de Prédiction des Prix des Maisons ! 🎉

Cette API vous permet de prédire les prix des maisons en fonction de diverses caractéristiques telles que la superficie, le nombre de chambres, de salles de bains et d'autres commodités. Elle utilise un modèle d'apprentissage automatique entraîné avec PyCaret pour fournir des prédictions précises.

## Endpoints

- **GET /**: Message de bienvenue.
- **POST /predict**: Prédisez le prix d'une maison.

""",
    version="1.0.0",
    contact={
        "name": "Abraham Koloboe",
        "email": "abklb27@gmail.com",
        "url": "https://github.com/abrahamkoloboe27/API-Housing-Price-Prediction"
    },
    license_info={
        "name": "Licence MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Charger le modèle entraîné
model_path = "House_price_predictor"
if os.path.exists(model_path):
    print("✅ Le fichier du modèle existe.")
else:
    print("❌ Le fichier du modèle n'existe pas.")

model = load_model(model_path)

# Créer les modèles Pydantic d'entrée/sortie
class InputModel(BaseModel):
    """
    Modèle de données d'entrée contenant les caractéristiques pour la prédiction du prix de la maison.
    """
    area: int = Field(2640, description="🏠 Superficie en pieds carrés")
    bedrooms: int = Field(2, description="🛏️ Nombre de chambres")
    bathrooms: int = Field(1, description="🛁 Nombre de salles de bains")
    stories: int = Field(1, description="🏢 Nombre d'étages")
    mainroad: str = Field('no', description="🛣️ La maison est-elle sur la route principale ('yes'/'no')")
    guestroom: str = Field('no', description="🛋️ La maison a-t-elle une chambre d'amis ('yes'/'no')")
    basement: str = Field('no', description="🏚️ La maison a-t-elle un sous-sol ('yes'/'no')")
    hotwaterheating: str = Field('no', description="🔥 La maison a-t-elle le chauffage à eau chaude ('yes'/'no')")
    airconditioning: str = Field('no', description="❄️ La maison a-t-elle la climatisation ('yes'/'no')")
    parking: int = Field(1, description="🚗 Nombre de places de parking")
    prefarea: str = Field('no', description="🌳 La maison est-elle dans une zone préférée ('yes'/'no')")
    furnishingstatus: str = Field('furnished', description="🛋️ État d'ameublement de la maison ('furnished', 'semi-furnished', 'unfurnished')")

class OutputModel(BaseModel):
    """
    Modèle de données de sortie contenant le prix prédit de la maison.
    """
    prediction: float

# Définir la route par défaut
@app.get("/")
def read_root():
    """
    Endpoint racine accueillant les utilisateurs de l'API.
    Retourne un message de bienvenue.
    """
    return {"message": "🏡 Bienvenue sur l'API de Prédiction des Prix des Maisons"}

# Définir la fonction de prédiction
@app.post("/predict", response_model=OutputModel)
def predict(data: InputModel):
    """
    Prédisez le prix d'une maison en fonction de ses caractéristiques.

    Args:
        data (InputModel): Un objet contenant les caractéristiques de la maison.

    Returns:
        dict: Un dictionnaire contenant le prix prédit de la maison.
    """
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}
