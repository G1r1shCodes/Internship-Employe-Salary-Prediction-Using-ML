#  Employee Salary Prediction Web Application

A Machine Learning-powered web app that accurately predicts employee salaries based on inputs such as age, gender, education level, job title, and years of experience. Designed with a modern UI using **Streamlit**, and trained using regression techniques in **scikit-learn**.

<p align="center">
  <a href="https://employee-salary-predictionbygirish.streamlit.app/" target="_blank">
    🔗 <strong>Live Demo</strong>
  </a> |
  <a href="https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer/data" target="_blank">
    📂 Dataset
  </a>
</p>

---

## Features

-  Predict salary using multiple input factors
-  Interactive and modern Streamlit UI
-  Real-time display of predicted salary, monthly salary, hourly rate
-  Visual R² Score indicating model performance
-  Trained using Linear Regression with proper preprocessing
-  Model caching for fast response

---

## Input Features

- Age
- Gender
- Education Level
- Job Title
- Years of Experience

---

## Tech Stack

| Layer       | Tools Used                        |
|-------------|-----------------------------------|
| UI          | Streamlit, HTML/CSS               |
| ML Model    | Scikit-learn (Linear Regression)  |
| Data Prep   | Pandas, NumPy, LabelEncoder, Scaler |
| Deployment  | Streamlit Cloud                   |

---

## Project Structure

```

salary-prediction-app/
│
├── app.py                  # Streamlit web app
├── Employee-Salary-Model.ipynb  # Model training notebook
├── salary\_predictor.pkl    # Trained model
├── model\_score.txt         # Stored R² score
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

````

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/salary-prediction-app.git
cd salary-prediction-app
````

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application Locally

```bash
streamlit run app.py
```

---

## Model Information

* **Algorithm**: Linear Regression
* **Evaluation Metric**: R² Score
* **Encoding**: Label Encoding for categorical fields
* **Scaling**: StandardScaler for numeric normalization

---

##  Screenshots

| Input Form                               | Salary Prediction Output                 |
| ---------------------------------------- | ---------------------------------------- |
| [![F481063-E-7676-4-BB4-91-F0-8778010069-E7.png](https://i.postimg.cc/fLDtHzJg/F481063-E-7676-4-BB4-91-F0-8778010069-E7.png)](https://postimg.cc/jW3S2r6z) | [![5-C3-D3098-24-A4-4-EF3-ABE2-7-D2-EBE64-D96-A.png](https://i.postimg.cc/Xqhv04YW/5-C3-D3098-24-A4-4-EF3-ABE2-7-D2-EBE64-D96-A.png)](https://postimg.cc/D4rhrVGp) |

---

##  Live Deployment

This project is deployed and publicly accessible at:
👉 [https://employe-salary-predictionbygirish.streamlit.app/](https://employee-salary-predictionbygirish.streamlit.app/)

---

##  Dataset Source

* Kaggle: [Salary Prediction for Beginners](https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer/data)

---

## License
This project is for educational and internship purposes. All rights reserved by the author.
