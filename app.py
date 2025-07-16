import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
@st.cache_resource
def load_model():
    return joblib.load('salary_predictor.pkl')

@st.cache_data
def load_score():
    with open("model_score.txt", "r") as f:
        return float(f.read())

# Load model components
try:
    model_data = load_model()
    model = model_data['model']
    label_encoders = model_data['label_encoders']
    scaler = model_data['scaler']
    feature_names = model_data['feature_names']
    score = load_score()
except:
    st.error("❗ Please retrain the model first by running all cells in the notebook.")
    st.stop()

# Page configuration
st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼", layout="wide")

# 🌈 Custom CSS Styling
st.markdown("""
<style>
body {
    font-family: 'Segoe UI', sans-serif;
}
.main-header {
    background: linear-gradient(90deg, #3b82f6, #6366f1);
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    text-align: center;
    color: white;
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
}
.metric-card {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    margin-bottom: 1.5rem;
    color: #222;
}
.metric-card h2 {
    font-size: 2rem;
    color: #10b981;
    margin: 0.5rem 0 0;
}
.prediction-card {
    background: linear-gradient(135deg, #4f46e5, #3b82f6);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    margin: 2rem 0;
}
.stButton > button {
    background: linear-gradient(90deg, #3b82f6, #6366f1);
    color: white;
    border: none;
    padding: 0.8rem 2rem;
    border-radius: 30px;
    font-size: 1.1rem;
    font-weight: bold;
    width: 100%;
    transition: all 0.3s ease-in-out;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# 🌟 Main Heading
st.markdown("""
<div class="main-header">
    <h1>💼 Employee Salary Prediction</h1>
    <p>Estimate salaries based on age, gender, education, job title, and experience</p>
</div>
""", unsafe_allow_html=True)

# 🧾 Form Inputs and Info Panel
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📋 Enter Employee Details")
    with st.form("salary_prediction_form"):
        age = st.slider("👤 Age", 18, 70, 30)
        gender = st.selectbox("⚧ Gender", sorted(['Male', 'Female']))
        education = st.selectbox("🎓 Education Level", sorted(["Bachelor's", "Master's", "PhD"]))
        job_title = st.selectbox("💼 Job Title", sorted([
            'Software Engineer', 'Data Analyst', 'Senior Manager', 'Sales Associate',
            'Director', 'Marketing Analyst', 'Product Manager', 'Sales Manager',
            'Marketing Coordinator'
        ]))
        experience = st.slider("📈 Years of Experience", 0.0, 50.0, 5.0, step=0.5)

        submitted = st.form_submit_button("🔮 Predict Salary")

with col2:
    st.markdown("### 📈 Model Performance")
    st.markdown(f"""
    <div class="metric-card">
        <h3>🎯 Model Accuracy (R² Score)</h3>
        <h2>{score:.2%}</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔧 Features Used")
    for feature in feature_names:
        st.markdown(f"- {feature}")

    st.markdown("### 📝 Instructions")
    st.markdown("""
    1. Fill all the employee details on the left.
    2. Click 'Predict Salary'.
    3. View predicted salary with monthly and hourly insights.
    """)

# 🔮 Prediction
if submitted:
    try:
        input_data = pd.DataFrame({
            'Age': [age],
            'Gender': [gender],
            'Education Level': [education],
            'Job Title': [job_title],
            'Years of Experience': [experience]
        })

        # Encode categorical features
        input_encoded = input_data.copy()
        for col in ['Gender', 'Education Level', 'Job Title']:
            if col in label_encoders:
                input_encoded[col] = label_encoders[col].transform(input_data[col])

        # Match column order
        input_final = input_encoded[feature_names]

        # Scale input
        input_scaled = scaler.transform(input_final)

        # Predict salary
        prediction = model.predict(input_scaled)[0]

        # 🌟 Show Prediction
        st.markdown(f"""
        <div class="prediction-card">
            <h2>💰 Predicted Annual Salary</h2>
            <h1>${prediction:,.0f}</h1>
            <p>Based on the employee profile provided</p>
        </div>
        """, unsafe_allow_html=True)

        # 📊 Extra Metrics
        colA, colB, colC = st.columns(3)
        colA.metric("📅 Monthly Salary", f"${prediction/12:,.0f}")
        colB.metric("⏰ Hourly Rate", f"${prediction/(52*40):,.0f}")
        colC.metric("📊 Market Percentile", "75th")  # Placeholder

        # 📋 Input Summary
        st.markdown("### 📌 Summary of Inputs")
        s1, s2 = st.columns(2)
        with s1:
            st.write(f"**👤 Age:** {age}")
            st.write(f"**⚧ Gender:** {gender}")
            st.write(f"**🎓 Education:** {education}")
        with s2:
            st.write(f"**💼 Job Title:** {job_title}")
            st.write(f"**📈 Experience:** {experience} years")

    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
        st.info("Ensure the model was trained using these input features.")

# 🔻 Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 0.9rem; color: #777;">
    🤖 Powered by Machine Learning | 🔐 Secure and Local | 🌐 Streamlit Web App
</div>
""", unsafe_allow_html=True)
