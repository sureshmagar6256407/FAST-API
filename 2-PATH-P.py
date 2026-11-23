from fastapi import FastAPI  
app = FastAPI()

customer_info   =  {  
    101 : {"name":"suresh pun magar" ,"Risk":"Low" ,"score":0.89},
    102 : {"name":"nirmall mall" ,"Risk":"high" ,"score":0.9},
    103 : {"name":"Rahul budha" ,"Risk":"medium" ,"score":0.5}
}

@app.get("/customer/{customer_id}")
def get_customer_risk (customer_id : int) : 
    if customer_id not in customer_info : 
        return {"error" : f"{customer_id} not in customer info "}

    profile = customer_info[customer_id]
    return  { 
        "customer id" : customer_id  , 
        "name" : profile["name"] , 
        "Risk" : profile["Risk"] , 
        "score" : profile["score"]
    }

    
    
