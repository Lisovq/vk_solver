import os.path
import socket
import struct

path_to_file = "/home/user/captcha/vk/1.jpg"

sock = socket.socket()
sock.bind(("localhost", 5000))

size = os.path.getsize(path_to_file)
bytes_size = struct.pack("<Q", size)
sock.send(bytes_size) # Send packed file size

fp = open(path_to_file, "rb")

while chunk := fp.read(1024):
    sock.send(chunk)

print("File send complete")
