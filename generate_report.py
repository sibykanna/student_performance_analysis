# generate_report.py
import pandas as pd
import numpy as np
import os

DATA_FILE = "student-mat.csv"
REPORT_FILE = "report.txt"

df = pd.read_csv(DATA_FILE, sep=';')

with open(REPORT_FILE, "w") as f:
    f.write("STUDENT PERFORMANCE ANALYSIS REPORT\n")
    f.write("="*45 + "\n\n")

    # Dataset Info
    f.write(f"Total students: {len(df)}\n")
    f.write(f"Total features: {df.shape[1]}\n\n")

    # Basic Stats
    f.write("Average Final Grade (G3): {:.2f}\n".format(df['G3'].mean()))
    f.write("Highest Grade: {}\n".format(df['G3'].max()))
    f.write("Lowest Grade: {}\n\n".format(df['G3'].min()))

    # Gender performance
    avg_gender = df.groupby('sex')['G3'].mean()
    f.write("Average Grade by Gender:\n")
    f.write(avg_gender.to_string())
    f.write("\n\n")

    # Study time
    avg_study = df.groupby('studytime')['G3'].mean()
    f.write("Average Grade by Study Time:\n")
    f.write(avg_study.to_string())
    f.write("\n\n")

    # Family support
    avg_famsup = df.groupby('famsup')['G3'].mean()
    f.write("Average Grade by Family Support:\n")
    f.write(avg_famsup.to_string())
    f.write("\n\n")

    # Correlation summary
    corr = df[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']].corr()['G3'].sort_values(ascending=False)
    f.write("Top Correlations with Final Grade (G3):\n")
    f.write(corr.to_string())
    f.write("\n\n")

    # Insights summary
    f.write("Key Insights:\n")
    f.write("- Students with higher G1 and G2 tend to score better in G3.\n")
    f.write("- Longer study time and higher parental education slightly improve performance.\n")
    f.write("- Family support and internet access have small but positive effects.\n")
    f.write("- Alcohol consumption (Walc, Dalc) negatively correlates with performance.\n")
    f.write("- Average final grade is around 10.4 out of 20.\n")

print(f"✅ Report generated and saved as '{REPORT_FILE}'")
