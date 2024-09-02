"""First observation features: age                               1.733246
avg_glucose_level                 0.735149
bmi                               0.729592
gender_Male                           True
gender_Other                         False
hypertension_1                       False
heart_disease_1                       True
ever_married_Yes                      True
work_type_Never_worked               False
work_type_Private                     True
work_type_Self-employed              False
work_type_children                   False
smoking_status_formerly smoked       False
smoking_status_never smoked           True
smoking_status_smokes                False
Name: 0, dtype: object
First observation target: stroke    1
"""
    
import streamlit as st
import numpy as np
import pickle

st.set_page_config('Heart Attack Risk Prediction ',layout='wide')

st.markdown('# Heart Attack Rik Prediction :heart:')

st.write('Fill the below fields to predict the heart strokes')

age = st.number_input('Age', 10, 85, 10)
glucose_level =st.number_input('Glucose Level', 50, 130, 60)
gender = st.selectbox('Gender', ['Male', 'Female'], index = 0)
gender_Male, gender_Other = 0
gender_Male = 1 if gender == 'Male' else 0
gender_Other = 1 if gender == 'Female' else 0
hypertension_1 = st.selectbox('Hypertesnion', ['Yes', 'No'])
hypertension_1 = 1 if hypertension_1 == 'Yes' else 0
heart_disease_1 = st.selectbox('Heart Disease', ['Yes', 'No'])
hypertension_1 = 1 if heart_disease_1 == 'Yes' else 0
ever_married_Yes = st.selectbox('Married', ['Yes', 'No'])
ever_married_Yes = 1 if ever_married_Yes == 'Yes' else 0
work_type = st.selectbox('Work Type', ['Worked', 'Private', 'Self-Employed', 'Children'])
work_type_Never_worked = 1 if work_type == 'Worked' else 0         
work_type_Private = 1 if work_type == 'Private' else 0                
work_type_self_employed = 1 if work_type == 'Self-Employed' else 0
work_type_children = 1 if work_type == 'Children' else 0
