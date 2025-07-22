from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from CentralWidgets.BaseModeWidget import BaseModeWidget
from CentralWidgets.CustomWidgets.Canvas import Canvas

class CanvasMode(BaseModeWidget):
    def __init__(self, *args, **kwargs):
        self.canvasInstance = Canvas()
        super().__init__(receivedContentWidget=self.canvasInstance, *args, **kwargs)

