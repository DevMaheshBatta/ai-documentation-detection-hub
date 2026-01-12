from fastapi import FastAPI, UploadFile, File
import requests
import io


app = FastAPI(title="API Gateway")
OCR_URL = "http://127.0.0.1:8002/extract"
ML_URL = "http://127.0.0.1:8001/predict"

@app.get("/")
def health():
    return {"status": "API Gateway Running"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")

    response = requests.post(ML_URL, json={"text": text})
    result = response.json()

    return {
        "filename": file.filename,
        "prediction": result["document_type"]
    }
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    
    # Send file to OCR
    ocr_response = requests.post(OCR_URL, files={"file": (file.filename, io.BytesIO(content))})
    extracted_text = ocr_response.json()["extracted_text"]

    # Send extracted text to ML
    ml_response = requests.post(ML_URL, json={"text": extracted_text})
    prediction = ml_response.json()["document_type"]

    return {
        "filename": file.filename,
        "extracted_text": extracted_text,
        "prediction": prediction
    }