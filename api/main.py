from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI(title="Auto Damage Segmentation API")

model = YOLO("../model/best.pt")

@app.get("/")
def root():
    return {"message": "Auto Damage Segmentation API ishlamoqda!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    img_array = np.array(image)

    results = model(img_array)[0]

    detections = []
    if results.masks is not None:
        for i, box in enumerate(results.boxes):
            detections.append({
                "class": results.names[int(box.cls)],
                "confidence": round(float(box.conf), 3),
                "bbox": box.xyxy[0].tolist()
            })

    return JSONResponse({
        "total_detected": len(detections),
        "detections": detections
    })
