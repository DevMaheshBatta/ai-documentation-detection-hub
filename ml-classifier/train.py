import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

data = {
    "text": ["invoice total amount", "resume experience python", "bank statement debit"],
    "label": ["invoice", "resume", "bank"]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

pickle.dump((vectorizer, model), open("model.pkl", "wb"))
print("Model trained & saved")
