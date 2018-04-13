import sys
from .core import client, logging
from .logic import mainWindow, app


mainWindow.sendSignal = client.sendSignal
mainWindow.connectSignal = client.connectSignal
client.loginDoneSignal = mainWindow.loginDoneSignal
