import urllib.request
from typing import List, Union
from numpy import ndarray, uint8

CODEMAP = ' 24578acdehkmnpqsuvxyz'


def make_request_for_data(url: str) -> bytes:
    return urllib.request.urlopen(url).read()


def compile_url(sid: Union[str, int]) -> str:
    return "https://api.vk.com/captcha.php?s=1&sid=%s" % sid


def symbols_from_array(array: List[ndarray]) -> str:
    return ''.join(CODEMAP[c] for c in uint8(array[-1][array[0]>0]))
