from typing import Tuple
from PIL import Image
from io import BytesIO
import numpy as np

TImg = Image.Image


def make(picture: bytes) -> np.ndarray:
    picture = Image.open(BytesIO(picture))
    return reshape(resize(picture))


def resize(img: TImg, sizes: Tuple[int, int] = (128, 64)) -> TImg:
    return img.resize(sizes).convert('RGB')


def reshape(img: TImg) -> np.ndarray:
    shaped = np.array(img).reshape(1, -1)
    dims = np.expand_dims(shaped, axis=0)
    return dims / np.float32(255.0)
