import streamlit as st
import numpy as np
import joblib

model =  joblib.load('model.joblib')

st.title('What is the Smoking Status of the person? :smoking:')

gender = st.selectbox("Gender(M:0,F:1)", [0,1])
height_cm = st.number_input("Height", 100.0, 200.0)
hemoglobin = st.number_input("Hemoglobin", 4.0, 22.0)
Gtp = st.number_input("Gtp", 1.0, 1000.0)
weight_kg = st.slider("Weight(kg)", 30, 135)
serum_creatinine = st.number_input("Serum Creatinine", 0.1, 12.0)
triglyceride = st.number_input("Triglyceride", 0.0, 999.0)
waist_cm = st.number_input("Waist(cm)", 50.0, 130.0)
HDL = st.number_input("HDL", 1.0, 620.0)
ALT = st.number_input("ALT", 1.0, 3000.0)
age = st.slider("Age", 1, 80)
systolic = st.number_input("Systolic", 70.0, 250.0)
fasting_blood_sugar = st.number_input("Fasting Blood Sugar", 40.0, 520.0)
tartar = st.selectbox("Tartar(Y:1,N:0)", [0,1])
relaxation = st.number_input("Relaxation", 40.0, 150.0)
dental_caries = st.selectbox("Dental Caries(Y:1,N:0)", [0,1])
Cholesterol = st.number_input("Cholesterol", 50.0, 450.0)

def predict():
    float_features = [float(x) for x in [height_cm, hemoglobin, Gtp, triglyceride, waist_cm, HDL, ALT, systolic, fasting_blood_sugar, relaxation,Cholesterol]]
    categorical_features = [gender, tartar, dental_caries]
    integer_features = [age, weight_kg]

    final_features = [np.array(float_features + integer_features + categorical_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)
    
    st.success('The Prediction is : ' + str(label))
    if prediction[0] == 1:
        st.success['The person is a smoker :smoking:']
        
    else:
        st.success['The person is a non-smoker :no_smoking:']
    
trigger = st.button('Predict', on_click=predict)
