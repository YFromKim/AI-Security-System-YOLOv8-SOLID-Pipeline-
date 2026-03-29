from abc import ABC, abstractmethod
import numpy as np

class BaseDetector(ABC):
    @abstractmethod
    def detect(self, frame: np.ndarray) -> list:
        pass

class BaseAction(ABC):  # <-- ДОБАВЬ ЭТОТ КЛАСС
    @abstractmethod
    def execute(self, frame: np.ndarray, detections: list):
        pass