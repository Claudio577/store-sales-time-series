import streamlit as st
import pandas as pd
import joblib

st.title("📊 Store Sales Predictor")

model = joblib.load("model/model.joblib")

st.sidebar.header("Input Data")

store = st.sidebar.number_input("Store Number", 1, 54, 1)
family = st.sidebar.number_input("Product Family Code", 0, 30, 1)
onpromotion = st.sidebar.number_input("Promotion Items", 0, 100, 0)

date = st.sidebar.date_input("Select Date")

year = date.year
month = date.month
day = date.day
dayofweek = date.weekday()

input_data = pd.DataFrame({
    "store_nbr":[store],
    "family":[family],
    "year":[year],
    "month":[month],
    "day":[day],
    "dayofweek":[dayofweek],
    "onpromotion":[onpromotion]
})

prediction = model.predict(input_data)

st.subheader("Predicted Sales")

st.write(f"Estimated sales: {prediction[0]:.2f}")
