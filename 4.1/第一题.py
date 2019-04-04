import os
import socket

# __file__的意思是本Python文件在os中的绝对路径
# os。path。dirname是找到文件所属的文件夹名称
# os。path。join的意思是拼凑文件的路径
dir_name = os.path.dirname(__file__)
jpg_name = os.path.join(dir_name,'111.png')
jpg_name1 = os.path.join(dir_name,'111_copy.png')

# rb read binary
# r模式是read模式 普通字符串
# b''表示的是声明一个二进制的字符串对象

with open(jpg_name,'rb') as f:
    b_file = f.read()
# with open(jpg_name1,'wb') as f:
#     f.write(b_file)

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('127.0.0.1',60000)
ss.connect(addr)
ss.sendall(b_file)
ss.close()
print('链接已经完成')