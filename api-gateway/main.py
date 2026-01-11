from fastapi import FastAPI, UploadFile, File

app = FastAPI(title="AI Documentation Detection Hub")

@app.get("/")
def health_check():
    return {"status": "API Gateway is running"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File received successfully"
    }
