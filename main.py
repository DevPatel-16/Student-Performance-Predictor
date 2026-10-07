import joblib
import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse


# Create FastAPI application
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load trained model
model = joblib.load("student_model.pkl")


# Input data structure
class StudentData(BaseModel):
    study_hours: float = Field(ge=1, le=10)
    attendance: float = Field(ge=50, le=100)
    previous_score: float = Field(ge=40, le=100)
    assignment_score: float = Field(ge=40, le=100)
    sleep_hours: float = Field(ge=4, le=12)
    participation: float = Field(ge=1, le=10)


# Home endpoint
@app.get("/")
def home():
    return FileResponse("frontend/index.html")


# Prediction endpoint
@app.post("/predict")
def predict(data: StudentData):

    student = pd.DataFrame({
        "study_hours": [data.study_hours],
        "attendance": [data.attendance],
        "previous_score": [data.previous_score],
        "assignment_score": [data.assignment_score],
        "sleep_hours": [data.sleep_hours],
        "participation": [data.participation]
    })

    prediction = model.predict(student)

    prediction = max(0, min(100, prediction[0]))

    return {
        "predicted_final_score": round(float(prediction), 2)
    }