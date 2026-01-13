from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI(title="ML Document Classifier")

vectorizer, model = pickle.load(open("model.pkl", "rb"))

class DocumentRequest(BaseModel):
    text: str

@app.get("/")
def health():
    return {"status": "ML Service Running"}

@app.post("/predict")
def predict(data: DocumentRequest):
    X = vectorizer.transform([data.text])
    prediction = model.predict(X)[0]
    return {"document_type": prediction}
@app.get("/health")
def health():
    return {"status": "ok"}
