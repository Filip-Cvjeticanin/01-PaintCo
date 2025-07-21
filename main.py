from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QVBoxLayout

from CentralWidgets.ModeSetup.BaseSetup import BaseSetup
from TimeManager import TimeManager
from CentralWidgets.MenuWidget import MenuWidget
from CentralWidgets.BaseModeWidget import BaseModeWidget
from globalData import GlobalData
from ClickableWidget import ClickableWidget






import sys




class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setMinimumSize(800,600)
        self.setWindowTitle("Paint CO")
        self.show()

        self.menuWidg = None
        self.mode1 = None
        self.mode2 = None
        self.mode3 = None
        self.mode4 = None

    def switchCentralWidgetTo(self, widget):
        current = self.centralWidget()
        if current is not None:
            current.setParent(None)  # Prevent auto-delete
        self.setCentralWidget(widget)

    def LaunchMenu(self):
        self.switchCentralWidgetTo(self.menuWidg)

    def LaunchCOPaint(self):
        self.switchCentralWidgetTo(self.mode1)

    def LaunchPaintBattle(self):
        self.switchCentralWidgetTo(self.mode2)

    def LaunchFreeDraw(self):
        self.switchCentralWidgetTo(self.mode3)

    def LaunchGallery(self):
        self.switchCentralWidgetTo(self.mode4)


if __name__ == "__main__":
    globalData = GlobalData.getInstance()
    globalData.COPaintTurn = 60
    #Define app window and timer
    timeManager = TimeManager.getInstance()
    app = QApplication(sys.argv)
    window = MyMainWindow()
    timeManager.start()

    window.menuWidg = MenuWidget()          # Add the MenuWidget as a member to the window.
    window.mode1 = BaseSetup()  # Add the Modes as a members to the window.
    window.mode2 = BaseModeWidget(QLabel("Paint Battle"))
    window.mode3 = BaseModeWidget(QLabel("Free Draw"))
    window.mode4 = BaseModeWidget(QLabel("Gallery"))

    # Connect buttons for each mode.
    window.menuWidg.COPaintButton.clicked.connect(window.LaunchCOPaint)
    window.menuWidg.BattleButton.clicked.connect(window.LaunchPaintBattle)
    window.menuWidg.FreeDrawButton.clicked.connect(window.LaunchFreeDraw)
    window.menuWidg.GalleryButton.clicked.connect(window.LaunchGallery)

    # Connect back buttons for each mode.
    window.mode1.backButton.clicked.connect(window.LaunchMenu)
    window.mode2.backButton.clicked.connect(window.LaunchMenu)
    window.mode3.backButton.clicked.connect(window.LaunchMenu)
    window.mode4.backButton.clicked.connect(window.LaunchMenu)


    window.setCentralWidget(window.menuWidg)


    app.exec()