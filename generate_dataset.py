import pandas as pd
import numpy as np


# Make results reproducible
np.random.seed(42)

# Number of students
n = 500


# Generate student features

study_hours = np.random.uniform(1, 10, n)

attendance = np.random.uniform(50, 100, n)

previous_score = np.random.uniform(40, 95, n)

assignment_score = np.random.uniform(40, 100, n)

sleep_hours = np.random.uniform(4, 9, n)

participation = np.random.uniform(1, 10, n)


# Generate some random noise
noise = np.random.normal(0, 4, n)


# Calculate final score
final_score = (
    2.5 * study_hours
    + 0.25 * attendance
    + 0.35 * previous_score
    + 0.20 * assignment_score
    + 1.5 * sleep_hours
    + 1.5 * participation
    + noise
)


# Keep scores between 0 and 100
final_score = np.clip(final_score, 0, 100)


# Create DataFrame
df = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "previous_score": previous_score,
    "assignment_score": assignment_score,
    "sleep_hours": sleep_hours,
    "participation": participation,
    "final_score": final_score
})


# Save dataset
df.to_csv("dataset/students.csv", index=False)


print("Dataset generated successfully!")
print("\nShape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())