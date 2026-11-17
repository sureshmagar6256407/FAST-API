from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import asyncio  # async भित्र समय कुर्नको लागि
import time     # सामान्य (sync) background फङ्सन भित्र समय कुर्नको लागि

app = FastAPI()

# युजरले पठाउने डेटाको ढाँचा (Pydantic Model)
class OrderRequest(BaseModel):
    customer_name: str
    email: str
    item_name: str
    price: float


# ==========================================
# भाग १: Async / Await को पूरा उदाहरण
# ==========================================
# मानौँ हामीले बाहिरी बैंकको सर्भरबाट पेमेन्ट चेक गर्दैछौँ (जसलाई ३ सेकेन्ड लाग्छ)
async def check_payment_gateway(amount: float):
    print("🔄 बैंकको सर्भरसँग कनेक्ट हुँदैछ...")
    await asyncio.sleep(3)  # ३ सेकेन्ड कुर्छ, तर अरू युजरको काम रोक्दैन
    print("✅ पेमेन्ट भेरिफाई भयो!")
    return True

@app.post("/verify-payment")
async def verify_payment(amount: float):
    # माथिको async फङ्सनलाई कल गर्दा अगाडि 'await' लेख्नैपर्छ
    is_paid = await check_payment_gateway(amount)
    
    if is_paid:
        return {"status": "Success", "message": f"रु. {amount} प्राप्त भयो।"}
    return {"status": "Failed"}


# ==========================================
# भाग २: BackgroundTasks को पूरा उदाहरण
# ==========================================
# पछाडि (Background मा) चल्ने फङ्सनहरू:
def save_order_receipt(order: OrderRequest):
    time.sleep(4)  # मानौँ रसिद फाइलमा लेख्न ४ सेकेन्ड लाग्छ
    with open("orders_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Name: {order.customer_name} | Item: {order.item_name} | Price: {order.price}\n")
    print(f"📄 [Background] {order.customer_name} को रसिद orders_log.txt मा सेभ भयो!")

def send_confirmation_email(email: str, item: str):
    time.sleep(2)  # मानौँ इमेल पठाउन २ सेकेन्ड लाग्छ
    print(f"📧 [Background] {email} मा '{item}' अर्डरको इमेल पठाइयो!")

# मुख्य API रुट (यहाँ दुवै Background कामहरू जोडिएका छन्)
@app.post("/place-order")
def place_order(order: OrderRequest, background_tasks: BackgroundTasks):
    # १. पहिलो काम Background मा थप्ने (रसिद सेभ गर्ने)
    background_tasks.add_task(save_order_receipt, order)
    
    # २. दोस्रो काम पनि Background मा थप्ने (इमेल पठाउने) - जतिवटा पनि थप्न मिल्छ!
    background_tasks.add_task(send_confirmation_email, order.email, order.item_name)
    
    # ३. युजरलाई ०.१ सेकेन्डमै तुरुन्तै उत्तर पठाउने (६ सेकेन्ड कुर्नु पर्दैन)
    return {
        "status": "Order Confirmed!",
        "message": f"धन्यवाद {order.customer_name}, तपाईंको {order.item_name} अर्डर भयो। रसिद इमेलमा आउँदैछ।"
    }



#ASYNC / AWAIT 

from fastapi import FastAPI
import asyncio  # async भित्र समय कुर्न र सँगसँगै काम चलाउन यो चाहिन्छ

app = FastAPI()

# १. बाहिरी सर्भरबाट मौसमको डेटा तान्ने नक्कली फङ्सन (मानौँ इन्टरनेटबाट आउन ३ सेकेन्ड लाग्छ)
async def fetch_weather_from_api(city: str):
    print(f"🌍 {city} को मौसम इन्टरनेटबाट तानिँदैछ...")
    await asyncio.sleep(3)  # वेटरले किचेनमा अर्डर दिएर अरू काम गर्न गयो
    return {"city": city, "temp": "22°C", "condition": "Sunny"}

# २. अर्को बाहिरी सर्भरबाट समाचार तान्ने फङ्सन (यसलाई २ सेकेन्ड लाग्छ)
async def fetch_news_from_api(city: str):
    print(f"📰 {city} को समाचार तानिँदैछ...")
    await asyncio.sleep(2)
    return [f"{city} मा आज मौसम सफा छ", f"{city} मा प्रविधिको विकास हुँदैछ"]


# ३. मुख्य API रुट (यहाँ दुवै काम सँगसँगै चलाउने जादु हेर!)
@app.get("/dashboard/{city}")
async def get_city_dashboard(city: str):
    # तरिका A: एक-एक गरेर पर्खिने (यसलाई ३ + २ = ५ सेकेन्ड लाग्छ)
    # weather = await fetch_weather_from_api(city)
    # news = await fetch_news_from_api(city)

    # तरिका B (प्रो लेभल): asyncio.gather() ले दुवै काम एकैपटक सुरु गर्छ! (जम्मा ३ सेकेन्डमै सकिन्छ!)
    weather, news = await asyncio.gather(
        fetch_weather_from_api(city),
        fetch_news_from_api(city)
    )

    return {
        "city": city,
        "weather_info": weather,
        "latest_news": news
    }



#BACKGROUND TASK 

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


