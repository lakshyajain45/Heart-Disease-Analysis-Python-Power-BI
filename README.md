# ❤️ Heart Disease Analysis | Python & Power BI

## 📌 Project Overview

This project focuses on analyzing heart disease data to identify patterns, trends, and key factors associated with heart disease using Python and Power BI.

The objective is to transform raw healthcare data into meaningful insights through data cleaning, exploratory data analysis (EDA), and interactive visualization.

---

## 🎯 Objectives

- Analyze heart disease data.
- Clean and preprocess the dataset using Python.
- Explore relationships between age, gender, cholesterol, maximum heart rate, and heart disease.
- Create an interactive Power BI dashboard.
- Identify important trends and insights from the data.

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **Matplotlib**
- **Power BI**
- **DAX**
- **Microsoft Excel / CSV**

---

## 📂 Dataset

The project uses the Cleveland Heart Disease dataset.

### Dataset Information

- Total Records: **303**
- Total Attributes: **14 original attributes**
- Target Variable: Heart Disease

The dataset was cleaned and transformed before performing analysis.

---

## 🧹 Data Cleaning & Preprocessing

Data preprocessing was performed using Python.

Key steps:

- Identified missing values represented by `?`.
- Converted missing values into `NaN`.
- Handled missing values in `ca` and `thal` using mode imputation.
- Checked and removed duplicate records.
- Created a binary `HeartDisease` column.
- Created categorical labels for gender and disease status.
- Created age groups for analysis.
- Verified the final dataset for missing values and duplicates.

### Final Dataset

- Rows: **303**
- Columns: **18**
- Missing Values: **0**
- Duplicate Records: **0**

---

## 📊 Exploratory Data Analysis

The analysis explored:

- Heart disease distribution.
- Age-wise heart disease distribution.
- Gender-wise analysis.
- Cholesterol levels.
- Maximum heart rate.
- Relationship between health parameters and heart disease.

---

## 📈 Power BI Dashboard

The Power BI report consists of **3 pages**:

### 1️⃣ Dashboard
 ## 📊 Dashboard Preview
![Heart Disease Analysis Dashboard](Gallery/dashboard_screenshot.png)

An interactive dashboard containing:

- Total Records
- Disease Present
- No Disease
- Average Age
- Heart Disease Distribution
- Age Group Analysis
- Gender Analysis
- Cholesterol vs Maximum Heart Rate

Interactive filters:

- Gender
- Age Group
- Disease Status

### 2️⃣ Key Insights

A dedicated page highlighting important observations and findings from the analysis.

### 3️⃣ Recommendations & Conclusion

A summary of analytical findings, recommendations, limitations, and the conclusion of the project.

---

## 🔍 Key Insights

- **303** records were analyzed.
- **139 individuals (45.87%)** had heart disease.
- **164 individuals (54.13%)** were classified as having no heart disease.
- The average age of individuals in the dataset was approximately **54.44 years**.
- Approximately **68%** of the dataset consisted of males.
- The average cholesterol level among individuals with heart disease was approximately **251.47**.
- The average maximum heart rate among individuals with heart disease was approximately **139.26 BPM**.
- Age, gender, cholesterol, and maximum heart rate were explored to understand their relationship with heart disease.

---

## 📐 DAX Measures

Some important measures created in Power BI:

DAX
Total Records = COUNTROWS('heart_disease_cleaned')

Disease Present =
CALCULATE(
    COUNTROWS('heart_disease_cleaned'),
    'heart_disease_cleaned'[HeartDisease] = 1
)

No Disease =
CALCULATE(
    COUNTROWS('heart_disease_cleaned'),
    'heart_disease_cleaned'[HeartDisease] = 0
)

Average Age = AVERAGE('heart_disease_cleaned'[age])

Disease Percentage =
DIVIDE([Disease Present], [Total Records], 0)

📁 Project Structure:-
Heart-Disease-Analysis-Python-Power-BI/
│
├── Dataset/
│   └── heart_disease_cleaned.csv
│
├── Python/
│   └── 01_data_exploration.py
│
├── PowerBI/
│   └── Heart_Disease_Analysis.pbix
│
├── Dashboard/
│   └── dashboard_screenshot.png
│
├── Documentation/
│   └── Heart_Disease_Analysis_Report.pdf
│
└── README.md




