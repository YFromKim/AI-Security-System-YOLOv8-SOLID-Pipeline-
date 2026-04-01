from ultralytics import YOLO

# Загрузи свою обученную модель
model = YOLO("model/best.pt")

# Выведи словарь классов
print("Список классов в твоей модели:")
print(model.names)