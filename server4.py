import socket
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('localhost', 5550))

sock.listen(5)
print('Server', socket.gethostbyname('localhost'), 'woring ...')

mydict = dict()
mylist = list()

# 把whatToSay传给除了exceptNum的所有人
def tellOthers(exceptNum, whatToSay):
    for c in mylist:
        if c.fileno() != exceptNum:
            try:
                c.send(whatToSay.encode())
            except:
                pass


def subThreadIn(myconnection, connNumber):
    nickname = myconnection.recv(1024).decode()
    mydict[myconnection.fileno()] = nickname
    mylist.append(myconnection)
    print('connection', connNumber, ' has nickname :', nickname)
    tellOthers(connNumber, '【系统提示：' + mydict[connNumber] + ' 进入聊天室】')
    while True:
        try:
            recvedMsg = myconnection.recv(1024).decode()
            if recvedMsg:
                print(mydict[connNumber], ':', recvedMsg)
                tellOthers(connNumber, mydict[connNumber] + ' :' + recvedMsg)

        except (OSError, ConnectionResetError):
            try:
                mylist.remove(myconnection)
            except:
                pass
            print(mydict[connNumber], 'exit, ', len(mylist), ' person left')
            tellOthers(connNumber, '【系统提示：' + mydict[connNumber] + ' 离开聊天室】')
            myconnection.close()
            return


while True:
    conn, addr = sock.accept()
    print('Accept a new connection', conn.getsockname(), conn.fileno())
    try:
        # connection.settimeout(5)
        buf = conn.recv(1024).decode()
        if buf == '1':
            conn.send(b'welcome to server!')

            # 为当前连接开辟一个新的线程
            mythread = Thread(target=subThreadIn, args=(conn, conn.fileno()))
            mythread.setDaemon(True)
            mythread.start()

        else:
            conn.send(b'please go out')
            conn.close()
    except:
        pass

