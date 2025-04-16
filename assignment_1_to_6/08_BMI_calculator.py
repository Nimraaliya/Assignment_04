import streamlit as st
import pandas as pd

# Title
st.title("🧮 BMI Calculator")

# Height slider (fix the comma between 250 and 175)
height = st.slider("Enter your height (in cm):", 100, 250, 175)

# Weight slider (add 'step' keyword for 60 to make sense)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70, step=1)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

# Display the BMI
st.write(f"### Your BMI is: `{bmi:.2f}`")

# Show the BMI Categories
st.write("### 🧾 BMI Categories:")
st.write("- **Underweight**: BMI less than 18.5")
st.write("- **Normal weight**: BMI between 18.5 and 24.9")
st.write("- **Overweight**: BMI between 25 and 29.9")
st.write("- **Obesity**: BMI 30 or greater")

