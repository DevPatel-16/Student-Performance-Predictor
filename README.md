# Student Performance Predictor

An end-to-end Machine Learning web application that predicts a student's final score based on academic and personal performance factors.

## Project Overview

This project uses Linear Regression to predict a student's final score using:

- Study hours
- Attendance
- Previous score
- Assignment score
- Sleep hours
- Participation

The trained machine learning model is integrated with a FastAPI backend and an HTML/CSS/JavaScript frontend.

## Features

- Student performance prediction
- Linear Regression model
- Train/test split
- Model evaluation using MAE, MSE, RMSE and R²
- Model coefficient analysis
- Saved trained model using Joblib
- FastAPI REST API
- Input validation using Pydantic
- Interactive web frontend
- Performance classification
- Synthetic dataset generation

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- FastAPI
- Pydantic
- HTML
- CSS
- JavaScript


## Project Structure

```text
Student-Performance-Predictor/
│
├── dataset/
│   └── students.csv
│
├── frontend/
│   └── index.html
│
├── generate_dataset.py
├── test_dataset.py
├── visualize.py
├── prepare_data.py
├── train_model.py
├── predict.py
├── main.py
├── student_model.pkl
├── requirements.txt
├── README.md
└── .gitignore