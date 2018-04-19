from PyQt5 import QtWidgets, QtCore
from ..ui import *
from ..core import logging, client, sendAcceptFriend, sendChat, sendAuthMessage, sendFriendRequest, sendFriendUpdate


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    updateMessageSignal = QtCore.pyqtSignal()
    loginSuccessSignal = QtCore.pyqtSignal()
    loginFailedSignal = QtCore.pyqtSignal()
    updateFriendSignal = QtCore.pyqtSignal()
    requestFriendSignal = QtCore.pyqtSignal(str)
    updateStatusSignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        self.log = logging.getLogger('MainWindow')
        super().__init__(parent)
        self.toUser = ''

        self.connectSignal = None

        self.setupUi(self)

        self.widgetLink()
        self.testWidgetLink()
        self.signalLink()

    def widgetLink(self):
        self.loginButton.clicked.connect(self.login)
        self.friendList.itemClicked.connect(self.changeTargetUser)
        self.sendButton.clicked.connect(self.sendMessage)
        self.addFriendAction.triggered.connect(self.addFriend)

    def testWidgetLink(self):
        #For Test
        pass

    def signalLink(self):
        self.updateMessageSignal.connect(self.updateMessage)
        self.loginSuccessSignal.connect(self.loginSuccess)
        self.loginFailedSignal.connect(self.loginFailed)
        self.updateFriendSignal.connect(self.updateFriend)
        self.requestFriendSignal.connect(self.requestFriend)
        self.updateStatusSignal.connect(self.updateStatus)

    def updateStatus(self, data):
        self.statusBar.showMessage(data)

    def addFriend(self):
        text, ok = QtWidgets.QInputDialog.getText(self, '添加好友','好友ID:')
        if ok:
            sendFriendRequest(text)

    def requestFriend(self, friend):
        self.log.debug(friend)
        result = QtWidgets.QMessageBox.question(self, '好友请求', '是否接受{0}的好友请求？'.format(friend))
        sendAcceptFriend(friend, result==QtWidgets.QMessageBox.Yes)

    def login(self):
        self.connectSignal.emit(self.serverAddressEdit.text())
        sendAuthMessage(self.userEdit.text(), self.passwordEdit.text())

    def loginSuccess(self):
        self.loginButton.setText('已登录')
        self.loginButton.disconnect()
        sendFriendUpdate()
        self.updateMessage()
        self.updateStatus('登陆成功')
        self.setWindowTitle('{0}-基于公钥加密的即时通讯系统'.format(client.username))

    def loginFailed(self):
        self.userEdit.clear()
        self.passwordEdit.clear()
        self.updateStatus('登录失败！')

    def sendMessage(self):
        content = self.sendText.toPlainText()
        client.db.insertMessage(self.toUser, content, client.username)
        sendChat(self.toUser, content)
        self.sendText.clear()
        self.updateStatus('消息成功发送给{0}'.format(self.toUser))
        self.updateMessage()

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
            if message[0] == self.toUser:
                self.messageList.addItem('[{2}]: → {1}'.format(*message))
            else:
                self.messageList.addItem('[{2}]: ← {1}'.format(*message))
        self.messageList.scrollToBottom()


mainWindow = MainWindow()