from Client.core import client
from Client.core.client import Route
from Client.util.logger import logger
from Client.message import *
from Client.logic import mainWindow

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
    client.db.insertMessage(message.source, message.content, message.source)
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

