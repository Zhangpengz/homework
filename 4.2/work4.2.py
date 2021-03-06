import socket
from threading import Thread
conn_list = list()
def handle_msg(conn,addr):
    while 1:
        msg = conn.recv(65535)
        return_msg = ('{}用户发送{}'.format(addr, msg.decode()))
        for conn in conn_list:
            conn.send(return_msg.encode())



def conn_sever(addr):
    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.bind(addr)
    ss.listen(5)
    print('服务器已经启动')
    while 1:
        conn,addr=ss.accept()
        print('接收新链接{}'.format(addr))
        conn_list.append(conn)
        t = Thread(target=handle_msg,args=(conn,addr))
        t.start()

if __name__ == "__main__":
    addr = ('127.0.0.1',9521)
    conn_sever(addr)



