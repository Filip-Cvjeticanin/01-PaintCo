from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from TimeManager import TimeManager

class Canvas(QWidget):
    def __init__(self, receivedColor = Qt.GlobalColor.black, penSize=6, parent=None):
        super().__init__(parent)
        self.receivedColor = receivedColor
        self.penSize = penSize
        self.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.setMouseTracking(True)

        self.canvas = QPixmap(self.size())  # This is your persistent drawing
        self.canvas.fill(Qt.white)

        self.last_point = None

    def resizeEvent(self, event):
        new_size = self.size()

        if new_size.width() > self.canvas.width() or new_size.height() > self.canvas.height():
            # Only grow the canvas, never shrink it
            new_width = max(self.canvas.width(), new_size.width())
            new_height = max(self.canvas.height(), new_size.height())

            new_canvas = QPixmap(new_width, new_height)
            new_canvas.fill(Qt.white)

            painter = QPainter(new_canvas)
            painter.drawPixmap(0, 0, self.canvas)
            painter.end()

            self.canvas = new_canvas

        super().resizeEvent(event)

    def paintEvent(self, event):
        # Draw the canvas onto the widget
        print(TimeManager.getInstance().timeToString() + " paintEvent triggered")
        painter = QPainter(self)
        visible_rect = self.rect()
        painter.drawPixmap(visible_rect, self.canvas, visible_rect)

    def mousePressEvent(self, event):
        if event.button() in (Qt.MouseButton.LeftButton, Qt.MouseButton.RightButton):
            self.last_point = event.pos()

            color = self.receivedColor if event.button() == Qt.MouseButton.LeftButton else Qt.white
            painter = QPainter(self.canvas)
            pen = QPen(color, self.penSize, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawPoint(self.last_point)  # Draw a dot at click position
            self.update()

    def mouseMoveEvent(self, event):

        color = None
        if event.buttons() & Qt.MouseButton.LeftButton: color = self.receivedColor
        elif event.buttons() & Qt.MouseButton.RightButton: color = Qt.GlobalColor.white

        if ((event.buttons() & Qt.MouseButton.LeftButton) or (event.buttons() & Qt.MouseButton.RightButton)) and self.last_point:
            painter = QPainter(self.canvas)
            pen = QPen(color, self.penSize, Qt.SolidLine)
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

    def setPenSize(self, newSize = 6):
        self.penSize = newSize