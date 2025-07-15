import joblib 
import streamlit as st

model = joblib.load('./Linear.joblib')
spend = st.number_input("Enter the spend amount: ")
if st.button("Predict Profit"):
    profit = model.predict([[spend]])
    st.write(f"Predicted profit for spend amount {spend} is: {profit[0]}")