import sys
import os
from wxpy import *
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

class Example(QWidget):

  def __init__(self):
    super().__init__()

  def initUI(self, path):

    hbox = QHBoxLayout(self)
    pixmap = QPixmap(path)

    lb1 = QLabel(self)              
    lb1.setPixmap(pixmap)

    hbox.addWidget(lb1)
    self.setLayout(hbox)

    self.move(300, 300)
    self.setWindowTitle('像素图控件')
    self.show()



class WXLogin():
    def login(self):
        bot = Bot(cache_path=False,qr_callback=self.qr_callback, login_callback=self.login_callback, logout_callback=self.logout_callback)
        self.bot = bot
        return bot
    def search_group(self):
        group_set = self.bot.groups(False, False)
        return group_set

    def get_group_member(self, group_name):
        group = self.bot.groups().search(group_name)[0]
        return group

    def qr_callback(self, uuid, status, qrcode):
        path = os.path.join(os.getcwd(),'{}.png'.format(uuid))
        with open(path,'wb') as qrcode_file:
            qrcode_file.write(qrcode)
        ex = Example()
        ex.initUI(path)


    def login_callback(self):
        print("login success")
        #print(bot.self.name)

    def logout_callback(self):
        print("login out")

