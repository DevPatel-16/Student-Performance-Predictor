import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("dataset/students.csv")

# Features
X = df[
    [
        "study_hours",
        "attendance",
        "previous_score",
        "assignment_score",
        "sleep_hours",
        "participation"
    ]
]

# Target
y = df["final_score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train shape:")
print(X_train.shape)

print("\nX_test shape:")
print(X_test.shape)

print("\ny_train shape:")
print(y_train.shape)

print("\ny_test shape:")
print(y_test.shape)