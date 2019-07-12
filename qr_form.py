# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qr_form.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QRMainWindow(object):
    def setupUi(self, QRMainWindow):
        QRMainWindow.setObjectName("QRMainWindow")
        QRMainWindow.resize(436, 406)
        self.centralwidget = QtWidgets.QWidget(QRMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        QRMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QRMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 23))
        self.menubar.setObjectName("menubar")
        QRMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QRMainWindow)
        self.statusbar.setObjectName("statusbar")
        QRMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QRMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QRMainWindow)

    def retranslateUi(self, QRMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QRMainWindow.setWindowTitle(_translate("QRMainWindow", "二维码"))


