import socket
from threading import Thread
ss = socket.socket()
addr = ('127.0.0.1',9521)
ss.connect(addr)

def recv(ss):
    while 1:
        msg = ss.recv(65535)
        print(msg.decode())

def send(ss):
    while 1:
        words =input('请输入')
        ss.send(words.encode())

t1 = Thread(target=send,args=(ss,))
t2 = Thread(target=recv,args=(ss,))
t1.start()
t2.start()
t1.join()
t2.join()