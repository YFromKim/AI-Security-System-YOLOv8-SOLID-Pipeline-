# actions/alarm_action.py
import cv2
import os
from datetime import datetime
from core.interfaces import BaseAction

class SafetyViolationAction(BaseAction):
    def __init__(self, output_dir="violations"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def execute(self, frame, detections):
        # Список "тревожных" классов (кто нарушает правила)
        violations = ['NO-Hardhat', 'NO-Mask', 'NO-Safety Vest']
        
        found_violation = False
        current_labels = []

        for (x1, y1, x2, y2, label, conf) in detections:
            if label in violations:
                found_violation = True
                current_labels.append(label)

        if found_violation:
            # Сохраняем скриншот нарушения
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            labels_str = "_".join(current_labels)
            filename = f"{self.output_dir}/alert_{timestamp}_{labels_str}.jpg"
            
            cv2.imwrite(filename, frame)
            print(f"[ALARM] Нарушение: {current_labels}. Фото сохранено: {filename}")