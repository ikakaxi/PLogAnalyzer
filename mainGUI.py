#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:刘海超
# 参考：
# 控件：http://code.py40.com/pyqt5/26.html#title-0
# QTableWidget：https://blog.csdn.net/jia666666/article/details/81627589
# QTableWidget：http://www.edbiji.com/doccenter/showdoc/188/nav/3329.html

from PyQt5.QtGui import *
from lib.logItem import *
from keysGUI import *
from aboutGUI import *
import sys
import os
import codecs
# from lib.py2 import decode_mars_crypt_log_file as crypt, decode_mars_nocrypt_log_file as nocrypt
from lib.py3 import decode_mars_crypt_log_file as crypt, decode_mars_nocrypt_log_file as nocrypt

levelIndex = 0
tagIndex = 1
dateIndex = 2
positionIndex = 3
messageIndex = 4
tagFilterAll = "all"
maxWidth = 0
maxLength = 0


class MainGUI(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.decode = False
        self.headerList = ["等级", "tag", "时间", "调用位置", "message"]
        self.columnCount = len(self.headerList)
        self.initUI()

    # 是否解密
    def decodeChangeAction(self, state):
        self.decode = (state == Qt.Checked)

    # 开始分析
    def startAnalyzerAction(self, table, publicKey, privateKey):
        if self.decode:
            result = crypt.main([self.logEdit.text()], publicKey, privateKey)
        else:
            result = nocrypt.main([self.logEdit.text()])
        if result is None:
            try:
                self.allLogItemList = self.readFile(table, self.logEdit.text())
                self.fillTableWidget(table, self.allLogItemList)
                self.fillTagFilterQComboBox(table, self.allLogItemList)
            except UnicodeDecodeError:
                QMessageBox(QMessageBox.Warning, "提示", "解析失败，请检查是否选错加密选项").exec_()
            else:
                # 没有异常发生什么都不做
                None
        else:
            QMessageBox(QMessageBox.Warning, "提示", "解析失败").exec_()

    # 填充过滤tag数据
    def fillTagFilterQComboBox(self, table, logItemList):
        self.tagFilterQComboBox.clear()
        self.tagFilterQComboBox.addItem(tagFilterAll)
        for logItem in logItemList:
            if self.tagFilterQComboBox.findText(logItem.tag) >= 0:
                continue
            self.tagFilterQComboBox.addItem(logItem.tag)
        self.qComboBoxAdjustItemWidth(self.tagFilterQComboBox)

    # 动态设置过滤tag宽度
    def qComboBoxAdjustItemWidth(self, tagFilterQComboBox):
        global maxWidth
        global maxLength
        maxWidth = 0
        maxLength = 0
        for i in range(tagFilterQComboBox.count()):
            textLength = len(tagFilterQComboBox.itemText(i))
            if maxLength < textLength:
                maxLength = textLength
                # 获取字体的磅值
                ptVal = tagFilterQComboBox.font().pointSize()
                maxWidth = maxLength * ptVal
        # 1.25是windows的缩放，这里默认设置1.25，这里不判断系统类型了不然太麻烦了
        tagFilterQComboBox.setFixedWidth(maxWidth * 1.25)

    # 根据tag过滤显示表格数据
    def filterTable(self, table):
        if (self.tagFilterQComboBox.currentText() == tagFilterAll):
            self.fillTableWidget(table, self.allLogItemList)
            return
        filterLogItemList = []
        for logItem in self.allLogItemList:
            if (logItem.tag == self.tagFilterQComboBox.currentText()):
                filterLogItemList.append(logItem)
        self.fillTableWidget(table, filterLogItemList)

    # 根据行数据创建一个LogItem实例
    def createLogItem(self, line):
        strs = line.split(";")
        # D;bluetooth;[2022-04-22 15:37:52:637];(MainActivity.kt:22);我是蓝牙日志
        return LogItem(strs[levelIndex],
                       strs[tagIndex],
                       strs[dateIndex],
                       strs[positionIndex],
                       strs[messageIndex])

    # 读文件，并返回读取的数据列表
    def readFile(self, table, logFilePath):
        _logFilePath = logFilePath + ".log"
        with codecs.open(_logFilePath, encoding='utf-8') as f:
            logItemList = []
            for line in f:
                _line = line.strip('\n')
                logItemList.append(self.createLogItem(_line))
            return logItemList

    # 打开xlog后缀的日志文件
    def selectFile(self):
        fname = QFileDialog.getOpenFileName(self, '选择日志文件', os.getcwd(), "xlog文件 (*.xlog)")
        if fname[0]:
            self.logEdit.setText(fname[0])

    # 填充表格数据
    def fillTableWidget(self, table, logItemList):
        table.clearContents()
        table.setRowCount(len(logItemList))
        # 设置垂直方向的表头标签
        table.setVerticalHeaderLabels(map(str, range(len(logItemList))))
        for row in range(len(logItemList)):
            for column in range(self.columnCount):
                table.setItem(row, column, QTableWidgetItem(logItemList[row].getText(column)))

    # 创建一个表格widget
    def createTableWidget(self):
        table = QTableWidget()
        # 设置只可以单选，可以使用ExtendedSelection进行多选
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        # 设置不可选择单个单元格，只可选择一行
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置表格列数
        table.setColumnCount(len(self.headerList))
        # 设置表头文字
        table.setHorizontalHeaderLabels(self.headerList)
        # 设置水平方向表格为自适应的伸缩模式
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表头可以自动排序
        table.setSortingEnabled(True)
        return table

    # 初始化UI
    def initUI(self):
        vBox = QVBoxLayout()
        # 创建日志表格控件
        table = self.createTableWidget()
        # 创建用户配置信息控件
        config = self.createConfigLayout(table)
        # 添加辅助功能
        hbox = self.createHelperLayout(table)
        # 添加所有控件到页面
        vBox.addLayout(config)
        vBox.addLayout(hbox)
        vBox.addWidget(table)
        self.setLayout(vBox)
        self.setGeometry(500, 300, 800, 500)
        self.setWindowTitle("plog日志分析器")
        self.setWindowIcon(QIcon('lib/logo.ico'))
        self.show()

    # 点击创建公钥私钥按钮
    def createKeyAction(self):
        keysGUI = KeysGUI()
        keysGUI.show()
        keysGUI.exec_()

    # 关于页面
    def aboutAction(self):
        aboutGUI = AboutGUI()
        aboutGUI.show()
        aboutGUI.exec_()

    # 创建顶部的配置widget
    def createConfigLayout(self, table):
        config = QGridLayout()
        config.setVerticalSpacing(5)
        config.setHorizontalSpacing(5)
        # 1.创建日志文件控件
        logLabel = QLabel("日志文件")
        self.logEdit = QLineEdit()
        logSelect = QPushButton("选择文件")
        logSelect.clicked.connect(self.selectFile)
        config.addWidget(logLabel, 0, 0)
        config.addWidget(self.logEdit, 0, 1)
        config.addWidget(logSelect, 0, 2)
        # 2.创建公钥控件
        publicKeyLabel = QLabel("公钥")
        publicKeyEdit = QLineEdit()
        config.addWidget(publicKeyLabel, 1, 0)
        config.addWidget(publicKeyEdit, 1, 1)
        # 3.创建私钥控件
        privateKeyLabel = QLabel("私钥")
        privateKeyEdit = QLineEdit()
        config.addWidget(privateKeyLabel, 2, 0)
        config.addWidget(privateKeyEdit, 2, 1)
        # 4.创建是否解密控件
        decodeQCheckBox = QCheckBox("是否解密")
        decodeQCheckBox.stateChanged.connect(self.decodeChangeAction)
        beginQPushButton = QPushButton("开始分析")
        beginQPushButton.clicked.connect(
            lambda: self.startAnalyzerAction(table, publicKeyEdit.text(), privateKeyEdit.text()))
        config.addWidget(decodeQCheckBox, 1, 2)
        config.addWidget(beginQPushButton, 2, 2)
        return config

    # 创建显示/隐藏表格某header的checkbox
    def createTableGrid(self, table, text, columnIndex):
        qCheckBox = QCheckBox(text)
        qCheckBox.setChecked(True)
        qCheckBox.stateChanged.connect(lambda: self.showHideAction(table, columnIndex))
        return qCheckBox

    # 点击某checkbox的事件
    def showHideAction(self, table, column):
        # 将第column列隐藏或显示
        table.setColumnHidden(column, not table.isColumnHidden(column))

    # 创建辅助控件
    def createHelperLayout(self, table):
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("显示/隐藏"))
        for index, text in enumerate(self.headerList):
            hbox.addWidget(self.createTableGrid(table, text, index))
        hbox.addWidget(QLabel("       tag过滤："))
        self.tagFilterQComboBox = QComboBox()
        self.tagFilterQComboBox.addItem(tagFilterAll)
        hbox.addWidget(self.tagFilterQComboBox)
        filterByTag = QPushButton("过滤")
        filterByTag.clicked.connect(lambda: self.filterTable(table))
        hbox.addWidget(filterByTag)
        hbox.addStretch(1)
        createKeys = QPushButton("生成公钥与私钥")
        createKeys.clicked.connect(self.createKeyAction)
        hbox.addWidget(createKeys)
        about = QPushButton("使用说明")
        about.clicked.connect(self.aboutAction)
        hbox.addWidget(about)
        return hbox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainGUI = MainGUI();
    mainGUI.show()
    sys.exit(app.exec_())
