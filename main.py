from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import numpy as np
import joblib
import os

app = FastAPI(title="E-Doctor API")

if os.path.isdir("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ─── Load Models ────────────────────────────────────────────────────────────
MODEL_PATH = "models"

def load_model(name):
    path = os.path.join(MODEL_PATH, f"{name}.sav")
    if os.path.exists(path):
        return joblib.load(path)
    return None

diabetes_model  = load_model("Diabetes")
heart_model     = load_model("Heart")
parkinsons_model = load_model("Parkinsons")

# ─── Schemas ────────────────────────────────────────────────────────────────
class DiabetesInput(BaseModel):
    pregnancies: float
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    dpf: float
    age: float

class HeartInput(BaseModel):
    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

class ParkinsonsInput(BaseModel):
    fo: float; fhi: float; flo: float
    jitter: float; jitter_abs: float
    rap: float; ppq: float; ddp: float
    shimmer: float; shimmer_db: float
    apq3: float; apq5: float; apq: float; dda: float
    nhr: float; hnr: float; rpde: float; dfa: float
    spread1: float; spread2: float; d2: float; ppe: float

# ─── Page Route ─────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ─── API Endpoints ──────────────────────────────────────────────────────────
@app.post("/predict/diabetes")
async def predict_diabetes(data: DiabetesInput):
    if diabetes_model is None:
        return {"error": "Model not loaded"}
    arr = np.array([[data.pregnancies, data.glucose, data.blood_pressure,
                     data.skin_thickness, data.insulin, data.bmi,
                     data.dpf, data.age]])
    result = diabetes_model.predict(arr)[0]
    return {
        "prediction": int(result),
        "label": "Diabetic" if result == 1 else "Healthy",
        "status": "positive" if result == 1 else "negative"
    }

@app.post("/predict/heart")
async def predict_heart(data: HeartInput):
    if heart_model is None:
        return {"error": "Model not loaded"}
    arr = np.array([[data.age, data.sex, data.cp, data.trestbps,
                     data.chol, data.fbs, data.restecg, data.thalach,
                     data.exang, data.oldpeak, data.slope, data.ca, data.thal]])
    result = heart_model.predict(arr)[0]
    return {
        "prediction": int(result),
        "label": "Heart Disease Detected" if result == 1 else "Healthy Heart",
        "status": "positive" if result == 1 else "negative"
    }

@app.post("/predict/parkinsons")
async def predict_parkinsons(data: ParkinsonsInput):
    if parkinsons_model is None:
        return {"error": "Model not loaded"}
    arr = np.array([[data.fo, data.fhi, data.flo, data.jitter, data.jitter_abs,
                     data.rap, data.ppq, data.ddp, data.shimmer, data.shimmer_db,
                     data.apq3, data.apq5, data.apq, data.dda, data.nhr, data.hnr,
                     data.rpde, data.dfa, data.spread1, data.spread2, data.d2, data.ppe]])
    result = parkinsons_model.predict(arr)[0]
    return {
        "prediction": int(result),
        "label": "Parkinson's Detected" if result == 1 else "No Parkinson's",
        "status": "positive" if result == 1 else "negative"
    }
