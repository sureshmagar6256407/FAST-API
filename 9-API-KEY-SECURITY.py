from fastapi import FastAPI , Security , HTTPException  
from fastapi.security import APIKeyHeader

app  = FastAPI()

api_pw="sureshpun2022"
api_key_box  = APIKeyHeader(name="X-API-Key")

def check_password(user_key : str  = Security(api_key_box) ) : 
    if user_key != api_pw : 
        raise HTTPException (status_code= 403, detail="Password miilena")
    
@app.get("/home")
def home() : 
    return {"message" : "This is  a Free everyone"}

@app.get("/secret" , dependencies=[Security(check_password)])
def secret() : 
    return{"message" : "This is  paid"}