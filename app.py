import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

st.set_page_config(layout="wide")

scaler = joblib.load("scaler.pkl")

st.title("Restaurant Ratings Predictor")

st.caption("Predict restaurant ratings based on various features.")
st.divider()

averagecost = st.number_input("Average Cost for Two", min_value=50, max_value=999999, value=1000, step = 200)

tablebooking = st.selectbox("Table Booking Available", ["Yes", "No"])

onlinedelivery = st.selectbox("Online delviery Available", ["Yes", "No"])

pricerange = st.selectbox("Price Range (1 cheapest to 4 costliest)", ["1", "2", "3", "4"])

predictbutton = st.button("Predict the Review!")

st.divider()


model = joblib.load("mlmodel.pkl")

bookingstatus = 1 if tablebooking == "Yes" else 0

deliverystatus = 1 if onlinedelivery == "Yes" else 0

values = [[averagecost, bookingstatus, deliverystatus, pricerange]]

my_X_values = np.array(values)

X = scaler.transform(my_X_values)

if predictbutton:
    st.snow()

    prediction = model.predict(X)

    if prediction < 2.5:
        st.write("Poor")
    elif prediction < 3.5:
        st.write("Average")
    elif prediction < 4.0:
        st.write("Good")
    elif prediction < 4.5:
        st.write("Very Good")
    else:
        st.write("Excellent")