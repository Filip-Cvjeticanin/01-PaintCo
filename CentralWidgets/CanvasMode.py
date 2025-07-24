from xml.dom.pulldom import default_bufsize

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from CentralWidgets.BaseModeWidget import BaseModeWidget
from globalData import GlobalData
from CentralWidgets.CustomWidgets.Canvas import Canvas
from TimeManager import TimeManager

class CanvasMode(BaseModeWidget):
    toolbar: QWidget
    colorSelector: QWidget
    sizeSelector: QWidget
    infoSection: QWidget

    toolbarLayout: QHBoxLayout

    def __init__(self, info: list[tuple[str, str]] = None, defaultButtonText = "Save", playerName="-", *args, **kwargs):
        if info is None:
            info = []
        self.canvasInstance = Canvas()
        super().__init__(receivedContentWidget=self.canvasInstance, *args, **kwargs)
        self.setupToolbar(playerName)

    def setupToolbar(self, playerName = "-", defaultButtonText = "Save"):
        self.toolbar = self.headerWrapper.contentWrapper

        self.colorSelector: ColorSelector = ColorSelector()
        self.sizeSelector: SizeSelector = SizeSelector()
        self.infoSection: InfoSection = InfoSection(playerName=playerName, buttonText=defaultButtonText)
        self.bindNextButton()

        #self.sizeSelector.setStyleSheet("border: 1px dotted black")
        #self.infoSection.setStyleSheet("border: 1px dotted black")

        self.colorSelector.colorChosen.connect(self.setPenColor)
        self.sizeSelector.sizeChanged.connect(self.setPenSize)

        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setSpacing(25)
        self.toolbarLayout.setContentsMargins(10,0,0,10)
        self.toolbarLayout.addWidget(self.colorSelector, stretch=1)
        self.toolbarLayout.addWidget(self.sizeSelector, stretch=1)
        self.toolbarLayout.addWidget(self.infoSection, stretch=1)

        self.toolbar.setLayout(self.toolbarLayout)

    def setPenColor(self, color: QColor):
        print("Color set to:", color.name())
        self.canvasInstance.setPenColor(color)

    def setPenSize(self, size: int):
        print("Size set to:", size)
        self.canvasInstance.setPenSize(size)

    def bindNextButton(self, function = None, **kwargs):

        timeManager = TimeManager.getInstance()
        def dummy():
            return
            print(timeManager.timeToString() + "Save not implemented!" + str(self.canvasInstance.size().toTuple()))

        if function is None:
            function = dummy

        self.infoSection.nextButton.clicked.connect(function)



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
            border: 1px solid silver;
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
                    border: 1px solid silver;
                    background-color: rgba(240, 240, 240, 1.0)
                }
                """)
        self.setStyleSheet("""
        ColorButton {
            border: 1px solid silver;
            background-color: pink
        }
        """)
        self.colorSignal.emit(self.color)
        self.update()




class SizeSelector(QWidget):
    sizeChanged = Signal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        globalData = GlobalData.getInstance()
        self.Layout = QHBoxLayout()
        self.Layout.setSpacing(0)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        for size in globalData.availableSizes:
            newSizeButton = SizeButton(size)
            newSizeButton.sizeSignal.connect(self.sizeChanged)
            style = """
                    border: 1px solid silver;
                    """
            if size == 6:  # background-color: rgba(240, 240, 240, 1.0);
                style = style + "background-color: pink"
            newSizeButton.setStyleSheet("SizeButton {" + style + "}")
            self.Layout.addWidget(newSizeButton)

        self.setLayout(self.Layout)



class SizeButton(QWidget):
    sizeSignal = Signal(int)

    def __init__(self, penSize = 6, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.penSize = penSize
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.Layout = QHBoxLayout()
        self.Layout.setContentsMargins(0, 0, 0, 0)

        self.activateButton = QPushButton(str(penSize))

        self.activateButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.activateButton.setMinimumSize(10, 10)
        self.activateButton.clicked.connect(self.changeSelectedSize)
        self.Layout.addWidget(self.activateButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.Layout)

    def resizeEvent(self, event, /):
        side = int(min(self.width(), self.height()) * 0.75)
        self.activateButton.setFixedSize(side, side)
        super().resizeEvent(event)

    def changeSelectedSize(self):
        parent = self.parent()
        children = parent.children()
        for child in children:
            if isinstance(child, SizeButton):
                child.setStyleSheet("""
                    SizeButton {
                        border: 1px solid silver;
                        background-color: rgba(240, 240, 240, 1.0)
                    }
                    """)
        self.setStyleSheet("""
            SizeButton {
                border: 1px solid silver;
                background-color: pink
            }
            """)
        self.sizeSignal.emit(self.penSize)
        self.update()


class InfoSection(QWidget):
    def __init__(self, playerName = "-", buttonText = "Save", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Layout = QHBoxLayout()

        self.playerLabel = QLabel("Player: " + playerName)
        self.nextButton = QPushButton(buttonText)

        self.playerLabel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.nextButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.Layout.addWidget(self.playerLabel, stretch=1)
        self.Layout.addWidget(self.nextButton, stretch=1)

        self.setLayout(self.Layout)
