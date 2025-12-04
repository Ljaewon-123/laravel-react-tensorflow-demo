from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from tensorflow import keras
import json

app = FastAPI()

MAX_LENGTH = 200

# 모델 로드
model = keras.models.load_model("sentiment_model.h5")

# 단어 인덱스 로드
with open("word_index.json", "r", encoding="utf-8") as f:
    word_index = json.load(f)

def encode_review(review: str):
    words = review.lower().split()
    encoded = [word_index.get(word, 0) + 3 for word in words]
    padded = keras.preprocessing.sequence.pad_sequences(
        [encoded],
        maxlen=MAX_LENGTH,
        padding='post'
    )
    return padded

class ReviewRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(req: ReviewRequest):
    encoded = encode_review(req.text)
    prediction = model.predict(encoded)[0][0]
    sentiment = "positive" if prediction > 0.5 else "negative"

    return {
        "sentiment": sentiment,
        "score": float(prediction)
    }
