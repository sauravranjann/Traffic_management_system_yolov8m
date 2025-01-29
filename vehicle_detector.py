# vehicle_detector.py

from ultralytics import YOLO
import cv2

class VehicleDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_vehicles(self, frame):
        results = self.model(frame)
        return results