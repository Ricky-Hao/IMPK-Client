from Client.core import client, crypto
from Client.core.client import Route
from Client.message import *
from Client.logic import mainWindow
from Client.util import logger

message_log = logger.getChild('Route')

@Route.route('AuthResultMessage')
async def login(message):
    log = message_log.getChild('AuthMessage')
    message = AuthResultMessage(message)
    log.debug(message)
    if message.status == 'Logged':
        client.loginSuccessSignal.emit(message.username)
        mainWindow.loginSuccessSignal.emit()
    else:
        mainWindow.loginFailedSignal.emit()


@Route.route('ChatMessage')
async def chat(message):
    log = message_log.getChild('Chat')
    message = ChatMessage(message)
    log.debug(message)
    plaintext = crypto.decryptAndVerify(message.ciphertext,
                                        message.signature,
                                        crypto.loadCertFromUser(message.source).public_key(),
                                        mainWindow.privateKey)
    if plaintext == '':
        mainWindow.updateStatusSignal.emit('{0}的消息解密失败。'.format(message.source))
    else:
        client.db.insertMessage(message.source, plaintext, message.source)
        mainWindow.updateMessageSignal.emit()

@Route.route('FriendMessage')
async def friend(message):
    log = message_log.getChild('FriendMessage')
    message = FriendMessage(message)
    log.debug(message)
    client.db.clearTable('friends')
    for friend in message.friend_list:
        client.db.addFriend(friend)

    mainWindow.updateFriendSignal.emit()

@Route.route('FriendRequestMessage')
async def friendRequest(message):
    message = FriendRequestMessage(message)
    mainWindow.requestFriendSignal.emit(message.source)

@Route.route('ServerMessage')
async def server(message):
    message = ServerMessage(message)
    mainWindow.updateStatusSignal.emit('{0}: {1}'.format(message.source, message.content))

@Route.route('CertificateInstallMessage')
async def certInstall(message):
    log = message_log.getChild('CertInstall')

    message = CertificateInstallMessage(message)
    crypto.installCertForUser(message.cert_user, message.cert)
    log.info('Install Cert for {0}.'.format(message.cert_user))

    mainWindow.installCertSignal.emit(message.cert_user)