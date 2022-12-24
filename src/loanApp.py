
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open(r"C:\Users\srila\classifier.pkl", 'rb')
classifier = pickle.load(pickle_in)


def prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
        Loan_Amount_Term, Credit_History, Property_Area):  
   
    prediction = classifier.predict(
        [[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
        Loan_Amount_Term, Credit_History, Property_Area]])
    print(prediction)
    return prediction
 
def main():
      # giving the webpage a title
    st.title("Loan Approval Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Loan Approval Prediction ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    Gender = st.text_input("Gender", "Type Here")
    Married = st.text_input("Married", "Type Here")
    Dependents = st.text_input("Dependents", "Type Here")
    Education = st.text_input("Education", "Type Here")
    Self_Employed = st.text_input("Self_Employed", "Type Here")
    ApplicantIncome = st.text_input("ApplicantIncome", "Type Here")
    CoapplicantIncome = st.text_input("CoapplicantIncome", "Type Here")
    LoanAmount = st.text_input("LoanAmount", "Type Here")
    Loan_Amount_Term = st.text_input("Loan_Amount_Term", "Type Here")
    Credit_History = st.text_input("Credit_History", "Type Here")
    Property_Area = st.text_input("Property_Area", "Type Here")
    
    
    result =""
    if st.button("Predict"):
        result = prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
        Loan_Amount_Term, Credit_History, Property_Area)
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()