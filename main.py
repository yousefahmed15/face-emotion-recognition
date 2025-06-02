import cv2
from ultralytics import YOLO
from PIL import Image

model = YOLO("best.pt")
results =model.predict(source="0", show=True)