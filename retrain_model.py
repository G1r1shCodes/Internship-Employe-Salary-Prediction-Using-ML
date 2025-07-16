# Quick script to retrain the enhanced model
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import joblib

print("🚀 Retraining enhanced salary prediction model...")

# Load and clean data
df = pd.read_csv("data/Salary Data.csv")
df = df.drop_duplicates()
df = df.dropna()

print(f"✅ Dataset loaded and cleaned: {df.shape}")

# Feature Engineering
label_encoders = {}
categorical_columns = ['Gender', 'Education Level', 'Job Title']
df_processed = df.copy()

for col in categorical_columns:
    label_encoders[col] = LabelEncoder()
    df_processed[col] = label_encoders[col].fit_transform(df_processed[col])

print("✅ Categorical variables encoded")

# Display unique values for reference
print("\n📊 Unique values for categorical features:")
for col in categorical_columns:
    unique_values = sorted(df[col].unique())
    print(f"   {col}: {unique_values}")

# Define features and target
X = df_processed[['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience']]
y = df_processed['Salary']

print(f"\n✅ Features selected: {list(X.columns)}")
print(f"✅ Dataset shape: {X.shape}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"✅ Data split and scaled - Train: {X_train_scaled.shape}, Test: {X_test_scaled.shape}")

# Train model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

print("✅ Model trained successfully")

# Evaluate model
y_pred = model.predict(X_test_scaled)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\n📈 Model Performance:")
print(f"   R² Score: {r2:.4f} ({r2:.1%})")
print(f"   RMSE: ${rmse:,.2f}")

# Save enhanced model
model_data = {
    'model': model,
    'label_encoders': label_encoders,
    'scaler': scaler,
    'feature_names': ['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience']
}

joblib.dump(model_data, 'salary_predictor.pkl')

# Save score
with open("model_score.txt", "w") as f:
    f.write(str(r2))

print(f"\n💾 Enhanced model saved successfully!")
print(f"   Features: {len(model_data['feature_names'])} ({', '.join(model_data['feature_names'])})")
print(f"   Model file: salary_predictor.pkl")
print(f"   Score file: model_score.txt")

print("\n🎉 Model retraining complete! You can now run the Streamlit app with all features.")