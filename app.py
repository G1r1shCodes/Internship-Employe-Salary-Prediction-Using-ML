import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Employee Salary Predictor",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
/* General styling */
.main {
    background-color: #1f2937;
    color: #e5e7eb;
}

/* Header styles */
.header {
    color: #93c5fd;
    font-size: 32px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 20px;
}
.subheader {
    color: #d1d5db;
    font-size: 22px;
    font-weight: 600;
    margin-top: 30px;
    margin-bottom: 10px;
}

/* Info box */
.info-box {
    background-color: #1f2937;
    border-left: 6px solid #3b82f6;
    padding: 20px;
    border-radius: 10px;
    font-size: 16px;
    line-height: 1.6;
    color: #f3f4f6;
    margin-bottom: 30px;
}

/* Input and select styling */
.stNumberInput input, .stSelectbox div[data-baseweb="select"] {
    background-color: #374151;
    color: #e5e7eb;
    border: 1px solid #4b5563;
    border-radius: 5px;
}
.stSelectbox div[data-baseweb="select"] > div {
    color: #e5e7eb;
}

/* Center form button */
.center-button {
    display: flex;
    justify-content: center;
    margin-top: 25px;
}
.stButton>button {
    background-color: #3b82f6;
    color: white;
    padding: 10px 25px;
    border-radius: 10px;
    font-weight: bold;
    font-size: 16px;
    border: none;
}
.stButton>button:hover {
    background-color: #60a5fa;
}

/* Prediction box */
.prediction-box {
    background-color: #2563eb;
    color: white;
    padding: 25px;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    border-radius: 12px;
    margin-top: 30px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# Load model
model_data = joblib.load("salary_predictor.pkl")
model = model_data["model"]
label_encoders = model_data["label_encoders"]
scaler = model_data["scaler"]
feature_names = model_data["feature_names"]

# Load supporting assets
eval_plot = Image.open("evaluation_plot.png")
with open("model_score.txt", "r") as f:
    r2_score = float(f.read())

# Header
st.markdown('<div class="header">💼 Employee Salary Predictor</div>', unsafe_allow_html=True)

# Info box
st.markdown(f"""
<div class="info-box">
    <b>📘 Algorithm Used:</b> Linear Regression<br>
    <b>📈 Model R² Score:</b> {r2_score:.4f}<br>
    <b>📊 Evaluation:</b> Compares predicted vs actual salaries.
</div>
""", unsafe_allow_html=True)

# Form title
st.markdown('<div class="subheader">📝 Enter Employee Details</div>', unsafe_allow_html=True)

# Input form
with st.form("salary_form"):
    age = st.number_input("Age", min_value=18, max_value=80, value=30)
    gender = st.selectbox("Gender", options=label_encoders["Gender"].classes_)
    education_level = st.selectbox("Education Level", options=label_encoders["Education Level"].classes_)
    job_title = st.selectbox("Job Title", options=label_encoders["Job Title"].classes_)
    years_of_experience = st.number_input("Years of Experience", min_value=0, max_value=40, value=5)

    # Centered button
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    submit_button = st.form_submit_button("Predict Salary")
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction output
if submit_button:
    input_df = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Education Level": [education_level],
        "Job Title": [job_title],
        "Years of Experience": [years_of_experience]
    })

    for col in ["Gender", "Education Level", "Job Title"]:
        input_df[col] = label_encoders[col].transform(input_df[col])

    input_scaled = scaler.transform(input_df)
    predicted_salary = model.predict(input_scaled)[0]

    predicted_inr = predicted_salary * 83  # Approx conversion rate to INR
    st.markdown(f"""
    <div class="prediction-box">
        💰 <b>Estimated Annual Salary:</b><br>
        USD ${predicted_salary:,.2f}<br>
        INR ₹{predicted_inr:,.0f}<br><br>
        📌 This prediction is based on your provided inputs and the model's training data.<br>
        📈 Accuracy may vary depending on job type and experience levels.
    </div>
    """, unsafe_allow_html=True)

# Evaluation section
st.markdown('<div class="subheader">📉 Model Evaluation</div>', unsafe_allow_html=True)
st.image(eval_plot, caption="Actual vs Predicted Salary", use_container_width=True)
