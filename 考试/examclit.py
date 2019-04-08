import socket
from concurrent.futures import ThreadPoolExecutor
ss =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = ('127.0.0.1',9327)
ss.connect(addr)

def recv(ss):
    while 1:
        msg=ss.recv(65535)
        print(msg.decode())

def send(ss):
    while 1:
        msg = input('请输入')
        ss.send(msg.encode())

pools = ThreadPoolExecutor(max_workers=20)
from concurrent.futures import as_completed
function_list = [recv,send]
pools_list = list()
for i in function_list:
    pools_list.append(pools.submit(i,ss))
for i in as_completed(pools_list):
    i.result()


