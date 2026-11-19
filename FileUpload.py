from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI()

# उदाहरण १: जुनसुकै फाइल अपलोड गर्ने र त्यसको जानकारी हेर्ने
@app.post("/upload-any")
async def upload_any_file(file: UploadFile = File(...)):
    # १. फाइल भित्रको डेटा पढ्ने (async भएकोले await प्रयोग गरिएको)
    contents = await file.read()
    
    # २. फाइलको जानकारी फिर्ता पठाउने
    return {
        "file_ko_naam": file.filename,
        "file_ko_type": file.content_type,
        "file_size_bytes": len(contents)
    }


# उदाहरण २ (ML को लागि): CSV फाइल मात्र लिने र भित्रको डेटा पढ्ने
@app.post("/upload-csv")
async def upload_csv_file(file: UploadFile = File(...)):
    # १. चेक गर्ने: फाइलको नामको पछाडि .csv छ कि छैन?
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400, 
            detail="गल्ती भयो! कृपया .csv फाइल मात्र पठाउनुहोस्।"
        )
    
    # २. फाइलको डेटा (Bytes) पढ्ने
    contents = await file.read()
    
    # ३. Bytes लाई सामान्य अक्षर (String) मा बदल्ने
    text_data = contents.decode("utf-8")
    
    # ४. प्रत्येक लाइनलाई अलग-अलग लिस्टमा राख्ने
    lines = text_data.splitlines()
    
    return {
        "message": "CSV फाइल सफलतापूर्वक पढियो!",
        "total_rows": len(lines),
        "data": lines
    }