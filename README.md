# 💳 Credit Card Fraud Detection

## 📌 Project Overview

Credit Card Fraud Detection is a Machine Learning project that identifies potentially fraudulent credit card transactions.

The project uses a Random Forest classification model to analyze transaction features and predict whether a transaction is:

- ✅ Legitimate
- 🚨 Potentially Fraudulent

A Streamlit web interface is provided so users can enter transaction details and receive a prediction.

---

## 🎯 Project Objectives

- Detect fraudulent credit card transactions using Machine Learning.
- Handle highly imbalanced transaction data.
- Compare Logistic Regression and Random Forest models.
- Optimize the classification threshold using validation data.
- Build an interactive Streamlit interface.
- Prepare the application for deployment using Streamlit Community Cloud.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn
- Google Colab
- VS Code

---

## 🤖 Machine Learning Models

### Logistic Regression

Used as a baseline classification model.

### Random Forest

Used as the main model because it performs well on tabular transaction data and can capture non-linear relationships between features.

The final Random Forest model uses a classification threshold selected using the validation set.

---

## 📊 Dataset

The project uses the `creditcard.csv` dataset.

The dataset contains:

- 284,807 transactions originally
- 30 input features
- 1 target variable (`Class`)
- Highly imbalanced classes

After removing duplicate rows:

- 283,726 transactions
- 283,253 legitimate transactions
- 473 fraudulent transactions

The features include:

- `Time`
- `V1` to `V28`
- `Amount`

The target variable is:

- `Class = 0` → Legitimate
- `Class = 1` → Fraudulent

---

## 📈 Model Evaluation

The final Random Forest model was evaluated on an untouched test set.

| Metric | Score |
|---|---:|
| Accuracy | 99.95% |
| Precision | 92.41% |
| Recall | 76.84% |
| F1 Score | 83.91% |
| PR-AUC | 80.47% |

The classification threshold was selected using validation data rather than the final test set.

---

## 🖥️ Streamlit Interface

The application provides:

1. Transaction Time input
2. Transaction Amount input
3. V1–V28 feature inputs
4. Fraud probability
5. Transaction classification
6. Visual prediction result

---

## 📁 Project Structure

```text
credit-card-fraud-detection/
│
├── app.py
├── predict.py
├── requirements.txt
├── README.md
│
└── models/
    ├── fraud_model.pkl
    ├── threshold.pkl
    └── feature_names.pkl