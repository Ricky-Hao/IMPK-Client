import sys
from core import client
from logic import mainWindow, app


if __name__ == '__main__':
    try:
        mainWindow.show()
        mainWindow.sendSignal = client.sendSignal
        mainWindow.connectSignal = client.connectSignal
        client.loginDoneSignal = mainWindow.loginDoneSignal
        sys.exit(app.exec_())
    except Exception as err:
        print(err)

