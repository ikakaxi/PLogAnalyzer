# PLogAnalyzer

## 使用方式：
1. 首先安装 http://slproweb.com/download/Win64OpenSSL-1_1_1n.msi ，安装时安装到默认的C盘路径不要变否则脚本会找不到对应的文件
   > win32OpenSSL-1_1_1n.exe未测试，提供下载地址请自行测试：
http://slproweb.com/products/Win32OpenSSL.html
2. 运行main.exe即可

## 打包独立应用的方式：
### windows：
1. 下载python2.7.10以上的版本（32位系统下载32位的，64位系统下载64位的，建议下载最新的python2版本即可）
2. 64位系统安装 http://slproweb.com/download/Win64OpenSSL-1_1_1n.msi ，安装时安装到默认的C盘路径不要变否则脚本会找不到对应的文件，如果是32位系统自行下载对应的win32OpenSSL-1_1_1n.exe
3. 安装pyelliptic1.5.10：
   > pip install https://github.com/mfranciszkiewicz/pyelliptic/archive/1.5.10.tar.gz#egg=pyelliptic
4. 安装pyinstaller：pip install pyinstaller==3.2.1
5. 运行pyinstaller mainGUI.py

### mac：
1. 下载 pyelliptic1.5.7：https://github.com/yann2192/pyelliptic/releases/tag/1.5.7
2. 解压 pyelliptic1.5.7，执行 python setup.py install 安装 pyelliptic1.5.7
   > 如果没权限，执行：sudo python setup.py install
3. 安装pyinstaller：pip install pyinstaller==3.2.1
4. 运行pyinstaller mainGUI.py