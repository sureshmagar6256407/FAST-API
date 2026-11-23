from fastapi import FastAPI , Security ,HTTPException , File ,UploadFile
from fastapi.middleware.cors  import CORSMiddleware  
from fastapi.security import APIKeyHeader 

app  = FastAPI()
app.add_middleware ( 
    CORSMiddleware , 
    allow_origins =["http://localhost:5173"] , 
    allow_methods  = ["*"] ,
    allow_headers  = ["*"]
)
api_pw  = "sureshpun2022"
api_key_box   = APIKeyHeader(name="X-API-Key")
def check_password(user_pwd : str  = Security(api_key_box)) : 
    if user_pwd != api_pw : 
        raise HTTPException ( 
            status_code= 403 , 
            detail="password milena"
        )
    return user_pwd

@app.post("/secure-predict",dependencies=[Security(check_password)])  
async def user_csv (file : UploadFile = File(...)) : 
    if not file.filename.endswith(".csv") : 
        raise HTTPException ( 
            status_code= 400 , 
            detail="Only csv file"
        )
    
    content  =  await file.read()
    lines  = content.decode("utf-8").splitlines()

    return { 
        "total_rows" : len(lines)
    }