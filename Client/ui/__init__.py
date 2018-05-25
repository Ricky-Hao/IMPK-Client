import sys
import os

ui_path = os.path.dirname(os.path.abspath(__file__))
resource_path = os.path.join(ui_path, 'resource')
sys.path.append(resource_path)

from Client.ui.MainWindow import *
from Client.ui.resource import *
