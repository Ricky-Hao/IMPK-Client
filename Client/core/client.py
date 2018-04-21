import asyncio
import time
import json
import websockets
from PyQt5 import QtCore
from Client.message import *
from Client.database import Database
from Client.util import logger

class Route:
    Routes = {}

    @classmethod
    def route(cls, route):
        def wrapper(route_function):
            cls.Routes.update({route:route_function})
            return route_function
        return wrapper


class Client(QtCore.QThread):
    connectSignal = QtCore.pyqtSignal(str)
    loginSuccessSignal = QtCore.pyqtSignal(str)

    def __init__(self, loop, parent=None):
        super().__init__(parent)
        self.loop = loop
        asyncio.set_event_loop(self.loop)
        self.log = logger.getChild('ClientWorker')
        self.connection = None
        self.db = None
        self.username = ''

        self.connectSignal.connect(self.startConnection)
        self.loginSuccessSignal.connect(self.loginSuccess)

    def run(self):
        self.loop.run_until_complete(self._run_forever())
        self.log.debug('Started.')

    async def _run_forever(self):
        while True:
            await asyncio.sleep(1)

    def startConnection(self, server_address):
        self.connection = Connection(server_address, self.loop)

    def send(self, data):
        data['source'] = self.username
        self.connection.sender(data)

    def loginSuccess(self, username):
        self.username = username
        self.db = Database(username)

class Connection:

    def __init__(self, server_address, loop):
        self.server_address = server_address
        self.loop = loop
        self.log = logger.getChild('Client({0})'.format(server_address))
        self.connection = None
        self.exit = 0

        self.connect()

    def connect(self):
        self.factory = websockets.connect('ws://{0}:30000'.format(self.server_address), loop=self.loop)
        self.task = asyncio.ensure_future(self.factory, loop=self.loop)
        while True:
            if self.task.done():
                self.connection = self.task.result()
                break
        self.log.debug(self.connection)
        asyncio.ensure_future(self.listener(), loop=self.loop)

    def fun(self, obj):
        self.log.debug(obj)

    async def listener(self):
        log = self.log.getChild('Listener')
        log.debug('Started.')
        try:
            async for message in self.connection:
                if self.exit == 1:
                    self.connection.close()
                    break
                log.debug(message)
                base_message = BaseMessage(message)

                if base_message.type in Route.Routes.keys():
                    log.debug(base_message.type)
                    await Route.Routes[base_message.type](message)

        except Exception as err:
            log.error(err)
            self.connection.close()

    async def _sender(self, data):
        log = self.log.getChild('Sender')
        try:
            await self.connection.send(json.dumps(data))
        except Exception as err:
            log.error(err)

    def sender(self, data):
        try:
            self._sender(data).send(None)
        except StopIteration:
            pass

