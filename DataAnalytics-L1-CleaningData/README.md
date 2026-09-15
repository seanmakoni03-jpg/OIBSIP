# LinkedIn Job Dataset Cleaning & Preprocessing (Task 3)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-orange.svg)](https://pandas.pydata.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seanmakoni03-jpg/OIBSIP/blob/main/OIBSIP_Data_Analytics_L1_Task3_Cleaning_Data.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Data Quality Report Summary](#-data-quality-report-summary)
- [Cleaning Methodology & Strategy](#-cleaning-methodology--strategy)
- [Before vs. After Comparison](#-before-vs-after-comparison)
- [Project Structure](#-project-structure)
- [Getting Started & Installation](#-getting-started--installation)
- [Author](#-author)

---

## 🚀 Project Overview
This repository contains the complete data cleaning, sanitization, and preprocessing pipeline for **Task 3** of the **Oasis Infobyte Data Analytics Internship (OIBSIP)**[cite: 3]. The project takes raw, unformatted web-scraped recruitment records (`linkdin_Job_data.csv`)[cite: 3] and systematically transforms them into an analysis-ready dataset (`cleaned_linkedin_jobs.csv`)[cite: 3].

Using Python (`Pandas` and `NumPy`)[cite: 3], this workflow resolves structural anomalies, purges redundant columns, removes exact duplicates, standardizes inconsistent text attributes, and handles numerical outliers.

---

## 📊 Data Quality Report Summary
An initial inspection of the raw dataset revealed several key structural issues[cite: 3]:
1. **Dimensions**: 7,927 rows and 16 columns[cite: 3].
2. **Completely Empty Columns**: `company_id` and `Column1` contained 100% missing values (7,927 nulls) offering zero analytical utility[cite: 3].
3. **High-Missingness Fields**: Columns like `alumni` (3,069 missing), `linkedin_followers` (3,113 missing), and `Hiring_person` / `hiring_person_link` (2,207 missing) exhibited high null rates typical of web scraping[cite: 3].
4. **Duplicates**: 79 exact duplicate rows were detected across the dataframe[cite: 3].
5. **Type Inconsistencies**: Key numeric and identifier fields required string extraction, parsing, and type casting[cite: 3].

---

## 🛠️ Cleaning Methodology & Strategy
The data sanitization pipeline followed these rigorous steps[cite: 3]:
* **Column & Row Dropping**: Dropped redundant 100% null columns (`company_id`, `Column1`) and purged rows missing crucial identifiers like `job`, `location`, or `company_name` (~35 rows) to prevent analytical skew[cite: 3].
* **Missing Value Imputation**: Imputed missing categorical variables in `work_type` and `full_time_remote` with `'Not Specified'` to preserve valuable sample size[cite: 3].
* **Duplicate Removal**: Identified and removed all exact row duplicates[cite: 3].
* **Text Standardization**: Cleaned string variations, normalized capitalization, and stripped whitespaces for fields like `work_type`[cite: 3].
* **Numerical Extraction & Outlier Capping**: Extracted clean numeric digits from applicant count strings and applied the Interquartile Range (IQR) method to cap extreme high-end outliers[cite: 3].

---

## 📈 Before vs. After Comparison

| Metric | Before Cleaning | After Cleaning |
| :--- | :---: | :---: |
| **Row Count** | 7,927[cite: 3] | 7,813[cite: 3] |
| **Duplicate Rows** | 79[cite: 3] | 0[cite: 3] |
| **Total Missing Values** | 27,238[cite: 3] | 10,642[cite: 3] |
| **Dtype Accuracy** | Unoptimized / Mixed Strings[cite: 3] | Fully Standardized & Typed[cite: 3] |

---

## 📁 Project Structure

```text
├── OIBSIP_Data_Analytics_L1_Task3_Cleaning_Data.ipynb # Data cleaning Jupyter Notebook
├── cleaned_linkedin_jobs.csv                             # Output sanitized dataset
├── README.md                                             # Project Documentation
└── requirements.txt                                      # Python dependencies
```