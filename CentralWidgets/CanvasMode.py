from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from CentralWidgets.BaseModeWidget import BaseModeWidget
from globalData import GlobalData
from CentralWidgets.CustomWidgets.Canvas import Canvas

class CanvasMode(BaseModeWidget):
    toolbar: QWidget
    colorSelector: QWidget
    sizeSelector: QWidget
    infoSection: QWidget

    toolbarLayout: QHBoxLayout

    def __init__(self, *args, **kwargs):
        self.canvasInstance = Canvas()
        super().__init__(receivedContentWidget=self.canvasInstance, *args, **kwargs)
        self.setupToolbar()

    def setupToolbar(self):
        self.toolbar = self.headerWrapper.contentWrapper

        self.colorSelector: ColorSelector = ColorSelector()
        self.sizeSelector = QWidget()
        self.infoSection = QWidget()

        self.colorSelector.setStyleSheet("""
        ColorSelector{
            border: 1px solid green
        }
        """)
        self.sizeSelector.setStyleSheet("border: 1px dotted black")
        self.infoSection.setStyleSheet("border: 1px dotted black")

        self.colorSelector.colorChosen.connect(self.setPenColor)

        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setSpacing(40)
        self.toolbarLayout.setContentsMargins(10,0,0,10)
        self.toolbarLayout.addWidget(self.colorSelector, stretch=1)
        self.toolbarLayout.addWidget(self.sizeSelector, stretch=1)
        self.toolbarLayout.addWidget(self.infoSection, stretch=1)

        self.toolbar.setLayout(self.toolbarLayout)

    def setPenColor(self, color: QColor):
        print("Color set to:", color.name())
        self.canvasInstance.setPenColor(color)

class ColorSelector(QWidget):
    colorChosen = Signal(QColor)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        globalData = GlobalData.getInstance()
        self.Layout = QHBoxLayout()
        self.Layout.setSpacing(0)
        self.Layout.setContentsMargins(0,0,0,0)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        for color in globalData.availableColors:
            newColorButton = ColorButton(color)
            newColorButton.colorSignal.connect(self.colorChosen)
            style = """
            border: 1px dotted red;
            """
            if color == Qt.GlobalColor.black:                                                        #background-color: rgba(240, 240, 240, 1.0);
                style = style + "background-color: pink"
            newColorButton.setStyleSheet("ColorButton {" + style + "}")
            self.Layout.addWidget(newColorButton)

        self.setLayout(self.Layout)



class ColorButton(QWidget):

    colorSignal = Signal(QColor)

    def __init__(self, color: QColor = Qt.GlobalColor.black, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.Layout = QHBoxLayout()
        self.Layout.setContentsMargins(0,0,0,0)


        self.activateButton = QPushButton()

        self.activateButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.activateButton.setMinimumSize(10, 10)
        self.activateButton.clicked.connect(self.changeSelectedColor)
        self.Layout.addWidget(self.activateButton, alignment=Qt.AlignmentFlag.AlignCenter)
        self.activateButton.setStyleSheet(f"background-color: {color.name}")
        self.setLayout(self.Layout)

    def resizeEvent(self, event, /):
        side = int(min(self.width(), self.height()) * 0.75)
        self.activateButton.setFixedSize(side, side)
        super().resizeEvent(event)

    def changeSelectedColor(self):
        parent = self.parent()
        children = parent.children()
        for child in children:
            if isinstance(child, ColorButton):
                child.setStyleSheet("""
                ColorButton {
                    border: 1px dotted red;
                    background-color: rgba(240, 240, 240, 1.0)
                }
                """)
        self.setStyleSheet("""
        ColorButton {
            border: 1px dotted red;
            background-color: pink
        }
        """)
        self.colorSignal.emit(self.color)
        self.update()


