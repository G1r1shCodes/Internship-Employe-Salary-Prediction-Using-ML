# 💼 Employee Salary Prediction Web App

A Machine Learning-powered web application that predicts an employee's annual salary based on multiple features such as age, gender, education level, job title, and years of experience. The app is built using **Streamlit** for the frontend and **scikit-learn** for modeling.

---

## 🚀 Demo

![App Screenshot](https://via.placeholder.com/800x400.png?text=App+Screenshot) <!-- Replace with actual screenshot if uploading -->

---

## 🧠 Project Highlights

- 📊 **Regression Model** trained on structured employee salary data
- 🎨 **Modern Streamlit UI** with interactive sliders and dropdowns
- 🧮 **Features used**: Age, Gender, Education Level, Job Title, Years of Experience
- 📈 Shows **Predicted Salary**, Monthly Salary, Hourly Rate, and more
- ✅ Model Accuracy (R² Score) shown on the interface
- 💾 Supports model caching with `joblib` for fast performance

---

## 📂 Project Structure

```

salary-predictor-app/
│
├── app.py                    # Streamlit UI application
├── model\_training.ipynb      # Jupyter Notebook for model building & training
├── salary\_predictor.pkl      # Saved trained model (Joblib format)
├── model\_score.txt           # R² score of the model
├── requirements.txt          # Python dependencies
├── Salary Data.csv           # Sample dataset (optional)
└── README.md                 # Project documentation

````

---

## 📌 Features

- 🔢 Real-time predictions from user input
- 💬 Supports encoding of categorical variables like Gender, Education, and Job Title
- 🔒 No data is stored — everything runs securely on-device
- 📱 Responsive layout with intuitive design

---

## 🛠️ Tech Stack

| Layer     | Technology            |
|-----------|------------------------|
| Frontend  | Streamlit              |
| Backend   | Scikit-learn (ML model)|
| Data      | Pandas, NumPy          |
| Model     | LinearRegression       |
| Styling   | Custom HTML/CSS        |
| Packaging | Joblib                 |

---

## ⚙️ Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/salary-predictor-app.git
   cd salary-predictor-app
````

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   streamlit run app.py
   ```

---

## 📊 Model Details

* **Algorithm**: Linear Regression
* **Encoding**: Label Encoding for categorical features
* **Scaler**: StandardScaler
* **Evaluation Metric**: R² Score
* **Output**: Predicted annual salary (numeric)

---

## 📸 Screenshots

| Input Form                                                        | Prediction Output                                                  |
| ----------------------------------------------------------------- | ------------------------------------------------------------------ |
| ![Input](https://via.placeholder.com/350x200.png?text=Input+Form) | ![Output](https://via.placeholder.com/350x200.png?text=Prediction) |

> *(Replace with actual screenshots when uploading to GitHub)*

---

## ✨ Future Enhancements

* ✅ Add more regression models (RandomForest, XGBoost)
* 📊 Display prediction confidence intervals
* 🗃️ Database integration for logging predictions
* 🌐 Deploy on Streamlit Cloud or Hugging Face Spaces

---

## 🙌 Acknowledgements

* Dataset prepared for demonstration purposes
* Streamlit for the fantastic UI framework
* CodeWithHarry / CampusX inspiration for ML fundamentals

---

## 👨‍💻 Author

**Girish Kumar Yadav**
Third Year B.Tech Student

🔗 [LinkedIn](https://linkedin.com/in/girishkumarcs) • 📧 [your.email@example.com](girishyadav.cs@gmail.com)

---
