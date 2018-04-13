from PyQt5 import QtWidgets, QtCore
from ui import *
from core import logging, client

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    updateMessageSignal = QtCore.pyqtSignal()
    loginDoneSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        self.log = logging.getLogger('MainWindow')
        super().__init__(parent)
        self.toUser = ''

        self.sendSignal = None
        self.connectSignal = None

        self.setupUi(self)

        self.loginButton.clicked.connect(self.login)
        self.friendList.itemClicked.connect(self.changeTargetUser)
        self.sendButton.clicked.connect(self.sendMessage)
        self.updateMessageSignal.connect(self.updateMessage)
        self.loginDoneSignal.connect(self.loginDoneHandler)
        self.addFriendAction.triggered.connect(self.addFriend)

    def addFriend(self):
        text, ok = QtWidgets.QInputDialog.getText(self, '添加好友','好友ID:')
        if ok:
            client.db.addFriend(text)
            self.updateFriend()

    def login(self):
        data = {}
        data['serverAddress'] = self.serverAddressEdit.text()
        data['user'] = self.userEdit.text()
        data['password'] = self.passwordEdit.text()
        self.log.debug(data)
        self.connectSignal.emit(data)

    def loginDoneHandler(self):
        self.loginButton.setText('已登录')
        self.loginButton.disconnect()
        self.updateFriend()
        self.updateMessage()

    def sendMessage(self):
        content = self.sendText.toPlainText()
        data = {'to':self.toUser, 'content':content}
        self.sendSignal.emit(data)
        self.sendText.clear()

    def updateFriend(self):
        self.friendList.clear()
        for friend in client.db.fetchFriend():
            if self.toUser == '':
                self.toUser = friend[0]
            self.friendList.addItem(friend[0])

    def changeTargetUser(self, item):
        self.toUser = item.text()
        self.updateMessage()

    def updateMessage(self):
        self.messageList.clear()
        for message in client.db.fetchMessage(self.toUser):
            self.messageList.addItem('用户：{0:20s} 时间：{2}\n内容：{1}'.format(*message))
        self.messageList.scrollToBottom()


mainWindow = MainWindow()