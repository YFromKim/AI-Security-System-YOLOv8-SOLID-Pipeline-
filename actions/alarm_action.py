import cv2
import datetime
import os
from core.interfaces import BaseAction

class SavePersonAction(BaseAction):
    def __init__(self, output_folder="alarms"):
        self.output_folder = output_folder
        # Создаем папку для фото, если её нет
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def execute(self, frame, detections):
        for (x1, y1, x2, y2, label, conf) in detections:
            # Если нейронка увидела человека с уверенностью > 50%
            if label == "person" and conf > 0.5:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{self.output_folder}/person_{timestamp}.jpg"
                
                # Сохраняем кадр на диск
                cv2.imwrite(filename, frame)
                print(f"[ALARM] Человек обнаружен! Фото сохранено в {filename}")