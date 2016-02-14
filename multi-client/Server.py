from socket import *
from thread import *

host = ''  #'localhost' or '127.0.0.1' or '' are all same
port = 52004

sock = socket()
sock.bind((host, port))
sock.listen(5) #5 number of clients can queue

def clientthread(conn,addr):
    conn.send('Hi '+addr[0]+'! I am server '+host+'\n') #only string
    while True:
        data = conn.recv(1024) #bytes
        print data," by ",addr
        if data=='list':
            conn.send('list of files')
        else :
            conn.send('command not found')


while True:
    conn, addr = sock.accept()
    start_new_thread(clientthread,(conn,addr))

conn.close()
sock.close()
