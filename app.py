import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="Store Sales Dashboard", layout="wide")

st.title("📊 Store Sales Forecast Dashboard")

# carregar modelo
model = joblib.load("model/model.joblib")

# carregar dataset
df = pd.read_csv("data/raw/train_sample.csv")

df["date"] = pd.to_datetime(df["date"])

# SIDEBAR
st.sidebar.header("Prediction Input")

store = st.sidebar.number_input("Store Number", 1, 54, 1)
family = st.sidebar.number_input("Product Family Code", 0, 30, 1)
onpromotion = st.sidebar.number_input("Promotion Items", 0, 100, 0)

date = st.sidebar.date_input("Prediction Date")

year = date.year
month = date.month
day = date.day
dayofweek = date.weekday()

# previsão
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

st.subheader("📈 Predicted Sales")

st.metric("Estimated Sales", f"{prediction[0]:.2f}")

# gráfico histórico
st.subheader("📊 Historical Sales")

df_plot = df[(df["store_nbr"] == store)]

df_plot = df_plot.sort_values("date")

fig, ax = plt.subplots()

ax.plot(df_plot["date"], df_plot["sales"])

ax.set_title("Sales History")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")

st.pyplot(fig)
