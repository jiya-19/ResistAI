# ResistAI
## AI-Powered Antibiotic Resistance Prediction and Decision Support System

---

## Project Overview

**ResistAI** is a machine learning-based healthcare prototype designed to predict antibiotic resistance patterns and provide AI-assisted decision support using bacterial isolate and susceptibility-related data.

Antimicrobial resistance (AMR) is a major global health challenge, and timely identification of resistance patterns is essential for effective treatment planning. ResistAI demonstrates how AI can assist in analyzing susceptibility data, predicting resistance outcomes, and visualizing resistance trends through an interactive web application.


> ⚠️ **Disclaimer:** This project is developed for educational, research, and hackathon purposes only. It is **not** intended for real-world clinical diagnosis, treatment planning, or prescription decisions.

---

## Tech Stack & Tools

### **Frontend / App**
- **Streamlit** – interactive web application framework
- **Custom CSS** – UI styling and layout enhancements

### **Backend / Data Processing**
- **Python**
- **Pandas**
- **NumPy**

### **Machine Learning**
- **Scikit-learn**
- **Joblib**

### **Data Visualization**
- **Plotly**
- **Matplotlib / Seaborn**

### **Development Tools**
- **Git**
- **GitHub**
- **Jupyter Notebook** 

---

## Features

### **1. Dataset Upload & Preview**
- Upload CSV files for training and testing
- Preview dataset rows, columns, and summary information
- Identify possible target and feature columns

### **2. Data Preprocessing**
- Handles missing values
- Encodes categorical variables
- Normalizes resistance labels
- Prepares data for model training and prediction

### **3. Model Training**
- Train a machine learning classification model on susceptibility-style data
- Automatically saves trained model and preprocessing pipeline

### **4. Resistance Prediction**
Predicts whether a bacterial isolate is:
- **Resistant**
- **Susceptible**
- **Intermediate**

### **5. Confidence Scores**
- Displays model confidence / probability for predictions

### **6. Performance Evaluation**
Displays:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

### **7. Batch Prediction**
- Upload new CSV files for bulk resistance prediction
- Download prediction results

### **8. Explainable AI Insights**
- Shows feature importance
- Helps users understand which factors influence predictions

### **9. Resistance Analytics Dashboard**
Interactive visualizations for:
- resistance class distribution
- antibiotic-wise resistance frequency
- species-wise trends
- resistance heatmaps

### **10. AI-Assisted Recommendation Layer**
- Suggests potentially effective antibiotics based on predicted susceptibility patterns

> ⚠️ These outputs are educational decision-support suggestions only and should not be considered medical advice.

---

## Installation / Setup Instructions

### **1. Clone the repository**
```bash
git clone https://github.com/jiya-19/ResistAI.git
cd ResistAI
```

### **2. Create a virtual environment (recommended)**

#### **Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

#### **macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run the application**

```bash
streamlit run app.py
```

The application should now open in your browser.

---

## How to Use

### **Option 1 – Use Sample Dataset**

* Launch the app
* Load the built-in sample dataset
* Explore dashboard, train model, and test predictions

### **Option 2 – Upload Your Own CSV**

* Upload a susceptibility-style CSV file
* Select target and feature columns
* Train the model
* Run predictions

### **Option 3 – Manual Prediction**

* Enter isolate or feature values manually
* Get resistance prediction and confidence score

### **Option 4 – Batch Prediction**

* Upload new input data
* Generate predictions for multiple records
* Download the results as CSV

---

## Technical Workflow

The ResistAI system follows the workflow below:

### **Step 1 – Data Input**

Users can:

* upload a CSV dataset, or
* use the built-in sample dataset

### **Step 2 – Data Preprocessing**

The system performs:

* missing value handling
* categorical encoding
* feature selection
* target label normalization
* train/test splitting

### **Step 3 – Model Training**

The model is trained to classify susceptibility outcomes into:

* Resistant
* Susceptible
* Intermediate

### **Step 4 – Model Evaluation**

The system evaluates model performance using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### **Step 5 – Prediction**

Users can:

* manually enter feature values, or
* upload new data for batch prediction

### **Step 6 – Explainability**

The app highlights the most important factors contributing to predicted resistance.

### **Step 7 – Analytics & Decision Support**

The system generates:

* resistance dashboards
* class distribution insights
* antibiotic trend analysis
* AI-assisted educational recommendations

---

## Project Structure

```bash
ResistAI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
│
├── assets/
│   └── styles.css
│
├── data/
│   └── sample_dataset.csv
│
├── models/
│   ├── trained_model.pkl
│   ├── preprocessor.pkl
│   └── metadata.json
│
├── notebooks/
│   └── experimentation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   ├── explain.py
│   ├── recommend.py
│   ├── dashboard.py
│   ├── utils.py
│   └── validators.py
│
└── .streamlit/
    └── config.toml
```

---

## Future Scope

ResistAI can be extended further by:

* integrating real antimicrobial resistance datasets
* adding genomic or laboratory data support
* improving model explainability with SHAP
* building clinician/lab-friendly workflows
* deploying as a scalable healthcare decision-support platform

---

## Disclaimer

**ResistAI is strictly an educational and hackathon prototype.**

It is **not**:

* a medical device
* a diagnostic tool
* a prescription system
* a substitute for laboratory susceptibility testing or clinical expertise

All predictions and recommendations are for **demonstration purposes only**.

---

## 📄 License

* MIT License — This project is for educational / prototype / hackathon demonstration purposes.
