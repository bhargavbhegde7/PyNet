from socket import *
from thread import *
import os
import json

host = ''  #'localhost' or '127.0.0.1' or '' are all same
port = 52000
pwd = '.'

sock = socket()
sock.bind((host, port))
sock.listen(5) #5 number of clients can queue

#returns json string with files and directories
# {
#     files : ['a.txt','b.java','c.m','d.mp4'],
#     directories : ['abc','fds','ttrr']
# }
def getFiles(path):
    jsonList = {}
    files=[]
    directories=[]
    allItems = os.listdir(path)
    for item in allItems:
        if os.path.isdir(item):
            directories.append(item)
        else :
            files.append(item)
    jsonList['files'] = files
    jsonList['directories'] = directories
    return json.dumps(jsonList)

def clientThread(conn,addr):
    conn.send('Hi '+addr[0]+'! I am server '+host+'\n') #only string
    while True:
        data = conn.recv(1024) #bytes
        print data," by ",addr
        if data=='list':
            conn.send(getFiles(pwd))
        elif 'cd' in data:
            conn.send('change directory to'+data.replace("cd","",1))
        else :
            conn.send('command not found')

#main program :
while True:
    conn, addr = sock.accept()
    start_new_thread(clientThread,(conn,addr))

conn.close()
sock.close()
