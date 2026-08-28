from fastapi import FastAPI  
app  = FastAPI()

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
