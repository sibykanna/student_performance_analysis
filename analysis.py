# analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Config ---
DATA_FILE = "student-mat.csv"   # put the CSV file in the same folder
OUTPUT_DIR = "visuals"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Load data ---
df = pd.read_csv(DATA_FILE, sep=';')  # this dataset uses semicolon delimiter
print("Shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())

# --- Quick look ---
print("\nFirst 5 rows:")
print(df.head())

# --- Missing values ---
print("\nMissing values per column:")
print(df.isnull().sum())

# --- Summary statistics for numeric columns ---
print("\nNumeric describe:")
print(df.describe())

# --- Create a new final grade column if not present (G3 usually final) ---
if 'G3' in df.columns:
    final_grade = 'G3'
else:
    # if dataset uses different scheme, try to compute or pick a column
    final_grade = df.select_dtypes(include=np.number).columns[-1]

# --- Basic visualizations --- #

# 1) Distribution (histogram) of final grades
plt.figure(figsize=(8,5))
sns.histplot(df[final_grade], bins=11, kde=False)
plt.title(f"Distribution of final grade ({final_grade})")
plt.xlabel("Grade")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "grade_distribution.png"))
plt.close()

# 2) Boxplot: studytime vs final grade
# studytime usually coded as 1-4 (less to more)
if 'studytime' in df.columns:
    plt.figure(figsize=(8,5))
    sns.boxplot(x='studytime', y=final_grade, data=df)
    plt.title("Study time vs Final Grade")
    plt.xlabel("Study time (1= <2h, 2=2-5h, 3=5-10h, 4=>10h)")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "studytime_vs_grade.png"))
    plt.close()

# 3) Correlation heatmap (numeric features)
plt.figure(figsize=(10,8))
num_df = df.select_dtypes(include=[np.number])
corr = num_df.corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation matrix (numeric features)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
plt.close()

print("\nSaved visuals to folder:", OUTPUT_DIR)

# --- Example simple insight: correlation with final grade ---
if final_grade in corr.columns:
    corr_with_grade = corr[final_grade].sort_values(ascending=False)
    print("\nTop correlations with final grade:")
    print(corr_with_grade.head(10))
else:
    print("\nFinal grade not found in numeric correlation matrix.")
