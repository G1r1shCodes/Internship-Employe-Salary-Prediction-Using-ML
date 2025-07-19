# 💼 Employee Salary Prediction Web Application

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

| Input Form                               | Salary Prediction Output                 |
| ---------------------------------------- | ---------------------------------------- |
| ![](https://private-user-images.githubusercontent.com/187031858/468243551-fae1b6e7-89f6-486e-af90-02fda7af9c6c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI4ODgzOTYsIm5iZiI6MTc1Mjg4ODA5NiwicGF0aCI6Ii8xODcwMzE4NTgvNDY4MjQzNTUxLWZhZTFiNmU3LTg5ZjYtNDg2ZS1hZjkwLTAyZmRhN2FmOWM2Yy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxOVQwMTIxMzZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lZDRkNWVmYmNjMDc5YWU4NTNlMDk4MzMwNGYyZTA2Yzg5ZmRmNzMyMjY2ZjhkZDI1YjdmMGUxN2I0ODQ5MzQzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.C9QiTfTaEpnDXnqMLjwBv8v63ILOx1KhFOFKHweVJPI) | ![](https://private-user-images.githubusercontent.com/187031858/468243582-92dc87c3-bddd-4ed3-bb52-95c0ad53b586.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI4ODgzOTYsIm5iZiI6MTc1Mjg4ODA5NiwicGF0aCI6Ii8xODcwMzE4NTgvNDY4MjQzNTgyLTkyZGM4N2MzLWJkZGQtNGVkMy1iYjUyLTk1YzBhZDUzYjU4Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxOVQwMTIxMzZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lMTZkN2Y3NGM0MWVmNmU3NTNkYTA2NGVmOGUxYTlhZTQ3N2JlZTgwYzJlNDI3N2FjZGRjMDRjZWRjYzUwMjVmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ZsRxnqi0hnQt11AwN53gX4kppNdK5-Km6BNCdKLjhR0) |

---

## 🌐 Live Deployment

This project is deployed and publicly accessible at:
👉 [https://employe-salary-predictionbygirish.streamlit.app/](https://employee-salary-predictionbygirish.streamlit.app/)

---

## 📄 Dataset Source

* Kaggle: [Salary Prediction for Beginners](https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer/data)

---

## 📌 License
This project is for educational and internship purposes. All rights reserved by the author.
