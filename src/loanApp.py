
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open(r".\classifier.pkl", 'rb')
classifier = pickle.load(pickle_in)

print(classifier)

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
        
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.idfcfirstbank.com/content/dam/idfcfirstbank/images/blog/finance/what-is-a-collateral-loan-717x404.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )




def main():
      # giving the webpage a title
    add_bg_from_url()
    # st.title("Loan Approval Prediction")

    st.markdown("<h1 style='text-align: center; color: white;'>Loan Approval Prediction</h1>", unsafe_allow_html=True)
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    # html_temp = """
    # <h1 style ="text-align:center;">Loan Approval Prediction</h1>
    # """
    # st.markdown(html_temp , )
    # this line allows us to display the front end aspects we have 
    # defined in the above code
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    
    Gender = st.selectbox(
    'Gender',
    ('select' , 'Male', 'Female'))
    Married = st.selectbox("Married", 
    ('select' , 'Yes' , 'No'))
    Dependents = st.text_input("Dependents")
    Education = st.selectbox(
    'Education',
    ('select' , 'Graduate', 'Not Graduate'))
    Self_Employed = st.selectbox(
    'Self Employed',
    ('select' , 'Yes', 'No'))
    ApplicantIncome = st.text_input("ApplicantIncome")
    CoapplicantIncome = st.text_input("CoapplicantIncome")
    LoanAmount = st.text_input("LoanAmount")
    Loan_Amount_Term = st.text_input("Loan_Amount_Term")
    Credit_History = st.text_input("Credit_History")
    Property_Area = st.selectbox(
    'Property Area',
    ('select' , 'Urban', 'Rural','Semi-Urban'))
    
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