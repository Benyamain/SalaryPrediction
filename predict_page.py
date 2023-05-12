import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']

def show_predict_page():
    st.title('Software Developer Salary Prediction')
    st.write("""### We need some information to predict the salary""")

    countries = (
        'United States of America',
        'Germany',
        'United Kingdom of Great Britain and Northern Ireland',
        'India',
        'Canada',
        'France',
        'Brazil',
        'Spain',
        'Netherlands',
        'Australia',
        'Italy',
        'Poland',
        'Sweden',
        'Russian Federatio',
        'Switzerland'
    )

    education = (
        'Less than a Bachelors',
        'Bachelor’s degree',
        'Master’s degree',
        'Post grad',
    )

    country = st.selectbox('Country', countries)
    education = st.selectbox('Education Level', education)
    experience = st.slider('Years of Experience', 0, 50, 3)