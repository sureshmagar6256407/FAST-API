from fastapi import FastAPI
from pydantic import BaseModel  
app  = FastAPI()


class LoanApproval  (BaseModel) : 
    name : str
    age : int 
    income : float  
    loan_amount :float  
    emplyeement_years :int


@app.post('/preict')
def predict_loan(application:LoanApproval) : 
    approved  =  [ 
        application.income > 50000 and  application.emplyeement_years >   2 and  application.age >= 21
    ]
    return { 
        "application name": application.name  , 
        "loan_amount"  : application.loan_amount  ,  
        "decision" : "approved" if approved else "rejected" , 
        "reveiew_income" : application.income
    }