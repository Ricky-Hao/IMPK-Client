# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 536)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons8-r-52.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(9, 2, 9, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sendText = QtWidgets.QTextEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sendText.sizePolicy().hasHeightForWidth())
        self.sendText.setSizePolicy(sizePolicy)
        self.sendText.setObjectName("sendText")
        self.verticalLayout.addWidget(self.sendText)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.clearButton = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setAutoDefault(False)
        self.clearButton.setDefault(False)
        self.clearButton.setFlat(False)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_3.addWidget(self.clearButton)
        self.sendButton = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout_3.addWidget(self.sendButton)
        self.verticalLayout.addWidget(self.widget_4)
        self.gridLayout.addWidget(self.widget_3, 3, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.friendList = QtWidgets.QListWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.friendList.sizePolicy().hasHeightForWidth())
        self.friendList.setSizePolicy(sizePolicy)
        self.friendList.setUniformItemSizes(True)
        self.friendList.setWordWrap(True)
        self.friendList.setSelectionRectVisible(False)
        self.friendList.setObjectName("friendList")
        self.horizontalLayout_2.addWidget(self.friendList)
        self.messageList = QtWidgets.QListWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.messageList.sizePolicy().hasHeightForWidth())
        self.messageList.setSizePolicy(sizePolicy)
        self.messageList.setUniformItemSizes(True)
        self.messageList.setWordWrap(True)
        self.messageList.setSelectionRectVisible(False)
        self.messageList.setObjectName("messageList")
        self.horizontalLayout_2.addWidget(self.messageList)
        self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.serverAddressEdit = QtWidgets.QLineEdit(self.widget)
        self.serverAddressEdit.setObjectName("serverAddressEdit")
        self.horizontalLayout.addWidget(self.serverAddressEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.userEdit = QtWidgets.QLineEdit(self.widget)
        self.userEdit.setObjectName("userEdit")
        self.horizontalLayout.addWidget(self.userEdit)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.passwordEdit = QtWidgets.QLineEdit(self.widget)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.horizontalLayout.addWidget(self.passwordEdit)
        self.loginButton = QtWidgets.QPushButton(self.widget)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout.addWidget(self.loginButton)
        self.registerButton = QtWidgets.QPushButton(self.widget)
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout.addWidget(self.registerButton)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 692, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.privateKeyMenu = QtWidgets.QMenu(self.menu)
        self.privateKeyMenu.setObjectName("privateKeyMenu")
        self.certMenu = QtWidgets.QMenu(self.menu)
        self.certMenu.setObjectName("certMenu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.addFriendAction = QtWidgets.QAction(MainWindow)
        self.addFriendAction.setObjectName("addFriendAction")
        self.actionTestAction1 = QtWidgets.QAction(MainWindow)
        self.actionTestAction1.setObjectName("actionTestAction1")
        self.generatePrivateKeyAction = QtWidgets.QAction(MainWindow)
        self.generatePrivateKeyAction.setObjectName("generatePrivateKeyAction")
        self.loadPrivateKeyAction = QtWidgets.QAction(MainWindow)
        self.loadPrivateKeyAction.setObjectName("loadPrivateKeyAction")
        self.generateCertAction = QtWidgets.QAction(MainWindow)
        self.generateCertAction.setObjectName("generateCertAction")
        self.loadCertAction = QtWidgets.QAction(MainWindow)
        self.loadCertAction.setObjectName("loadCertAction")
        self.privateKeyMenu.addAction(self.generatePrivateKeyAction)
        self.privateKeyMenu.addAction(self.loadPrivateKeyAction)
        self.certMenu.addAction(self.generateCertAction)
        self.certMenu.addAction(self.loadCertAction)
        self.menu.addAction(self.addFriendAction)
        self.menu.addAction(self.privateKeyMenu.menuAction())
        self.menu.addAction(self.certMenu.menuAction())
        self.menu_2.addAction(self.actionTestAction1)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.clearButton.clicked.connect(self.sendText.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于公钥加密的即时通讯系统-客户端"))
        self.clearButton.setText(_translate("MainWindow", "清空"))
        self.sendButton.setText(_translate("MainWindow", "发送"))
        self.label.setText(_translate("MainWindow", "服务器地址"))
        self.label_2.setText(_translate("MainWindow", "用户名"))
        self.label_3.setText(_translate("MainWindow", "密码"))
        self.loginButton.setText(_translate("MainWindow", "登陆"))
        self.registerButton.setText(_translate("MainWindow", "注册"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.privateKeyMenu.setTitle(_translate("MainWindow", "本地密钥管理"))
        self.certMenu.setTitle(_translate("MainWindow", "本地证书管理"))
        self.menu_2.setTitle(_translate("MainWindow", "测试"))
        self.addFriendAction.setText(_translate("MainWindow", "增加好友"))
        self.actionTestAction1.setText(_translate("MainWindow", "TestAction1"))
        self.generatePrivateKeyAction.setText(_translate("MainWindow", "生成"))
        self.loadPrivateKeyAction.setText(_translate("MainWindow", "导入"))
        self.generateCertAction.setText(_translate("MainWindow", "生成"))
        self.loadCertAction.setText(_translate("MainWindow", "导入"))

import MainWindow_rc
