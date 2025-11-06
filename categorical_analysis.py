# categorical_analysis.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

DATA_FILE = "student-mat.csv"
OUTPUT_DIR = "visuals"
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_FILE, sep=';')

# --- 1. Compare performance by gender ---
plt.figure(figsize=(6,5))
sns.boxplot(x='sex', y='G3', data=df)
plt.title("Final Grade (G3) by Gender")
plt.xlabel("Gender")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "grade_by_gender.png"))
plt.close()

# --- 2. Family support vs final grade ---
plt.figure(figsize=(6,5))
sns.boxplot(x='famsup', y='G3', data=df)
plt.title("Family Support vs Final Grade")
plt.xlabel("Family Support (yes/no)")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "famsup_vs_grade.png"))
plt.close()

# --- 3. Internet access vs final grade ---
plt.figure(figsize=(6,5))
sns.boxplot(x='internet', y='G3', data=df)
plt.title("Internet Access vs Final Grade")
plt.xlabel("Internet (yes/no)")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "internet_vs_grade.png"))
plt.close()

# --- 4. Average grade by studytime ---
avg_by_studytime = df.groupby('studytime')['G3'].mean()
print("\nAverage final grade by study time:")
print(avg_by_studytime)

# --- 5. Average grade by school ---
avg_by_school = df.groupby('school')['G3'].mean()
print("\nAverage final grade by school:")
print(avg_by_school)

print("\nSaved new visuals in 'visuals/' folder.")
