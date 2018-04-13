import asyncio
import json
import websockets
from PyQt5.QtCore import pyqtSignal, QThread
from .message import ChatMessage, BaseMessage
from .logger import logging
from database import Database


class Route:
    Routes = {}

    @classmethod
    def route(cls, route):
        def wrapper(route_function):
            cls.Routes.update({route:route_function})
            return route_function
        return wrapper

class Client(QThread):
    sendSignal = pyqtSignal(dict)
    connectSignal = pyqtSignal(dict)

    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.serverAddress = ''
        self.user = ''
        self.password = ''
        self.db = None
        self.log = logging.getLogger('Client')
        self.sendSignal.connect(self._sender)
        self.connectSignal.connect(self.connectSignalHandler)
        self.loginDoneSignal = None

    def run(self):
        self._connect()

    def connectSignalHandler(self, connect_dict):
        self.log.debug(connect_dict)
        self.serverAddress = connect_dict['serverAddress']
        self.user = connect_dict['user']
        self.password = connect_dict['password']
        self.start()

    def _connect(self):
        log = logging.getLogger('_connect')
        self.factory = websockets.connect('ws://{0}'.format(self.serverAddress), loop=self.loop)
        self.client = self.loop.run_until_complete(self.factory)
        try:
            self.loop.run_until_complete(self.connect())
        except KeyboardInterrupt:
            log.warning('KeyBoard!')
            self.client.close()

    async def listener(self):
        log = logging.getLogger('Listener')
        try:
            async for message in self.client:
                log.debug(message)
                base_message = BaseMessage(message)

                if base_message.message_type in Route.Routes.keys():
                    result = await Route.Routes[base_message.message_type](base_message.to_json())

        except KeyboardInterrupt:
            log.warning('Listener closed')
            self.client.close()

    def _sender(self, data):
        try:
            self.sender(data).send(None)
        except StopIteration:
            pass

    async def sender(self, data):
        log = logging.getLogger('Sender')
        try:
            send_data = ChatMessage(data)
            log.debug(send_data)
            await self.client.send(send_data.to_json())
        except Exception as err:
            log.warning(err)
            await asyncio.sleep(1)

    async def connect(self):
        data = {'message_type':'AuthMessage', 'username':self.user, 'password':self.password}
        self.db = Database(self.user)
        self.loginDoneSignal.emit()
        await self.client.send(json.dumps(data))
        listener_task = asyncio.ensure_future(self.listener())
        done, pending = await asyncio.wait(
            [listener_task],
            return_when=asyncio.FIRST_EXCEPTION,
        )

        for task in pending:
            task.cancel()

client = Client(asyncio.get_event_loop())