import joblib
import pandas as pd


# Load trained model
model = joblib.load("student_model.pkl")


# Get student information
study_hours = float(input("Enter study hours per day (1-10): "))
attendance = float(input("Enter attendance percentage (0-100): "))
previous_score = float(input("Enter previous score (0-100): "))
assignment_score = float(input("Enter assignment score (0-100): "))
sleep_hours = float(input("Enter average sleep hours (0-24): "))
participation = float(input("Enter participation score (1-10): "))


# Validate input
if not 0 <= study_hours <= 24:
    print("Invalid study hours.")
    exit()

if not 0 <= attendance <= 100:
    print("Invalid attendance.")
    exit()

if not 0 <= previous_score <= 100:
    print("Invalid previous score.")
    exit()

if not 0 <= assignment_score <= 100:
    print("Invalid assignment score.")
    exit()

if not 0 <= sleep_hours <= 24:
    print("Invalid sleep hours.")
    exit()

if not 1 <= participation <= 10:
    print("Invalid participation score.")
    exit()


# Create DataFrame
student = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance],
    "previous_score": [previous_score],
    "assignment_score": [assignment_score],
    "sleep_hours": [sleep_hours],
    "participation": [participation]
})


# Make prediction
prediction = model.predict(student)


# Keep prediction between 0 and 100
prediction = max(0, min(100, prediction[0]))


# Display result
print("\nPredicted Final Score:", round(prediction, 2))