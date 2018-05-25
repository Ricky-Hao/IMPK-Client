import os
import sys
from Client.util.logger import logger

log = logger.getChild('Util')

if getattr(sys, 'frozen', False):
    PROJECT_ROOT = sys._MEIPASS
else:
    script_path = os.path.abspath(__file__)
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(script_path)))
KEY_ROOT = os.path.join(PROJECT_ROOT, 'key')
DB_ROOT = os.path.join(PROJECT_ROOT, 'db')
log.debug('Project_ROOT: {0}'.format(PROJECT_ROOT))

os.makedirs(KEY_ROOT, exist_ok=True)
os.makedirs(DB_ROOT, exist_ok=True)

__all__ = ['PROJECT_ROOT', 'KEY_ROOT', 'DB_ROOT', 'logger']