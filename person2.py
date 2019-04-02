import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 5550))
sock.send(b'1')
print(sock.recv(1024).decode())
nickName = input('input your nickname: ')
sock.send(nickName.encode())


def sendThreadFunc():
    while True:
        try:
            myword = input()
            sock.send(myword.encode())
            # print(sock.recv(1024).decode())
        except ConnectionAbortedError:
            print('服务器断开链接!')
        except ConnectionResetError:
            print('服务器关闭!')


def recvThreadFunc():
    while True:
        try:
            otherword = sock.recv(1024)
            if otherword:
                print(otherword.decode())
            else:
                pass
        except ConnectionAbortedError:
            print('服务器断开链接!')

        except ConnectionResetError:
            print('服务器关闭!')


th1 = threading.Thread(target=sendThreadFunc)
th2 = threading.Thread(target=recvThreadFunc)
threads = [th1, th2]

for t in threads:
    t.setDaemon(True)
    t.start()
t.join()