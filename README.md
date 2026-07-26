# 🚀 Customer Support Intent Classification using Machine Learning

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://customer-support-intent.streamlit.app/)

## 🌐 Live Demo

👉 **Try the application here:**  
**https://customer-support-intent.streamlit.app/**

---

## 📌 Overview

Customer support teams receive thousands of customer queries every day. Manually categorizing these queries is time-consuming and inefficient. This project builds a **Natural Language Processing (NLP)** based intent classification system that automatically predicts the intent behind customer support messages.

The project demonstrates a complete end-to-end Machine Learning workflow, from data preprocessing to model deployment using **Streamlit**.

---

## 🎯 Project Objective

The objective of this project is to automatically classify customer support messages into predefined intent categories using Machine Learning.

This application can help organizations:

- 📌 Automate customer query categorization
- ⚡ Reduce manual effort
- 🚀 Improve ticket routing
- 💬 Enhance customer support efficiency

---

## 📂 Dataset

**Dataset:** Banking77

The Banking77 dataset contains over **10,000 customer support queries** classified into **77 banking-related intent categories**.

Example intents include:

- Card Arrival
- Cash Withdrawal
- Refund Issues
- Card Payment
- Cash Deposit
- Beneficiary Problems
- Exchange Rate
- Transfer Issues

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Data Processing
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn

### NLP
- TF-IDF Vectorization

### Models
- Logistic Regression
- Multinomial Naive Bayes
- Linear Support Vector Machine (Linear SVM)

### Deployment
- Streamlit

### Model Serialization
- Joblib

---

# 🔄 Project Workflow

```text
Customer Message
        │
        ▼
Text Preprocessing
        │
        ▼
TF-IDF Feature Extraction
        │
        ▼
Machine Learning Models
        │
        ▼
Intent Prediction
```

---

# 📊 Exploratory Data Analysis (EDA)

The dataset was analyzed to understand:

- Dataset structure
- Missing values
- Number of intent classes
- Intent distribution
- Text length distribution

Visualizations were created using **Matplotlib** and **Seaborn**.

---

# 📝 Text Preprocessing

The following preprocessing techniques were applied:

- Convert text to lowercase
- Remove special characters
- Remove punctuation
- Remove numbers
- Generate cleaned text

---

# 🔢 Feature Engineering

## TF-IDF Vectorization

TF-IDF (Term Frequency–Inverse Document Frequency) converts customer messages into numerical vectors while assigning higher importance to informative words and reducing the weight of common words.

---

# 🤖 Machine Learning Models

Three machine learning models were trained and compared.

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **83.21%** |
| Multinomial Naive Bayes | **76.13%** |
| **Linear SVM** | **85.16%** ✅ |

Linear SVM achieved the highest accuracy and was selected as the final model.

---

# 📈 Model Evaluation

The models were evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-score
- Classification Report
- Confusion Matrix
- 5-Fold Cross Validation

---

# 🚀 Deployment

The trained **Linear SVM** model and **TF-IDF Vectorizer** were serialized using **Joblib** and deployed using **Streamlit Community Cloud**, allowing users to classify customer support messages in real time. :contentReference[oaicite:0]{index=0}

**Live Application**

👉 https://customer-support-intent.streamlit.app/

---

# 📁 Project Structure

```text
Customer-Support-Intent-Classifier/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── models/
│   ├── best_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── intent_classifier.ipynb
│
└── cus_image.png
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/belindacarolam04/Customer-Support-Intent-Classifier.git
```

Move into the project folder:

```bash
cd Customer-Support-Intent-Classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 💡 Future Improvements

- Implement BERT-based intent classification
- Develop a FastAPI backend
- Dockerize the application
- Deploy on AWS, Azure, or Google Cloud
- Add multilingual support
- Integrate with real-world customer support platforms
- Build a React frontend

---

# 📚 Learning Outcomes

This project helped me gain practical experience in:

- Natural Language Processing (NLP)
- Text preprocessing
- TF-IDF feature engineering
- Machine Learning model comparison
- Hyperparameter tuning
- Model evaluation
- Streamlit deployment
- GitHub project management

---

# 👩‍💻 Author

**Belinda Carol**

Computer Science Student | Aspiring Data Scientist & Machine Learning Engineer

🔗 **GitHub:** https://github.com/belindacarolam04

🌐 **Live Demo:** https://customer-support-intent.streamlit.app/

---

## ⭐ If you found this project interesting, consider giving it a star!
