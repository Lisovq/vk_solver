from setuptools import setup


setup(
    author='Lisovq',
    author_email='lisov@internet.ru',

    name='vk_solver',
    version='1.0.0',
    description='VKontakte captcha solver',
    url="https://github.com/Lisovq/vk_solver",

    packages=['vk_solver'],
    python_requires=">=3.9",

    include_package_data = True,
    install_requires = ["Pillow", "onnxruntime", "numpy"],
    data_files=[('vk_solver',  ['vk_solver/models/captcha.onnx', 'vk_solver/models/ctc.onnx'])],
    entry_points={"console_scripts": ["vk-solver = vk_solver.cli:run"]}
)
