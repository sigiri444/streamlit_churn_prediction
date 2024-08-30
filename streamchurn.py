import sys
import pandas
import streamlit as st
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.impute import SimpleImputer
import pickle
from sklearn.feature_selection import RFE
import numpy
from sklearn.model_selection import GridSearchCV

am = ['YES',"NO"]

model = pickle.load(open('model_churn.pkl','rb'))

credit_score=st.number_input("Enter your Credit Score")
tenure=	st.number_input('Enter Tenure in months')
balance=st.number_input('Please Enter current account balance')
products_number=st.slider('Choose Nunber of products registered',0.0,5.0,0.0,step=1.0)
credit_card=st.slider('Choose Number of credit card',0.0,5.0,0.0,step=1.0)
active_member=st.selectbox('Are you an Active member',am)
estimated_salary=st.slider('Select Salary Range',10000.0,5000000.0,10000.0,step=10000.0)

active_mem = []
if active_member == 'Yes':
    active_mem.append(1)
else:
    active_mem.append(0)

pre =[]
if st.button("Submit"):
    prediction = model.predict([[credit_score,tenure,balance,products_number,credit_card,active_mem[0],estimated_salary]])[0]
    st.write("The prediction is: ", prediction)
    pre.append(prediction)
    if pre[0] == 0:
        st.write("Chance of Churn is Zero/Low")
    elif pre[0] == 1:
        st.write("Chance of Churn is High")


st.write("Thank you")