# 📊 Store Sales Forecast Dashboard

Machine Learning project for predicting store sales using time series features and an interactive dashboard built with Streamlit.

---

## 🚀 Live Demo

Access the deployed application:

https://store-sales-time-series.streamlit.app

---

## 📌 Project Overview

This project predicts retail sales using historical store data.  
The system uses machine learning to estimate future sales based on store number, product category, promotions, and temporal features extracted from the date.

The application provides an interactive dashboard where users can simulate different scenarios and visualize predicted sales.

---

## 🧠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib

---

## 📂 Dataset

The dataset comes from the Kaggle competition:

Store Sales – Time Series Forecasting

Due to the dataset size, this repository includes a reduced sample version (`train_sample.csv`).

The original dataset is available on Kaggle.

---

## ⚙️ Machine Learning Model

The model used is:

Random Forest Regressor

The following features were engineered from the dataset:

- store_nbr
- product family
- promotion count
- year
- month
- day
- day of week

The model predicts the expected sales value for a given store and date.

Evaluation metric used:

Root Mean Squared Error (RMSE)

---

## 📊 Dashboard Features

The Streamlit dashboard allows users to:

- Select store number
- Select product category
- Define promotion levels
- Choose prediction date
- Generate sales prediction
- Visualize historical sales data

---

## 🖥 Project Structure

```
store-sales-time-series
│
├── app.py
├── requirements.txt
│
├── model
│   └── model.joblib
│
├── data
│   └── raw
│
├── notebooks
│
└── README.md
```

---

## ▶️ Running the Project Locally

Clone the repository:

```
git clone https://github.com/Claudio577/store-sales-time-series
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

## 📈 Future Improvements

Possible enhancements for the project:

- Implement LightGBM model
- Add interactive visualizations with Plotly
- Predict sales for multiple days
- Improve feature engineering
- Integrate additional external data sources

---

## 👨‍💻 Author

Claudio Hideki Yoshida

AI & Machine Learning Student  
Python | Data Science | Artificial Intelligence

LinkedIn:  
https://www.linkedin.com/in/claudio-yoshida-726510359/
