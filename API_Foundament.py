#API FOUNDAMENTS 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserInfo(BaseModel):
    age: int
    name: str
    city: str


@app.get("/customer")
def get_customer(customer_id: int):
    return {
        "customer_id": customer_id,
        "name": "suresh pun magar",
        "age": 20,
    }


@app.get("/info")
def get_info(age: int, name: str, city: str):
    return {
        "name": name,
        "city": city,
        "age": age,
    }


@app.post("/userinfo")
def post_info(info: UserInfo):
    return {
        "name": info.name,
        "age": info.age,
        "City": info.city,
    }