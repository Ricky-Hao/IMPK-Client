import sys
from .core import client, logging
from .logic import mainWindow, app


mainWindow.connectSignal = client.connectSignal
