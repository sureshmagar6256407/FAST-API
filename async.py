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