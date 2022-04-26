#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:刘海超

from lib import gen_key as GenKey
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class KeysGUI(QDialog):
    def __init__(self, ):
        QWidget.__init__(self)
        self.initUI()

    def createKeyAction(self, privateKeyEdit, publicKeyEdit):
        privateKey, publicKey = GenKey.createPrivateKeyAndPublicKey()
        print(privateKey)
        print(publicKey)
        privateKeyEdit.setText(privateKey)
        publicKeyEdit.setText(publicKey)

    def initUI(self):
        grid = QGridLayout()
        grid.setVerticalSpacing(5)
        grid.setHorizontalSpacing(5)
        grid.addWidget(QLabel("私钥"), 1, 0)
        privateKeyEdit = QTextEdit()
        grid.addWidget(privateKeyEdit, 1, 1)
        grid.addWidget(QLabel("公钥"), 2, 0)
        publicKeyEdit = QTextEdit()
        grid.addWidget(publicKeyEdit, 2, 1)
        createKeys = QPushButton("生成")
        createKeys.clicked.connect(lambda: self.createKeyAction(privateKeyEdit, publicKeyEdit))
        grid.addWidget(createKeys, 0, 0)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle("生成私钥和公钥")
        self.setGeometry(600, 400, 400, 200)
        self.setLayout(grid)
