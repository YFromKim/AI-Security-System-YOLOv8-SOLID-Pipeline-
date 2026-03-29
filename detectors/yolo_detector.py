from ultralytics import YOLO
from core.interfaces import BaseDetector
import numpy as np

class YoloDetector(BaseDetector):
    def __init__(self, model_name="yolov8n.pt"):
        # Загружаем предобученную модель (n - nano, самая легкая)
        # Она автоматически скачается при первом запуске
        self.model = YOLO(model_name)

    def detect(self, frame: np.ndarray) -> list:
        # Делаем предсказание
        results = self.model(frame)[0]
        
        formatted_results = []
        
        # Переводим специфичный формат YOLO в наш стандартный список
        for box in results.boxes:
            # Координаты (x1, y1, x2, y2)
            coords = box.xyxy[0].tolist()
            x1, y1, x2, y2 = map(int, coords)
            
            # Вероятность (confidence)
            conf = float(box.conf[0])
            
            # Название класса (человек, машина и т.д.)
            cls_id = int(box.cls[0])
            label = results.names[cls_id]
            
            formatted_results.append((x1, y1, x2, y2, label, conf))
            
        return formatted_results