import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

# Set page configuration with a custom theme
st.set_page_config(
    page_title="Employee Salary Predictor",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Apply custom CSS for darker theme
st.markdown(
    """
    <style>
    .main {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 10px;
        color: #e5e7eb;
    }
    .stButton>button {
        background-color: #3b82f6;
        color: #ffffff;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #60a5fa;
    }
    .stNumberInput input {
        background-color: #374151;
        color: #e5e7eb;
        border: 1px solid #4b5563;
        border-radius: 5px;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #374151;
        color: #e5e7eb;
        border: 1px solid #4b5563;
        border-radius: 5px;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        color: #e5e7eb;
    }
    .header {
        color: #93c5fd;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subheader {
        color: #d1d5db;
        font-size: 20px;
        font-weight: 600;
        margin-top: 20px;
    }
    .info-box {
        background-color: #374151;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: #e5e7eb;
    }
    .stSuccess {
        background-color: #1e3a8a !important;
        color: #ffffff !important;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the model and preprocessing objects
model_data = joblib.load("salary_predictor.pkl")
model = model_data["model"]
label_encoders = model_data["label_encoders"]
scaler = model_data["scaler"]
feature_names = model_data["feature_names"]

# Load the evaluation plot
eval_plot = Image.open("evaluation_plot.png")

# Load the model score
with open("model_score.txt", "r") as f:
    r2_score = float(f.read())

# Streamlit app
st.markdown('<div class="header">Employee Salary Prediction</div>', unsafe_allow_html=True)

# Display algorithm and accuracy in an info box
with st.container():
    st.markdown(
        f"""
        <div class="info-box">
            <strong>Algorithm Used:</strong> Linear Regression<br>
            <strong>Model Accuracy (R² Score):</strong> {r2_score:.4f}
        </div>
        """,
        unsafe_allow_html=True
    )

# Input form
st.markdown('<div class="subheader">Enter Employee Details</div>', unsafe_allow_html=True)
with st.form(key="salary_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Age",
            min_value=18,
            max_value=80,
            value=30,
            help="Enter age between 18 and 80"
        )
        gender = st.selectbox(
            "Gender",
            options=label_encoders["Gender"].classes_,
            help="Select the employee's gender"
        )
        education_level = st.selectbox(
            "Education Level",
            options=label_encoders["Education Level"].classes_,
            help="Select the highest education level"
        )
    
    with col2:
        job_title = st.selectbox(
            "Job Title",
            options=label_encoders["Job Title"].classes_,
            help="Select the job title"
        )
        years_of_experience = st.number_input(
            "Years of Experience",
            min_value=0,
            max_value=40,
            value=5,
            help="Enter experience between 0 and 40 years"
        )
    
    # Prediction button
    submit_button = st.form_submit_button("Predict Salary")

# Handle prediction
if submit_button:
    # Create a DataFrame from input
    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Education Level": [education_level],
        "Job Title": [job_title],
        "Years of Experience": [years_of_experience]
    })
    
    # Label encode categorical features
    for col in ["Gender", "Education Level", "Job Title"]:
        le = label_encoders[col]
        input_data[col] = le.transform(input_data[col])
    
    # Scale the features
    input_scaled = scaler.transform(input_data)
    
    # Predict salary
    predicted_salary = model.predict(input_scaled)[0]
    
    # Display the prediction
    st.success(f"Predicted Salary: ${predicted_salary:,.2f}")

# Display the evaluation plot
st.markdown('<div class="subheader">Model Evaluation Plot</div>', unsafe_allow_html=True)
st.image(eval_plot, caption="Actual vs Predicted Salary", use_column_width=True)