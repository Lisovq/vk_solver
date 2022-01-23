from os import path
from typing import List, Union
from numpy import ndarray, float32
from onnxruntime import InferenceSession

MODELS_PATH = path.dirname(path.abspath(__file__))


class Base(object):
    def __init__(self, model_name: str, value_lambda):
        session = InferenceSession(path.join(
            MODELS_PATH, model_name + ".onnx"
        ))
        self.value_lambda = value_lambda
        self.inputs = session.get_inputs()
        self.run = session.run

    def process(self, array: Union[List[ndarray], ndarray]):
        return self.run(
            None, {
                value.name: self.value_lambda(array, pos)
                for pos, value in enumerate(self.inputs)
            }
        )


ctc = Base("ctc", lambda arr, pos: float32(arr[pos]))
captcha = Base("captcha", lambda arr, pos: arr[pos])

__all__ = ["ctc", "captcha"]
