from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QVBoxLayout

from CentralWidgets.ModeSetup.BaseSetup import BaseSetup
from TimeManager import TimeManager
from CentralWidgets.MenuWidget import MenuWidget
from CentralWidgets.BaseModeWidget import BaseModeWidget
from globalData import GlobalData
from CentralWidgets.CanvasMode import CanvasMode
from CentralWidgets.CustomWidgets.Canvas import Canvas
from ClickableWidget import ClickableWidget






import sys




class MyMainWindow(QMainWindow):
    menuWidg: MenuWidget
    mode1: BaseSetup
    mode2: BaseSetup
    mode3: CanvasMode
    mode4: BaseModeWidget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setMinimumSize(800,600)
        self.setWindowTitle("Paint CO")
        self.show()

    def switchCentralWidgetTo(self, widget):
        current = self.centralWidget()
        if current is not None:
            current.setParent(None)  # Prevent auto-delete
        self.setCentralWidget(widget)

    def LaunchMenu(self):
        self.switchCentralWidgetTo(self.menuWidg)

    def LaunchCOPaintSettings(self):
        self.mode1.update_()
        self.switchCentralWidgetTo(self.mode1)

    def LaunchCOPaint(self):
        for i in range(16):
            globalData.playerNames[i] = self.mode1.playerInputWidgets[i].text()
        print(globalData.playerNames)

        globalData.playerNumber = self.mode1.playerNumberValue.value()
        globalData.secondsPerTurn = self.mode1.secondsPerTurnValue.value()

        print(globalData.playerNumber)
        print(globalData.secondsPerTurn)
        print(self.mode1.backButton.size())

    def LaunchPaintBattleSettings(self):
        self.mode2.update_()
        self.switchCentralWidgetTo(self.mode2)

    def LaunchPaintBattle(self):
        for i in range(16):
            globalData.playerNames[i] = self.mode2.playerInputWidgets[i].text()
        print(globalData.playerNames)

        globalData.playerNumber = self.mode2.playerNumberValue.value()
        globalData.secondsPerTurn = self.mode2.secondsPerTurnValue.value()

        print(globalData.playerNumber)
        print(globalData.secondsPerTurn)
        print(self.mode2.backButton.size())

    def LaunchFreeDraw(self):
        self.switchCentralWidgetTo(self.mode3)

    def LaunchGallery(self):
        self.switchCentralWidgetTo(self.mode4)

    def exitFreeDraw(self):
        self.mode3.canvasInstance.clear()
        self.switchCentralWidgetTo(self.menuWidg)

    def saveFree(self):
        canvas = self.mode3.canvasInstance.canvas
        if canvas.save("output.jpg"):
            print(f"Canvas successfully saved to output.jpg")
        else:
            print("Failed to save canvas.")


if __name__ == "__main__":
    globalData = GlobalData.getInstance()
    globalData.COPaintTurn = 60
    #Define app window and timer
    timeManager = TimeManager.getInstance()
    app = QApplication(sys.argv)
    window = MyMainWindow()
    timeManager.start()

    window.menuWidg = MenuWidget()          # Add the MenuWidget as a member to the window.
    window.mode1 = BaseSetup("CO paint")  # Add the Modes as a members to the window.
    window.mode2 = BaseSetup("Paint Battle")
    window.mode3 = CanvasMode()
    window.mode4 = BaseModeWidget(QLabel("Gallery"))

    # Connect buttons for each mode.
    window.menuWidg.COPaintButton.clicked.connect(window.LaunchCOPaintSettings)
    window.menuWidg.BattleButton.clicked.connect(window.LaunchPaintBattleSettings)
    window.menuWidg.FreeDrawButton.clicked.connect(window.LaunchFreeDraw)
    window.menuWidg.GalleryButton.clicked.connect(window.LaunchGallery)

    # Connect back buttons for each mode.
    window.mode1.backButton.clicked.connect(window.LaunchMenu)
    window.mode2.backButton.clicked.connect(window.LaunchMenu)
    window.mode3.backButton.clicked.connect(window.exitFreeDraw)
    window.mode4.backButton.clicked.connect(window.LaunchMenu)
    window.mode1.startButton.clicked.connect(window.LaunchCOPaint)
    window.mode2.startButton.clicked.connect(window.LaunchPaintBattle)
    window.mode3.bindNextButton(window.saveFree)


    window.setCentralWidget(window.menuWidg)


    app.exec()
    print(window.mode1.playerWrapper.size())