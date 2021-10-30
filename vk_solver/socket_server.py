from threading import Thread
import socket
import struct

from . import solver


class Server(object):
    def __init__(self, bind: tuple[str, int], max_clients: int):
        self.socket = socket.socket()
        self.socket.bind(bind)
        self.socket.listen(max_clients)

        thread = Thread(target=self.listen)
        thread.start()
        thread.join()
    
    def listen(self):
        while True:
            client = Client(*self.socket.accept())

            thread = Thread(target=client.listen)
            thread.start()
            thread.join()


class Client(object):
    def __init__(self, user: socket.socket, addr):
        print(f"New client connected, IP: {addr[0]}:{addr[1]}")
        self.user = user

    def listen(self):
        while True:
            file = self.get_file()
            captcha = solver.solve(file)
            self.user.send(captcha.encode())
    
    def get_filesize(self) -> int:
        stream = bytes()
        recieved = 0

        while recieved < 8:
            chunk = self.user.recv(8 - recieved)
            stream += chunk
            recieved += len(chunk)
        
        filesize = struct.unpack("<Q", stream)[0]
        return filesize
    
    def get_file(self) -> bytes:
        size = self.get_filesize()
        file = bytes()
        recieved = 0

        while size > recieved:
            chunk = self.user.recv(1024)
            if chunk:
                recieved += len(chunk)
                file += chunk

        return file
