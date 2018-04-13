from .client import Route, client
from .logger import logging
from .message import ChatMessage
from main import mainWindow

@Route.route('ChatMessage')
async def chat(message):
    log = logging.getLogger('Chat')
    message = ChatMessage(message)
    log.debug(message)
    client.db.insertMessage(message.user, message.content)
    mainWindow.updateMessageSignal.emit()
