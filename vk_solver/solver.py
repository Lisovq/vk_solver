from typing import Union
from vk_solver.utils import (
    compile_url,
    symbols_from_array,
    make_request_for_data,
)
from vk_solver import image, models


def solve(arg: Union[str, int, bytes]) -> str:
    """ :param url: must be contains sid, url or image(bytes) of captcha """
        
    if isinstance(arg, bytes) is False:
        if isinstance(arg, int) or arg.isnumeric():
            arg = compile_url(arg)
            
        if "://" not in arg:
            raise TypeError("Argument not url or cannot be converted to url")

        arg = make_request_for_data(arg)

    array = image.make(arg)
    result = models.process(array)
    return symbols_from_array(result)
