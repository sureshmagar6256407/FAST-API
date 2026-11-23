
from fastapi import FastAPI , HTTPException , BackgroundTasks 
from pydantic import BaseModel  
import asyncio 
import time  


app = FastAPI()

class UserRegister (BaseModel) : 
    user_name  : str  
    email : str  
    age : int  



def log_new_user(user_name : str , email:str) : 
    time.sleep(3)
    with open("user.text" ,"a") as f : 
        f.write(f"{user_name} - {email} \n")
    
    print(f"welcome {email} sent to ")
    

@app.post("/register")  
def fast (hey : UserRegister , background_task : BackgroundTasks) : 
    if hey.age < 18 :  
        raise HTTPException ( 
            status_code= 400  , 
            detail= "Age must be 18"
        )

    background_task.add_task(log_new_user , hey.user_name , hey.email)
    return {"message": "अकाउन्ट सफलतापूर्वक बन्यो!"}


