import pandas as pd

# Load dataset
df = pd.read_csv("dataset/students.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset shape
print("\nShape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Data types
print("\nData types:")
print(df.dtypes)

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Statistical information
print("\nStatistical summary:")
print(df.describe())