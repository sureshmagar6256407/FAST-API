from fastapi import FastAPI  
from pydantic import BaseModel
app  = FastAPI()
@app.get("/")
def Home () : 
    return {"Message" : "this is a activate"}
    

@app.get('/about')
def about () : 
    return {"Message" :"this is a about page"}

@app.get("/contact")
def contact () : 
    return {"password" :"suresh pun magar"}   



class Require (BaseModel):  
    name : str  
    age : int  
    income : float  
    experience_leve : int  
    loan_amount : float  



@app.post ("/loan_predict")
def predict_value  (info : Require) : 
    if info.age >= 18 and info.income >= 100000 and info.experience_leve  > 2 : 
        decision  = "approval"
    else  : 
        decision   = "declined"

    return { 
        "name" : info.name , 
        "age" : info.age , 
        "loan_amount" : info.loan_amount  , 
        "decision" : decision  
    }