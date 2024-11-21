# main.py
import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
from pydantic import BaseModel, Field
import os
# Create the app
app = FastAPI()

# Load trained Pipeline
model_path = "House_price_predictor"
if os.path.exists(model_path):
    print("Model file exists.")
else:
    print("Model file does not exist.")

model = load_model(model_path)

# Create input/output pydantic models
class InputModel(BaseModel):
    area: int = Field(2640, description="Area in square feet")
    bedrooms: int = Field(2, description="Number of bedrooms")
    bathrooms: int = Field(1, description="Number of bathrooms")
    stories: int = Field(1, description="Number of stories")
    mainroad: str = Field('no', description="Is the house on the main road")
    guestroom: str = Field('no', description="Does the house have a guest room")
    basement: str = Field('no', description="Does the house have a basement")
    hotwaterheating: str = Field('no', description="Does the house have hot water heating")
    airconditioning: str = Field('no', description="Does the house have air conditioning")
    parking: int = Field(1, description="Number of parking spaces")
    prefarea: str = Field('no', description="Is the house in a preferred area")
    furnishingstatus: str = Field('furnished', description="Furnishing status of the house")

class OutputModel(BaseModel):
    prediction: float

# Define default route
@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API"}

# Define predict function
@app.post("/predict", response_model=OutputModel)
def predict(data: InputModel):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}
