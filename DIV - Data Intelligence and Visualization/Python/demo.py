import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = "threadora_boutique_data.csv"
df = pd.read_csv(file_path)

# ===== Data Cleaning =====

# Check for missing values
print("\n => Missing Values Before Cleaning:\n")
print(df.isnull().sum())

# Fill missing numeric values with the column median
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Fill missing categorical values with the column mode
categorical_cols = df.select_dtypes(include=[object]).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Confirm cleaning
print("\n => Missing Values After Cleaning:\n")
print(df.isnull().sum())

# Preview cleaned data
deal = LabelEncoder()
df['Deal_Offered'] = deal.fit_transform(df['Deal_Offered'])

print("\n => Cleaned Data Preview:\n")
print(df)