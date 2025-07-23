from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from TimeManager import TimeManager

class Canvas(QWidget):
    def __init__(self, receivedColor = Qt.GlobalColor.black, parent=None):
        super().__init__(parent)
        self.receivedColor = receivedColor
        self.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.setMouseTracking(True)

        self.canvas = QPixmap(self.size())  # This is your persistent drawing
        self.canvas.fill(Qt.white)

        self.last_point = None

    def resizeEvent(self, event):
        # Resize canvas without losing existing content
        if self.canvas.size() != self.size():
            new_canvas = QPixmap(self.size())
            new_canvas.fill(Qt.white)
            painter = QPainter(new_canvas)
            painter.drawPixmap(0, 0, self.canvas)
            self.canvas = new_canvas

    def paintEvent(self, event):
        # Draw the canvas onto the widget
        print(TimeManager.getInstance().timeToString() + " paintEvent triggered")
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.canvas)

    def mousePressEvent(self, event):
        if event.button() in (Qt.MouseButton.LeftButton, Qt.MouseButton.RightButton):
            self.last_point = event.pos()

            color = self.receivedColor if event.button() == Qt.MouseButton.LeftButton else Qt.white
            painter = QPainter(self.canvas)
            pen = QPen(color, 5, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawPoint(self.last_point)  # Draw a dot at click position
            self.update()

    def mouseMoveEvent(self, event):

        color = None
        if event.buttons() & Qt.MouseButton.LeftButton: color = self.receivedColor
        elif event.buttons() & Qt.MouseButton.RightButton: color = Qt.GlobalColor.white

        if ((event.buttons() & Qt.MouseButton.LeftButton) or (event.buttons() & Qt.MouseButton.RightButton)) and self.last_point:
            painter = QPainter(self.canvas)
            pen = QPen(color, 5, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()  # triggers repaint

    def mouseReleaseEvent(self, event):
        self.last_point = None

    def clear(self):
        print("clear called")
        self.canvas.fill(Qt.white)
        self.update()

    def setPenColor(self, newColor = Qt.GlobalColor.black):
        self.receivedColor = newColor