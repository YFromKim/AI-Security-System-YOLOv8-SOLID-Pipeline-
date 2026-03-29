from core.interfaces import BaseDetector
import random

class MockDetector(BaseDetector):
    """
    Детектор-пустышка, который рисует случайный квадрат.
    Нужен, чтобы проверить, как работает наш пайплайн.
    """
    def detect(self, frame: np.ndarray) -> list:
        # Просто имитируем, что нашли что-то в центре экрана
        h, w, _ = frame.shape
        return [(100, 100, 200, 200, "test_object", 0.99)]