import urllib.request
from io import BytesIO
from warnings import warn
from typing import Optional
from os.path import dirname, abspath

import numpy as np
from PIL import Image
from onnxruntime import InferenceSession

codemap = ' 24578acdehkmnpqsuvxyz'


class sessions:
    MODELS = dirname(abspath(__file__)) + "/models/"
    ctc = InferenceSession(MODELS + "ctc.onnx")
    ctc_inputs = ctc.get_inputs()

    captcha = InferenceSession(MODELS + "captcha.onnx")
    captcha_inputs = captcha.get_inputs()

    @classmethod
    def captcha_run(cls, array: np.ndarray):
        return cls.captcha.run(
            None,
            {
                inp.name: array[pos]
                for pos, inp in enumerate(cls.captcha_inputs)
            }
        )
    
    @classmethod
    def ctc_run(cls, arrays: list[np.ndarray]):
        return cls.ctc.run(
            None,
            {
                inp.name: np.float32(arrays[pos])
                for pos, inp in enumerate(cls.ctc_inputs)
            }
        )


class image_funcs:
    @classmethod
    def get(cls, picture: bytes) -> np.ndarray:
        """ The method is made for ease to use """
        if isinstance(picture, bytes):
            picture = cls.make(picture)

        picture = cls.resize(picture)
        return cls.reshape(picture)

    def make(picture: bytes) -> Image.Image:
        return Image.open(BytesIO(picture))

    def resize(image: Image.Image) -> Image.Image:
        return image.resize((128, 64)).convert('RGB')
        
    def reshape(image: Image.Image) -> np.ndarray:
        shaped = np.array(image).reshape(1, -1)
        dims = np.expand_dims(shaped, axis=0)
        return dims/np.float32(255.)


class other:
    def request_data(url: str) -> bytes:
        return urllib.request.urlopen(url).read()
    
    def get_url(sid: str) -> str:
        return "https://api.vk.com/captcha.php?s=1&sid=" + sid

    def get_symbols(array: list[np.ndarray]) -> str:
        return ''.join(
            codemap[c]
            for c in np.uint8(
                array[-1][array[0]>0]
            )
        )
