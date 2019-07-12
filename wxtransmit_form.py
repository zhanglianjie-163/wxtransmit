# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wxtransmit_form.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 20, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.listView1 = QtWidgets.QListWidget(self.centralwidget)
        self.listView1.setGeometry(QtCore.QRect(20, 50, 161, 361))
        self.listView1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listView1.setObjectName("listView1")
        self.listView2 = QtWidgets.QListWidget(self.centralwidget)
        self.listView2.setGeometry(QtCore.QRect(190, 50, 171, 171))
        self.listView2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listView2.setObjectName("listView2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 61, 21))
        self.label_2.setObjectName("label_2")
        self.listView3 = QtWidgets.QListWidget(self.centralwidget)
        self.listView3.setGeometry(QtCore.QRect(390, 50, 181, 171))
        self.listView3.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listView3.setObjectName("listView3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 20, 71, 21))
        self.label_3.setObjectName("label_3")
        self.listView4 = QtWidgets.QListWidget(self.centralwidget)
        self.listView4.setGeometry(QtCore.QRect(190, 250, 171, 161))
        self.listView4.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listView4.setObjectName("listView4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 230, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 230, 61, 21))
        self.label_5.setObjectName("label_5")
        self.listWidget5 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget5.setGeometry(QtCore.QRect(390, 250, 181, 161))
        self.listWidget5.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget5.setObjectName("listWidget5")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(480, 230, 81, 16))
        self.checkBox.setObjectName("checkBox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 440, 551, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 596, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主窗口"))
        self.label.setText(_translate("MainWindow", "我的群组"))
        self.pushButton.setText(_translate("MainWindow", "刷新群组"))
        self.label_2.setText(_translate("MainWindow", "群成员"))
        self.label_3.setText(_translate("MainWindow", "监控群成员"))
        self.label_4.setText(_translate("MainWindow", "转发群"))
        self.label_5.setText(_translate("MainWindow", "日志信息"))
        self.checkBox.setText(_translate("MainWindow", "过滤淘口令"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))


