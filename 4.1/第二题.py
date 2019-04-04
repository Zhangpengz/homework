import socket
def get(name):
    import os
    dir_name = os.path.dirname(__file__)
    # jpg_name = dir_name + '/' + '3_1.jpeg'
    root_dir = os.path.dirname(dir_name)
    download_name = os.path.join(root_dir,'download')
    jpg_name = os.path.join(download_name,'{}.html'.format(name))
    headers_name = os.path.join(dir_name,'hearder.txt')
    ss = socket.socket()
    addr = ('180.97.33.108',443)
    ss.connect(addr)
    with open(headers_name,'rb') as f:
        b_file = f.read()

    headers = b_file

    ss.send(headers)
    print('send ok')
    res = b""
    while 1:
        msg = ss.recv(65535)
        print(len(msg) / 8)
        print('recv ok')
        if not msg:
            break
        res += msg

    # print(res.decode())
    res = res.decode()
    res_list = res.split('\r\n\r\n',1)

    html = res_list[0]


    with open(jpg_name,'w') as f:
        f.write(html)
if __name__ == '__main__':
    for i in range(10):
        i = str(i)
        get(i)
