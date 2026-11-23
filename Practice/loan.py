from fastapi import FastAPI
from pydantic import BaseModel

app  = FastAPI()

class LoanAplicaton (BaseModel): 
    age :int 
    income:float  
    loan_amount :float  
    employee_years:int

@app.post("/predict")
def predict_loan (application:LoanAplicaton) : 
    if application.income >= 50000 and application.employee_years > 3 :
        decision = "approved"
    else : 
        decision ="reject"

    return { 
        "application_age":application.age ,
        "Decision":decision
    }