from Client.core import client
from Client.core.route import *
from Client.util import logger
from Client.logic import mainWindow, app

mainWindow.connectSignal = client.connectSignal