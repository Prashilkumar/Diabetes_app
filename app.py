
import numpy as np
import pickle
import streamlit as st
 
 #Loading the saved model
loaded_model = pickle.load(open('trained_model.sav','rb'))
 
 # creating a function for prediction 
 
def diabetes_prediction(input_data):
    #changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return 'Person is not Diabetic'
    else :
        return 'Person is not Diabetic'
     
def main():
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    # getting the input data form the user
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('BloodPressure value')
    SkinThickness = st.text_input('SkinThickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of Person')
    
    # code of prediction
    diagnosis = ''
    
    # Creating a button for prediction 
     
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()