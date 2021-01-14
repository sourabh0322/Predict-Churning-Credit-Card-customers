from flask import Flask, render_template, request
import pandas as pd

import requests
import joblib
import numpy as np
import sklearn

app = Flask(__name__)
model = joblib.load("save_models.pkl")
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        Customer_Age = int(request.form['Customer_Age'])
        
        Gender=request.form['Gender']
        if(Gender=="male"):
            Gender=0
        else:
            Gender=1
        
        Dependent_count = int(request.form['Dependent_count'])
        
        Education_Level=request.form['Education_Level']
        if(Education_Level=="Doctorate"):
            Education_Level=0.0
        elif(Education_Level=="Post-Graduate"):
            Education_Level=1.0
        elif(Education_Level=="Graduate"):
            Education_Level=2.0
        elif(Education_Level=="College"):
            Education_Level=3.0
        elif(Education_Level=="High School"):
            Education_Level=4.0
        elif(Education_Level=="Uneducated"):
            Education_Level=5.0
        else:
            Education_Level=6.0
        
        Marital_Status=request.form['Marital_Status']
        if(Marital_Status=="Married"):
            Marital_Status=3
        elif(Marital_Status=="Single"):
            Marital_Status=2
        elif(Marital_Status=="Divorced"):
            Marital_Status=1
        else:
            Marital_Status=0
        
        Income_Category=request.form['Income_Category']
        if(Income_Category=="$120K +"):
            Income_Category=5.0
        elif(Income_Category=="$80K - $120K"):
            Income_Category=4.0
        elif(Income_Category=="$60K - $80K"):
            Income_Category=3.0
        elif(Income_Category=="$40K - $60K"):
            Income_Category=2.0
        elif(Income_Category=="Less than $40K"):
            Income_Category=1.0
        else:
            Income_Category=0.0
            
        Card_Category=request.form['Card_Category']
        if(Card_Category=="Platinum"):
            Card_Category=3.0
        elif(Card_Category=="Gold"):
            Card_Category=2.0
        elif(Card_Category=="Silver"):
            Card_Category=1.0
        else:
            Card_Category=0.0
            
        Months_on_book= int(request.form['Months_on_book'])
        Total_Relationship_Count= int(request.form['Total_Relationship_Count'])
        Months_Inactive_12_mon= int(request.form['Months_Inactive_12_mon'])
        Contacts_Count_12_mon= int(request.form['Contacts_Count_12_mon'])
        Credit_Limit= float(request.form['Credit_Limit'])
        Total_Revolving_Bal= int(request.form['Total_Revolving_Bal'])
        Avg_Open_To_Buy= float(request.form['Avg_Open_To_Buy'])
        Total_Amt_Chng_Q4_Q1= float(request.form['Total_Amt_Chng_Q4_Q1'])
        Total_Trans_Amt= int(request.form['Total_Trans_Amt'])
        Total_Trans_Ct= int(request.form['Total_Trans_Ct'])
        Total_Ct_Chng_Q4_Q1= float(request.form['Total_Ct_Chng_Q4_Q1'])
        Avg_Utilization_Ratio= float(request.form['Avg_Utilization_Ratio'])
   
        prediction=model.predict([[Customer_Age,Gender,Dependent_count,Education_Level,Marital_Status,Income_Category,Card_Category,Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio]])
        if prediction== 0:
            res="stay"
        else:
            res="go"
        return render_template('index.html',prediction_text = res)

    else:
       return render_template('index.html',prediction_text = res)
if __name__=="__main__":
    app.run(debug=True)