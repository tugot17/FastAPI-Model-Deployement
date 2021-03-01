from abc import ABC, abstractmethod
import numpy as np


class BaseModel(ABC):
    @abstractmethod
    def __call__(self, image_batch: np.ndarray) -> np.ndarray:
        pass
