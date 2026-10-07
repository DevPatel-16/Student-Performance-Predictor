import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset/students.csv")

# Study hours vs final score
plt.scatter(df["study_hours"], df["final_score"])

plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Study Hours vs Final Score")

plt.show()

plt.scatter(df["attendance"], df["final_score"])

plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score")

plt.show()

plt.scatter(df["previous_score"], df["final_score"])

plt.xlabel("Previous Score")
plt.ylabel("Final Score")
plt.title("Previous Score vs Final Score")

plt.show()