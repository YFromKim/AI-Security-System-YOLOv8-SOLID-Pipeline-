import cv2
from core.pipeline import ObjectDetectionPipeline
from detectors.yolo_detector import YoloDetector
from actions.alarm_action import SafetyViolationAction
from actions.draw_action import DrawDetectionsAction


def main():
    # 1. Инициализация компонентов (Конструктор)
    detector = YoloDetector()
    
    # Теперь мы просто добавляем нужные действия в список
    actions = [
        SafetyViolationAction(),      # Сохраняет фото людей
        DrawDetectionsAction()   # Рисует рамки на кадре
    ]
    
    # 2. Создаем "Конвейер"
    pipeline = ObjectDetectionPipeline(detector, actions)
    
    # 3. Работа с видеопотоком
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret: break

        # ОДНА СТРОКА делает всю работу по детекции и обработке
        pipeline.process(frame)

        # Показываем результат (фрейм уже изменен внутри DrawDetectionsAction)
        cv2.imshow('Professional AI System', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()