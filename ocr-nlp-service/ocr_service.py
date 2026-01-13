from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image
import pdfplumber
import io

app = FastAPI(title="OCR + NLP Service")

@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    text = ""
    content = await file.read()

    # PDF
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"

    # Image
    elif file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        image = Image.open(io.BytesIO(content))
        text = pytesseract.image_to_string(image)

    # TXT or other
    else:
        text = content.decode("utf-8", errors="ignore")

    # Clean text
    text = text.replace("\n", " ").strip()

    return {"filename": file.filename, "extracted_text": text}
@app.get("/health")
def health():
    return {"status": "ok"}
