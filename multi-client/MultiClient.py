from socket import *

host = 'localhost' # '127.0.0.1' can also be used
port = 52001

sock = socket()
sock.connect((host, port))
fileName = ''

def receiveFile(fname):
    with open(fname, 'wb') as f:
        print 'file opened'
        while True:
            print('receiving data...')
            data = sock.recv(1024)
            #print('data=%s', (data))
            if not data or data == 'p00Pd0n3!':
                print(data)
                break
            f.write(data)
    f.close()
    print('transfer successful')

while True:
    data = sock.recv(1024)
    print data
    if data == 'prepare':
        receiveFile(fileName)
    message = raw_input('enter msg : ')
    if 'getfile' in message:
        fileName = message.replace("getfile","",1)
    sock.send(message)

sock.close()
