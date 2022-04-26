#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:刘海超

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class AboutGUI(QDialog):
    def __init__(self, ):
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        aboutEdit = QTextEdit()
        aboutEdit.setText("""查看日志操作步骤：
1. 点击“选择日志”文件
2. 如果日志被加密，输入公钥和私钥，选中“是否解密”
3. 点击开始分析按钮

生成公钥和私钥：
点击“生成公钥与私钥”按钮，跳转到生成公钥和私钥的页面，
点击被跳转页面中的生成按钮即可生成，注意保存好自己的私钥""")
        vbox.addWidget(aboutEdit)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle("使用说明")
        self.setGeometry(600, 400, 600, 400)
        self.setLayout(vbox)
