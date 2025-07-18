from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class ClickableWidget(QWidget):
    def __init__(self, timeManager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timeManager = timeManager

    def mousePressEvent(self, event: QMouseEvent):
        print(self.timeManager.timeToString() + "clicked on ClickableWidget")