
from fastapi import FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader

app = FastAPI()

# ==========================================
# १. CORS सेटअप (React फ्रन्टएन्डलाई अनुमति दिने)
# ==========================================
origins = [
    "http://localhost:3000",  # Create React App को लागि
    "http://localhost:5173",  # Vite + React को लागि
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # माथिका २ ठेगानालाई मात्र छिर्न दिने
    allow_credentials=True,
    allow_methods=["*"],         # GET, POST, आदि सबै चल्ने
    allow_headers=["*"],         # सबै हेडरहरू चल्ने
)

# ==========================================
# २. API Key सुरक्षा गार्ड (Security Guard)
# ==========================================
SECRET_API_KEY = "nepal-ai-2026"  # हाम्रो गोप्य साँचो
api_key_header = APIKeyHeader(name="X-API-Key")

# यो फङ्सनले साँचो जाँच गर्छ
def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != SECRET_API_KEY:
        raise HTTPException(
            status_code=403,
            detail="पहुँच अस्वीकृत! गलत API Key पठाउनुभयो।"
        )
    return api_key

# ==========================================
# ३. रुटहरू (Public vs Protected)
# ==========================================

# यो खुल्ला रुट हो — जोसुकैले हेर्न सक्छ (साँचो चाहिँदैन)
@app.get("/")
def home():
    return {"message": "स्वागत छ! यो खुल्ला पेज हो।"}

# यो सुरक्षित ML रुट हो — 'verify_api_key' पास नभई भित्र छिर्न पाइँदैन!
@app.post("/predict-secret", dependencies=[Security(verify_api_key)])
def predict_secret(house_area: float):
    price = house_area * 15000
    return {
        "status": "Authorized Access",
        "predicted_price": price
    }