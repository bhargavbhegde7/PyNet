from socket import *

host = 'localhost' # '127.0.0.1' can also be used
port = 52004

sock = socket()
sock.connect((host, port))

while True:
    data = sock.recv(1024)
    print data
    sock.send(raw_input('enter msg : '))

sock.close()
