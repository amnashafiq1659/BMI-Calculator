import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height in cm", min_value=100, max_value=300)
weight = st.slider("Enter your weight in kg", min_value=10, max_value=300)

bmi = weight / ((height/100)**2)

st.success(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
    color = "blue"
elif 18.5 <= bmi < 24.9:
    category = "Healthy weight"
    color = "green"
elif 25 <= bmi < 29.9:
    category = "Overweight"
    color = "orange"
else:
    category = "Obesity"
    color = "red"
    
st.markdown(f"<p style='color: {color}; font-size: 20px'>Category:{category}</p>",unsafe_allow_html=True)

st.sidebar.header("BMI Classification")
st.sidebar.write("💙 **Underweight:** BMI below 18.5 - You might need to gain some healthy weight.")
st.sidebar.write("💚 **Healthy Weight:** BMI between 18.5 and 24.9 - Great job! Maintain your healthy lifestyle.")
st.sidebar.write("🧡 **Overweight:** BMI between 25 and 29.9 - Consider balancing your diet and exercise.")
st.sidebar.write("❤️ **Obese:** BMI 30 or above - Prioritize a healthier routine and seek professional guidance if needed.")

if category == "Underweight":
    st.info("You are underweight. Consider consulting a nutritionist for a balanced diet.")
    
elif category == "Healthy weight":
    st.success("You have a healthy weight. Keep up the good work with a balanced diet and exercise.")
    
elif category == "Overweight":
    st.warning("You are overweight. Consider with a balanced diet and regular exercise.")
    
else:
    st.error("You are in the obesity range. It is recommended to seek medical advice for a healthier lifestyle. Focus on balanced meals and an active routine.")
    
    