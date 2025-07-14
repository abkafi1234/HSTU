import joblib 
import streamlit as st

states = ['California', 'Florida', 'New York']
model = joblib.load('./Logistic.joblib')


profit_input = st.number_input("Enter the profit:")

if st.button('Predict'):
    predicted_state = model.predict([[profit_input]])
    st.write(f"Predicted State is {states[predicted_state[0]]} .")
