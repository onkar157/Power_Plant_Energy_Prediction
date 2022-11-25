import streamlit as st
import pandas as pd
import numpy as np
import pickle 


pickle_in = open('C:/Users/onkar/Downloads/model_xgb.pkl', 'rb')
XGB_model = pickle.load(pickle_in)


def welcome():
    return 'welcome everyone'

def prediction(temperature,exhaust_vacuum,amb_pressure,r_humidity):
    
    prediction = XGB_model.predict(
        [[temperature,exhaust_vacuum,amb_pressure,r_humidity]])
    print(prediction)
    return prediction 


def main():
    st.title("ENERGY PREDICTION")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:black;text-align;center;">Streamlit Energy Predictor App </h1>
    </div>
    """
    
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
    temperature = st.text_input("Temperature", "Type Here")
    exhaust_vacuum = st.text_input("Exhaust Vacuum", "Type Here")
    amb_pressure = st.text_input("Ambient Pressure", "Type Here")
    r_humidity = st.text_input("Relative Humidity", "Type Here")
    
    result = ""
    
    if st.button("Predict"):
        result = prediction(temperature,exhaust_vacuum,amb_pressure,r_humidity)
    st.success('Energy Production is {}'.format(result))


if __name__=='__main__':
    main()    