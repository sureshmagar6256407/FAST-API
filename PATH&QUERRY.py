

from builtins import int
from fastapi import FastAPI

app = FastAPI()

# path parameter
customer_risk = {
    101: {"name": "suresh", "age": 20, "address": "kathmandu"},
    102: {"name": "tekam", "age": 30, "address": "ghorahi"},
    103: {"name": "rahul", "age": 15, "address": "khalanga"},
}

@app.get("/customer/{customer_id}")
def customer_risk_analysis(customer_id: int):
    if customer_id not in customer_risk : 
        return {"error" : f"{customer_id} not in the customer risk info"}

    profile = customer_risk[customer_id]

    return { 
        "name":profile.get("name"),  
        "age":profile.get("age"),  
        "address":profile.get("address")
    }  



@app.get("/predict/{version_model}/customer/{customer_name}")
def show_info (version_model:str , customer_name:str) : 
    return  {  
        "version_model" : version_model , 
        "customer_name" :customer_name
    }


# # QUERRY PATH  

all_customer =  [ 
    {"id":101,"name":"suresh" ,"city":"kathmandu","risk":"low"},
    {"id":102,"name":"prabes" ,"city":"ghorahi","risk":"low"},
    {"id":103,"name":"nirmall" ,"city":"kathmandu","risk":"low"},
    {"id":104,"name":"tekam" ,"city":"rukum","risk":"high"},
    {"id":105,"name":"rahul" ,"city":"chiwan","risk":"low"}
]

@app.get("/customers")
def get_customers(city:str , risk:str) : 
    filtered = [ 
        c for c in all_customer 
        if c["city"] == city and c["risk"] == risk 
    ]

    return { 
        "city" : city  , 
        "risk":risk , 
        "count" : len(filtered),
        "result":filtered
    }
