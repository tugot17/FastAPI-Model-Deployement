from .base_model import BaseModel
import numpy as np
from os.path import join, realpath, dirname

DEFAULT_WEIGHTS_PATH = join(
    dirname(realpath(__file__)), "weights", "DLV3_plus_efficientnet.pth"
)


class LungSegmentation(BaseModel):
    def __init__(self):
        pass

    def __call__(self, image_batch: np.ndarray) -> np.ndarray:
        pass
