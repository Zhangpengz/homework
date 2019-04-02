import socket
import os


# 和主机一样使用同样的网络和运输
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('0.0.0.0',41901)
client.connect(server_addr)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
n = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2737733418,2713695114&fm=26&gp=0.jpg'
client.send(n.encode())
msg = client.recv(1460)

print('收到服务端发过来的消息', msg.decode())


client.close()
print('链接已经完成')
