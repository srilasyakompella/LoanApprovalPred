
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open(r".\classifier.pkl", 'rb')
classifier = pickle.load(pickle_in)


def prediction(Attributes):  
   
    prediction = classifier.predict(
        [Attributes])
    print(prediction)
    return prediction

def toCategoricalVar(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
    Loan_Amount_Term, Credit_History, Property_Area):
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1


    if Married == "No":
        Married = 0
    else:
        Married = 1


    if Education == "Graduate":
        Education = 0
    else:
        Education = 1


    if Self_Employed == "No":
        Self_Employed = 0
    else:
        Self_Employed = 1


    if Property_Area == "Urban":
        Property_Area = 2
    elif Property_Area == "Rural":
        Property_Area = 0
    else:
        Property_Area = 1


    return [Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
        Loan_Amount_Term, Credit_History, Property_Area]
        
 
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
    
    Gender = st.selectbox(
    'Gender',
    ('Male', 'Female'))
    Married = st.selectbox("Married", 
    ('Yes' , 'No'))
    Dependents = st.text_input("Dependents", "Type Here")
    Education = st.selectbox(
    'Education',
    ('Graduate', 'Not Graduate'))
    Self_Employed = st.selectbox(
    'Self Employed',
    ('Yes', 'No'))
    ApplicantIncome = st.text_input("ApplicantIncome", "Type Here")
    CoapplicantIncome = st.text_input("CoapplicantIncome", "Type Here")
    LoanAmount = st.text_input("LoanAmount", "Type Here")
    Loan_Amount_Term = st.text_input("Loan_Amount_Term", "Type Here")
    Credit_History = st.text_input("Credit_History", "Type Here")
    Property_Area = st.selectbox(
    'Property Area',
    ('Urban', 'Rural','Semi-Urban'))
    
    Attributes = toCategoricalVar(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
        Loan_Amount_Term, Credit_History, Property_Area)

    
    result =""
    ans = ""
    if st.button("Predict"):
        result = prediction(Attributes)
    if result == 1:
        ans = "Loan approval is possible"
    else:
        ans = "Loan cannot be granted"
    st.success(ans)
     
if __name__=='__main__':
    main()