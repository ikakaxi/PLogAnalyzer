# PLogAnalyzer

## 使用方式：
1. 首先安装 http://slproweb.com/download/Win64OpenSSL-1_1_1n.msi ，安装时安装到默认的C盘路径不要变否则脚本会找不到对应的文件
   > win32OpenSSL-1_1_1n.exe未测试，提供下载地址请自行测试：
http://slproweb.com/products/Win32OpenSSL.html
2. 运行main.exe即可

## 打包独立应用的方式：
### windows：
1. 下载python2.7.10以上的版本（32位系统下载32位的，64位系统下载64位的，建议下载最新的python2版本即可）
2. 安装python2的Qt5：`pip install python-qt5`
2. 64位系统安装 http://slproweb.com/download/Win64OpenSSL-1_1_1n.msi ，安装时安装到默认的C盘路径不要变否则脚本会找不到对应的文件，如果是32位系统自行下载对应的win32OpenSSL-1_1_1n.exe
3. 在线安装`pyelliptic1.5.10`：
   > pip install https://github.com/mfranciszkiewicz/pyelliptic/archive/1.5.10.tar.gz#egg=pyelliptic
4. 如果网络不好无法在线安装`pyelliptic1.5.10`也可以直接使用resource里的下载包，下载包也是用上面的下载地址得到的，下载后解压，执行 `python setup.py install` 安装 `pyelliptic1.5.10`
5. 安装`pyinstaller：pip install pyinstaller==3.2.1`
6. 这里有个坑，你直接运行下面的步骤会报错，因为少了个文件，但是xlog里并没有告诉你少文件，所以需要把resource文件夹下面的libeay32.dll拷贝到C:\Windows\System32，如果是64位，则在C:\Windows\SysWOW64
7. 运行`pyinstaller -F -w mainGUI.py`

### mac：
> mac我用的是python3，因为我安装不上python2的Qt5

1. 安装python3的Qt5：`pip3 install PyQt5`
2. 在线安装`pyelliptic1.5.10`：
   > pip3 install https://github.com/mfranciszkiewicz/pyelliptic/archive/1.5.10.tar.gz#egg=pyelliptic
3. 如果网络不好无法在线安装`pyelliptic1.5.10`也可以直接使用resource里的下载包，下载包也是用上面的下载地址得到的，下载后解压，执行 `python3 setup.py install` 安装 `pyelliptic1.5.10`
   > 如果没权限，执行：sudo python3 setup.py install
3. 安装`pyinstaller：pip3 install pyinstaller`
4. 运行`pyinstaller -F -w mainGUI.py`