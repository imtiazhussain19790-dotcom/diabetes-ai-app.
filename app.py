import streamlit as st
import joblib
import numpy as np
model = joblib.load(r'C:\Users\FUTURE TECH HYD\Desktop\Python Day 1\diabetes_model.pk1')
st.title("🩺 Smart Diabetes Checker AI")
st.write("Apni medical reports ke mutabiq niche diye gaye khano ko bharen:")
col1, col2 = st.columns(2)
with col1:
    glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
    bmi = st.number_input("BMI (Weight/Height)", min_value=0.0, max_value=70.0, value=25.0)
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    bp = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
with col2:
    preg = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
    ins = st.number_input("Insulin", min_value=0, max_value=900, value=80)
    skin = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
    pedigree = st.number_input("Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    if st.button("Check My Result"):
        features = np.array([[preg, glucose, bp, skin, ins, bmi, pedigree, age]])
        prediction = model.predict(features)
        if prediction[0] == 1:
            st.error("⚠️ Result: Positive - Diabetes ka khatra ho sakta hai.")
        else:
            st.success("✅ Result: Negative - Aap filhal bilkul theek hain!")