from functools import partial
from PyQt5 import QtWidgets, QtCore
from Client.ui import *
from Client.core import client, send, crypto
from Client.util import logger, KEY_ROOT


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    updateMessageSignal = QtCore.pyqtSignal()
    loginSuccessSignal = QtCore.pyqtSignal()
    loginFailedSignal = QtCore.pyqtSignal()
    updateFriendSignal = QtCore.pyqtSignal()
    requestFriendSignal = QtCore.pyqtSignal(str)
    updateStatusSignal = QtCore.pyqtSignal(str)
    installCertSignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        self.log = logger.getChild('MainWindow')
        super().__init__(parent)
        self.toUser = ''
        self.privateKey = None
        self.cert = None
        self.username = ''
        self.password = ''

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
        self.registerButton.clicked.connect(self.register)

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
        self.installCertSignal.connect(self.installCert)

    def updateStatus(self, data):
        self.statusBar.showMessage(data)

    def addFriend(self):
        text, ok = QtWidgets.QInputDialog.getText(self, '添加好友','好友ID:')
        if ok:
            send.sendFriendRequest(text)

    def requestFriend(self, friend):
        self.log.debug(friend)
        result = QtWidgets.QMessageBox.question(self, '好友请求', '是否接受{0}的好友请求？'.format(friend))
        send.sendAcceptFriend(friend, result==QtWidgets.QMessageBox.Yes)

    def login(self):
        server_address = self.serverAddressEdit.text()
        self.username = self.userEdit.text()
        self.password = self.passwordEdit.text()
        if '' in (self.username, self.password, server_address):
            QtWidgets.QMessageBox.question(self, '登录失败', '请输入用户信息。')
        else:
            self.connectSignal.emit(server_address)
            send.sendAuthMessage(self.userEdit.text(), self.passwordEdit.text())

    def register(self):
        server_address = self.serverAddressEdit.text()
        self.username = self.userEdit.text()
        self.password = self.passwordEdit.text()
        if '' in (self.username, self.password, server_address):
            QtWidgets.QMessageBox.question(self, '注册失败', '请输入用户信息。')
        else:
            self.connectSignal.emit(server_address)
            send.sendRegisterMessage(self.userEdit.text(), self.passwordEdit.text())

    def loginSuccess(self):
        self.loginButton.setText('已登录')
        self.loginButton.disconnect()
        self.registerButton.disconnect()
        send.sendFriendUpdate()
        self.updateMessage()
        self.updateStatus('登陆成功')
        self.setWindowTitle('{0}-基于公钥加密的即时通讯系统'.format(self.username))

        if crypto.checkUserPrivateKey(self.username):
            self.privateKey = crypto.loadPrivateFromUser(self.username, self.password)
        else:
            self.privateKey = crypto.generatePrivate(self.username, self.password)
        self.loginButton.setText('已装载个人密钥')
        self.loginButton.clicked.connect(partial(self.showText, crypto.getUserFilePath(self.username, 'key')))

        if crypto.checkUserCertKey(self.username):
            self.installCert(self.username)
        else:
            csr = crypto.generateCSR(self.username, self.privateKey, 'CN', 'ShanXi', 'XiAn', 'XDU', 'CE', self.username)
            send.sendCertificateSigningRequestMessage(csr)

    def installCert(self, username):
        if self.username == username:
            self.cert = crypto.loadCertFromUser(self.username)
            self.registerButton.setText('已装载个人证书')
            self.registerButton.clicked.connect(partial(self.showText, crypto.getUserFilePath(username, 'crt')))
            self.log.debug(self.privateKey)
            self.log.debug(self.cert)

    def showText(self, file_path):
        with open(file_path, 'r') as f:
            QtWidgets.QMessageBox.question(self, '文件内容', f.read())


    def loginFailed(self):
        self.userEdit.clear()
        self.passwordEdit.clear()
        self.updateStatus('登录失败！')

    def sendMessage(self):
        content = self.sendText.toPlainText()
        if '' not in (self.toUser, content):
            client.db.insertMessage(self.toUser, content, self.username)
            to_cert = crypto.loadCertFromUser(self.toUser)
            ciphertext, signature = crypto.encryptAndSign(content, to_cert.public_key(), self.privateKey)
            send.sendChat(self.toUser, ciphertext, signature)
            self.sendText.clear()
            self.updateStatus('消息成功发送给{0}'.format(self.toUser))
            self.updateMessage()
        else:
            QtWidgets.QMessageBox.question(self, '发送消息失败', '请选择消息对象，且发送内容不为空。')

    def updateFriend(self):
        self.friendList.clear()
        for friend in client.db.fetchFriend():
            if self.toUser == '':
                self.toUser = friend[0]
            item = QtWidgets.QListWidgetItem(friend[0])
            self.friendList.addItem(item)

    def changeTargetUser(self, item):
        self.toUser = item.text()
        self.updateMessage()

    def updateMessage(self):
        self.messageList.clear()
        for message in client.db.fetchMessage(self.toUser):
            if message[0] == self.toUser:
                item =QtWidgets.QListWidgetItem('[{2}]: ← {1}'.format(*message))
            else:
                item = QtWidgets.QListWidgetItem('[{2}]: →  {1}'.format(*message))

            self.messageList.addItem(item)
        self.messageList.scrollToBottom()


