import pandas as pd
import numpy as np

# Dataset columns
columns = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "target"
]

# Load the dataset
df = pd.read_csv(
    "processed.cleveland.data",
    header=None,
    names=columns,
    na_values="?"
)

# Display first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Dataset shape
print("\nDATASET SHAPE:")
print(df.shape)

# Column names and data types
print("\nDATASET INFORMATION:")
df.info()

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Total rows and columns
print("\nTOTAL ROWS:", df.shape[0])
print("TOTAL COLUMNS:", df.shape[1])

# Statistical summary
print("\nSTATISTICAL SUMMARY:")
print(df.describe())

# Target distribution
print("\nTARGET DISTRIBUTION:")
print(df["target"].value_counts().sort_index())

# Duplicate records
print("\nDUPLICATE ROWS:", df.duplicated().sum())

# Unique values in categorical columns
print("\nUNIQUE VALUES:")
for col in ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal", "target"]:
    print(f"{col}: {df[col].unique()}")

# Heart disease target analysis

print("\n--- HEART DISEASE ANALYSIS ---")

# Count each target category
target_counts = df["target"].value_counts().sort_index()

print("\nOriginal Target Counts:")
print(target_counts)

# Convert target into two groups
df["HeartDisease"] = (df["target"] > 0).astype(int)

# Count patients in each group
print("\nHeart Disease Group Counts:")
print(
    df["HeartDisease"]
    .map({0: "No Disease", 1: "Disease Present"})
    .value_counts()
)

# Calculate percentages
print("\nHeart Disease Percentages:")
print(
    (
        df["HeartDisease"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )
)

# STEP 7: DATA CLEANING

print("\n--- DATA CLEANING ---")

# Check missing values before cleaning
print("\nMissing values before cleaning:")
print(df[["ca", "thal"]].isnull().sum())

# Fill missing categorical values using mode
for col in ["ca", "thal"]:
    mode_value = df[col].mode()[0]
    df[col] = df[col].fillna(mode_value)

# Verify missing values after cleaning
print("\nMissing values after cleaning:")
print(df[["ca", "thal"]].isnull().sum())

# Convert coded categorical columns to readable labels
df["sex_label"] = df["sex"].map({
    0: "Female",
    1: "Male"
})

df["disease_label"] = df["HeartDisease"].map({
    0: "No Disease",
    1: "Disease Present"
})

# Display cleaned data
print("\nCleaned dataset preview:")
print(df.head())

print("\nFinal dataset shape:", df.shape)

import matplotlib.pyplot as plt
import seaborn as sns

# Set chart style
sns.set_theme(style="whitegrid")

# Count patients in each group
disease_counts = df["disease_label"].value_counts()

# Create bar chart
plt.figure(figsize=(8, 5))

ax = sns.barplot(
    x=disease_counts.index,
    y=disease_counts.values
)

plt.title("Heart Disease Status Distribution", fontsize=15)
plt.xlabel("Disease Status")
plt.ylabel("Number of Records")

# Display count above each bar
for bar in ax.patches:
    ax.annotate(
        f"{int(bar.get_height())}",
        (bar.get_x() + bar.get_width() / 2, bar.get_height()),
        ha="center",
        va="bottom"
    )

plt.tight_layout()

# Save chart
plt.savefig("heart_disease_distribution.png", dpi=300)

plt.show()

# STEP 9: AGE GROUP ANALYSIS

# Create age groups
df["AgeGroup"] = pd.cut(
    df["age"],
    bins=[0, 30, 40, 50, 60, 70, 100],
    labels=[
        "Under 30",
        "30-39",
        "40-49",
        "50-59",
        "60-69",
        "70+"
    ],
    right=False
)

# Count records by age group and disease status
age_analysis = pd.crosstab(
    df["AgeGroup"],
    df["disease_label"]
)

print("\nAGE GROUP ANALYSIS:")
print(age_analysis)

# Create grouped bar chart
age_analysis.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Heart Disease Status by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.legend(title="Disease Status")
plt.tight_layout()

# Save chart
plt.savefig("age_group_analysis.png", dpi=300)

plt.show()

# STEP 10: GENDER ANALYSIS

gender_analysis = pd.crosstab(
    df["sex_label"],
    df["disease_label"]
)

print("\nGENDER ANALYSIS:")
print(gender_analysis)

# Plot grouped bar chart
gender_analysis.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Heart Disease Status by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.legend(title="Disease Status")
plt.tight_layout()

# Save chart
plt.savefig("gender_analysis.png", dpi=300)

plt.show()

# STEP 11: CHOLESTEROL ANALYSIS

print("\n--- CHOLESTEROL ANALYSIS ---")

# Overall cholesterol statistics
print("\nCholesterol Statistics:")
print(df["chol"].describe().round(2))

# Average cholesterol by disease status
cholesterol_analysis = (
    df.groupby("disease_label")["chol"]
    .agg(["mean", "median", "min", "max", "count"])
    .round(2)
)

print("\nCholesterol by Disease Status:")
print(cholesterol_analysis)

# Box plot to compare distributions
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="disease_label",
    y="chol"
)

plt.title("Cholesterol Distribution by Disease Status")
plt.xlabel("Disease Status")
plt.ylabel("Cholesterol (mg/dL)")
plt.tight_layout()

plt.savefig("cholesterol_analysis.png", dpi=300)
plt.show()

# STEP 12: EXPORT CLEANED DATA

output_path = "heart_disease_cleaned.csv"

df.to_csv(output_path, index=False)

print(f"\nCleaned dataset exported successfully: {output_path}")
