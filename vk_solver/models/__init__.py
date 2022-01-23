from vk_solver.models.logics import ctc, captcha

def process(array):
    return ctc.process(
        captcha.process(array)
    )
