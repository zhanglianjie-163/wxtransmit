# -*- coding: utf-8 -*-
import sys
import re
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import *
from  wxtransmit_form import Ui_MainWindow
from  wxlogin import WXLogin

import threading
from wxpy import *
import requests
import itchat

g_my_grp_list = []                 #我的群组列表
g_grp_member_list = []             #群组成员列表
g_grp_member_monitor_list = []     #监控成员列表
g_grp_trasmit_list = []            #转发群列表
bot = Null
wxobj = Null

#listview define function ******************************************************
def set_list_content(listview, items):
    listview.clear()
    for item in items:
        listview.addItem(item)

def flush_listview1():
    global g_my_grp_list                 #我的群组列表
    global g_grp_member_list            #群组成员列表
    global g_grp_member_monitor_list     #监控成员列表
    global g_grp_trasmit_list            #转发群列表

    qLists = wxobj.search_group()
    ui.listView1.clear()
    ui.listView2.clear()
    ui.listView3.clear()
    ui.listView4.clear()
    g_my_grp_list = []
    g_grp_member_list = []
    g_grp_member_monitor_list = []
    g_grp_trasmit_list = []
    for item in qLists:
        g_my_grp_list.append(item.name)
    set_list_content(ui.listView1, g_my_grp_list)
        
        

def listview1_menu_callback(pos):
    global g_my_grp_list                 #我的群组列表
    global g_grp_member_list            #群组成员列表
    global g_grp_member_monitor_list     #监控成员列表
    global g_grp_trasmit_list            #转发群列表

    text_list = ui.listView1.selectedItems()
    menu = QMenu()
    opt1 = menu.addAction("添加到转发群")
    action = menu.exec_(ui.listView1.mapToGlobal(pos))
    if action == opt1:
        for item in text_list:
            if item.text() not in g_grp_trasmit_list:  #添加到转发群列表
                g_grp_trasmit_list.append(item.text())
            if item.text() in g_my_grp_list:      #从我的群组列表删除
                g_my_grp_list.remove(item.text())
        set_list_content(ui.listView4, g_grp_trasmit_list)
        set_list_content(ui.listView1, g_my_grp_list)

def listview1_add_menu():
    #创建右键菜单listView_Action
    ui.listView1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    ui.listView1.customContextMenuRequested.connect(listview1_menu_callback)

#listview2 define function ******************************************************
def flush_listview2():
    global g_my_grp_list                 #我的群组列表
    global g_grp_member_list            #群组成员列表
    global g_grp_member_monitor_list     #监控成员列表
    global g_grp_trasmit_list            #转发群列表
    items = ui.listView1.selectedItems()
    search_group_name = items[0].text()
    group = wxobj.get_group_member(search_group_name)
    ui.listView2.clear()
    g_grp_member_list = []
    for member in group:
        g_grp_member_list.append(member.name)
    set_list_content(ui.listView2, g_grp_member_list)
def listview2_menu_callback(pos):
    global g_my_grp_list                 #我的群组列表
    global g_grp_member_list            #群组成员列表
    global g_grp_member_monitor_list     #监控成员列表
    global g_grp_trasmit_list            #转发群列表
    text_list = ui.listView2.selectedItems()
    menu = QMenu()
    opt1 = menu.addAction("添加到监控成员")
    action = menu.exec_(ui.listView2.mapToGlobal(pos))
    if action == opt1:
        for item in text_list:
            if item.text() not in g_grp_member_monitor_list:
                g_grp_member_monitor_list.append(item.text())
            if item.text() in g_grp_member_list:
                g_grp_member_list.remove(item.text())
        set_list_content(ui.listView3, g_grp_member_monitor_list)
        set_list_content(ui.listView2, g_grp_member_list)


def listview2_add_menu():
    #创建右键菜单listView_Action
    ui.listView2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    ui.listView2.customContextMenuRequested.connect(listview2_menu_callback)
#listview3 define function ******************************************************
def listview3_menu_callback(pos):
    global g_my_grp_list                 #我的群组列表
    global g_grp_member_list            #群组成员列表
    global g_grp_member_monitor_list     #监控成员列表
    global g_grp_trasmit_list            #转发群列表
    text_list = ui.listView3.selectedItems()
    menu = QMenu()
    opt1 = menu.addAction("移出")
    action = menu.exec_(ui.listView3.mapToGlobal(pos))
    if action == opt1:
        for item in text_list:
            if item.text() in g_grp_member_monitor_list:
                g_grp_member_monitor_list.remove(item.text())
            if item.text() not in g_grp_member_list:
                g_grp_member_list.append(item.text())
        set_list_content(ui.listView3, g_grp_member_monitor_list)
        set_list_content(ui.listView2, g_grp_member_list)

def listview3_add_menu():
    #创建右键菜单listView_Action
    ui.listView3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    ui.listView3.customContextMenuRequested.connect(listview3_menu_callback)

#listview4 define function ******************************************************
def listview4_menu_callback(pos):
    global g_my_grp_list                 #我的群组列表
    global g_grp_member_list            #群组成员列表
    global g_grp_member_monitor_list     #监控成员列表
    global g_grp_trasmit_list            #转发群列表
    text_list = ui.listView4.selectedItems()
    menu = QMenu()
    opt1 = menu.addAction("移出转发群")
    action = menu.exec_(ui.listView4.mapToGlobal(pos))
    if action == opt1:
        for item in text_list:
            if item.text() in g_grp_trasmit_list:
                g_grp_trasmit_list.remove(item.text())
            if item.text not in g_my_grp_list:
                g_my_grp_list.append(item.text())
        set_list_content(ui.listView4, g_grp_trasmit_list)
        set_list_content(ui.listView1, g_my_grp_list)

def listview4_add_menu():
    #创建右键菜单listView_Action
    ui.listView4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    ui.listView4.customContextMenuRequested.connect(listview4_menu_callback)

#************************************主窗口初始化 接口**********************************************
def main_window_init(ui):
    #刷新我的群组
    ui.pushButton.clicked.connect(flush_listview1)
    listview1_add_menu()
    #刷新群成员
    ui.listView1.clicked.connect(flush_listview2)
    listview2_add_menu()
    #刷新监控群成员
    listview3_add_menu()
    #刷新转发群
    listview4_add_menu()


class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        global wxobj
        wxobj = WXLogin()
        wxobj.login();
        #Message.sender
        @wxobj.bot.register(Group, SHARING)
        @wxobj.bot.register(Group, PICTURE)
        @wxobj.bot.register(Group, TEXT)
        def auto_reply(msg):
            if isinstance(msg.chat, Group):
                if msg.member.name in g_grp_member_monitor_list:
                    for item in g_grp_trasmit_list:
                        grop_chat = wxobj.bot.groups().search(item)[0]
                        if grop_chat != None:
                            msg.forward(grop_chat, prefix='')
        embed()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    main_window_init(ui)
    MainWindow.show()

    #t =MyThread(0)
    #t.start()
    """
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    """
    sys.exit(app.exec_())