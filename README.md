VK Captcha Solver
-------------
Это ревью [другой](https://github.com/DedInc/vk_captchasolver) библиотеки.
Заточено исключительно под личные нужды.
Python3.9+

Можно использовать через CLI (vk-solver -h) и также возможна работа через сокет-сервер.
В examples/ лежит скромный пример клиента для сокет-сервера солвера

Использованные сторонние библиотеки:
* Pillow
* numpy
* onnxruntime

Для работы с сетью использовался urllib, socket & threading