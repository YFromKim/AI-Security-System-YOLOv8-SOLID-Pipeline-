class ObjectDetectionPipeline:
    def __init__(self, detector, actions):
        self.detector = detector
        self.actions = actions

    def process(self, frame):
        # 1. Сначала находим объекты
        results = self.detector.detect(frame)
        
        # 2. Потом прогоняем кадр через все действия (сохранение, отрисовка и т.д.)
        for action in self.actions:
            action.execute(frame, results)
            
        return results