# 💼 Employee Salary Prediction Web Application

A Machine Learning-powered web app that accurately predicts employee salaries based on inputs such as age, gender, education level, job title, and years of experience. Designed with a modern UI using **Streamlit**, and trained using regression techniques in **scikit-learn**.

<p align="center">
  <a href="https://employe-salary-predictionbygirish.streamlit.app/" target="_blank">
    🔗 <strong>Live Demo</strong>
  </a> |
  <a href="https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer/data" target="_blank">
    📂 Dataset
  </a>
</p>

---

## 🚀 Features

- 🔢 Predict salary using multiple input factors
- 🎨 Interactive and modern Streamlit UI
- 📈 Real-time display of predicted salary, monthly salary, hourly rate
- 📊 Visual R² Score indicating model performance
- 🧠 Trained using Linear Regression with proper preprocessing
- 📦 Model caching for fast response

---

## 📊 Input Features

- Age
- Gender
- Education Level
- Job Title
- Years of Experience

---

## 🛠 Tech Stack

| Layer       | Tools Used                        |
|-------------|-----------------------------------|
| UI          | Streamlit, HTML/CSS               |
| ML Model    | Scikit-learn (Linear Regression)  |
| Data Prep   | Pandas, NumPy, LabelEncoder, Scaler |
| Deployment  | Streamlit Cloud                   |

---

## 📁 Project Structure

```

salary-prediction-app/
│
├── app.py                  # Streamlit web app
├── model\_training.ipynb    # Model training notebook
├── salary\_predictor.pkl    # Trained model
├── model\_score.txt         # Stored R² score
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

````

---

## 🔧 Setup Instructions

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

## 📈 Model Information

* **Algorithm**: Linear Regression
* **Evaluation Metric**: R² Score
* **Encoding**: Label Encoding for categorical fields
* **Scaling**: StandardScaler for numeric normalization

---

## 📷 Screenshots

> Replace with actual screenshots in your repo.

| Input Form                               | Salary Prediction Output                 |
| ---------------------------------------- | ---------------------------------------- |
| ![](https://private-user-images.githubusercontent.com/187031858/467276419-bfe61990-5cdf-4dc5-91dd-c6f0b14d65d8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI3MTE2NzgsIm5iZiI6MTc1MjcxMTM3OCwicGF0aCI6Ii8xODcwMzE4NTgvNDY3Mjc2NDE5LWJmZTYxOTkwLTVjZGYtNGRjNS05MWRkLWM2ZjBiMTRkNjVkOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxN1QwMDE2MThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NGRiZDIwZmNiMGVlNWMwZDY5MjNiYjE0N2FmNDQ4OTU2NTU1MjczYzdhMTU0NzQ2NTJkYmY5NWQyNzkzZjNiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.vNq-SE4PSITOW7kF6HpKHIet3Xxb4-gmfIfbZC76ufY) | ![](https://private-user-images.githubusercontent.com/187031858/467276419-bfe61990-5cdf-4dc5-91dd-c6f0b14d65d8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI3MTE2NzgsIm5iZiI6MTc1MjcxMTM3OCwicGF0aCI6Ii8xODcwMzE4NTgvNDY3Mjc2NDE5LWJmZTYxOTkwLTVjZGYtNGRjNS05MWRkLWM2ZjBiMTRkNjVkOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxN1QwMDE2MThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NGRiZDIwZmNiMGVlNWMwZDY5MjNiYjE0N2FmNDQ4OTU2NTU1MjczYzdhMTU0NzQ2NTJkYmY5NWQyNzkzZjNiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.vNq-SE4PSITOW7kF6HpKHIet3Xxb4-gmfIfbZC76ufY) |

---

## 🌐 Live Deployment

This project is deployed and publicly accessible at:
👉 [https://employe-salary-predictionbygirish.streamlit.app/](https://employe-salary-predictionbygirish.streamlit.app/)

---

## 📄 Dataset Source

* Kaggle: [Salary Prediction for Beginners](https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer/data)

---

## 📌 License

This project is for educational and internship purposes. All rights reserved by the author.

```
