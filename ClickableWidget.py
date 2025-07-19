from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *



class ClickableWidget(QWidget):
    def __init__(self, timeManager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timeManager = timeManager

    def mousePressEvent(self, event: QMouseEvent):
        mouseButton = ""
        if event.button() == Qt.MouseButton.LeftButton: mouseButton = "Left"
        elif event.button() == Qt.MouseButton.RightButton: mouseButton = "Right"
        pos = (event.pos().x(), event.pos().y())
        posGlobal = (event.globalPos().x(), event.globalPos().y())
        print(self.timeManager.timeToString() + mouseButton + " clicked on ClickableWidget; local @", pos, "global @", posGlobal)