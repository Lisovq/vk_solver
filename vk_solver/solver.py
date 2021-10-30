from typing import Union
from vk_solver.utils import sessions, image_funcs, other


def solve(arg: Union[str, int, bytes]) -> str:
    """ :param url: must be contains sid, url or bytes of captcha """
    if isinstance(arg, (bytes, int, str)) is False:
        raise TypeError(
            "Argument must be url, sid or bytes of captcha, "
            "not {%s : %s}" % (type(arg), arg)
        )
        
    if isinstance(arg, bytes) is False:
        if arg.isnumeric():
            arg = other.get_url(arg)
            
        if "://" not in arg:
            raise TypeError("Argument not url or cannot be converted to url")

        arg = other.request_data(arg) # fix

    image = image_funcs.get(arg)
    arrays = sessions.captcha_run(image)
    result = sessions.ctc_run(arrays)
    return other.get_symbols(result)
