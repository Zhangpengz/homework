import socket
ss = socket.socket()

addr = ('0.0.0.0',9527)
ss.bind(addr)

ss.listen()

response_headers = b"""
 HTTP/1.1 200 OK\r\n
 \r\n
 Helloworld
 """


while 1:
    conn,addr = ss.accept()
    print('你有新的链接{}'.format(addr))

    msg = conn.recv(65535)
    print(msg.decode())
    conn.send(response_headers)



