from socket import *
from thread import *
import os
import json

host = ''  #'localhost' or '127.0.0.1' or '' are all same
port = 52001
pwd = '.'
conn = None
addr = None



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

def sendFile(fileName):
    #fileName = fileName.lstrip()
    fileName = '/home/bhargav/sample_file.txt'
    print(fileName)
    f = open('/home/bhargav/sample_file.txt','rb')
    l = f.read(1024)
    print('Sending...')
    while (l):
       conn.send(l)
       #print('Sent ',repr(l))
       l = f.read(1024)
    f.close()
    conn.send('p00Pd0n3!')
    print('Done sending')

def clientThread(conn,addr):
    conn.send('Hi '+addr[0]+'! I am server '+host+'\n') #only string
    while True:
        data = conn.recv(1024) #bytes
        print data," by ",addr
        if data=='list':
            conn.send(getFiles(pwd))
        elif 'cd' in data:
            conn.send('change directory to'+data.replace("cd","",1))
        elif 'getfile' in data:
            conn.send('prepare')
            sendFile(data.replace("getfile","",1))
        else :
            conn.send('command not found')

#main function
if __name__ == '__main__':
    sock = socket()
    sock.bind((host, port))
    sock.listen(5) #5 number of clients can queue
    while True:
        conn, addr = sock.accept()
        start_new_thread(clientThread,(conn,addr))

    conn.close()
    sock.close()
