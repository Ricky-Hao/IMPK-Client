from client import *


if __name__ == '__main__':
    log = logging.getLogger('Run_Client')
    try:
        mainWindow.show()
        sys.exit(app.exec_())
    except Exception as err:
        log.error(err)

