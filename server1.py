import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('0.0.0.0', 41901)
server.bind(server_addr)
print('服务器已经开启')
server.listen()
BASE_DIR = os.path.dirname(os.path.abspath('/Desktop/cs'))
while 1:
    try:
       conn, conn_addr = server.accept()
    except Exception:
        break

    while True:
        try:
           msg = conn.recv(1460)
           if not msg:
               break

           msg = msg.decode()

           print('收到{}发送过来的消息:{}'.format(conn_addr,msg))

           return_msg = '已经收到你的消息--->' + msg

           conn.send(return_msg.encode())

           filename = '123.jpg'
           path = os.path.join(BASE_DIR, filename)
           f = open(path, 'ab')

           data=conn.recv(5000)
           f.write(msg)

           f.close()
           print(msg)

        except Exception:
            break
    conn.close()
    print('{}的连接已经断开'.format(conn_addr))
server.close()
print('服务器已经结束')
