from fastapi import FastAPI, UploadFile, File
from inference import predict_image
import shutil
import os

app = FastAPI()

@app.post("/predict")
async def classify_image(file: UploadFile = File(...)):
    with open("temp.jpg", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    prediction = predict_image("temp.jpg")
    os.remove("temp.jpg")
    return {"prediction": prediction}
