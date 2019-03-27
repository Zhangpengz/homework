1、以容易理解的格式列出/home目录里面所有的以d开头的文件目录的大小

![img](https:////note.youdao.com/src/WEBRESOURCE60fa1346cc84dc9bd75bd01b6c57d844)

2、列出/home 目录中所有以”s”开头的目录。

![img](https:////note.youdao.com/src/WEBRESOURCEa22957d4e8b3810c63f9b49e9e8f47a1)

3、删除后缀名为.log 的所有，删除前逐一询问

![img](https:////note.youdao.com/src/WEBRESOURCE8a8d2d01938f68d8275821664146fdf9)

4、cp 命令 —n 和 -u的区别

-u 或 --update 使用这项参数之后，只会在源文件的修改时间(Modification Time)较目的文件更新时，或是名称相互对应的目的文件并不存在，才复制文件

复制文件，只有源文件file1较目的文件file2的修改时间新时，才复制文件

cp -u file1 file2

-p：除复制文件的内容外，还把修改时间和访问权限也复制到新文件中。

使用cp命令的-n参数即可跳过相同的文件 。

\--------------------- 

5、找你的用户目录下面的所有py文件,ls -l 查看他们的属性,然后把这些结果输入到一个文件之中

![img](https:////note.youdao.com/src/WEBRESOURCEc8b91a75e206d4d2b4ce64769e520c7f)



6、使用ls查看根目录 并且每行显示3个信息



![img](https:////note.youdao.com/src/WEBRESOURCE61370569802276ca1a9a13533bac3749)



7、查看所有进程信息，只查看前3行

![img](https:////note.youdao.com/src/WEBRESOURCE954c941c2dcce7d9eb6eadd49bc6b092)

8、分析以下问题，并给出解决方案

1. Mount is denied because the NTFS volume is already exclusively opened.

The volume may be already mounted, or another software may use it which could be identified for example by the help of the 'fuser' command.

NTFS卷被拒，因为NTFS卷已经完全打开

9、ssh 服务端口是多少,ssh免密登录方式的原理是什么

port 22

cd ~./ssh

ssh-keygen

ssh-copy-id

10、权限755代表什么权限,如果我想把所有的w权限去除应该使用什么命令

755代表本人拥有rwx权限，组内和其他人拥有rx权限。

使用chmod a-w 的命令