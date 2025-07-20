from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QVBoxLayout


from TimeManager import TimeManager
from CentralWidgets.MenuWidget import MenuWidget
from ClickableWidget import ClickableWidget





import sys




class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setMinimumSize(800,600)
        self.setWindowTitle("Paint CO")
        self.show()

        self.menuWidg = None
        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None


    def LaunchMenu(self):
        self.setCentralWidget(self.menuWidg)

    def LaunchCOPaint(self):
        self.setCentralWidget(self.label1)

    def LaunchPaintBattle(self):
        self.setCentralWidget(self.label2)

    def LaunchFreeDraw(self):
        self.setCentralWidget(self.label3)

    def LaunchGallery(self):
        self.setCentralWidget(self.label4)
    '''
        Example usage of a window with 2 widgets.
        
        self.setMinimumSize(800, 600)
        self.setMaximumSize(1200,900)
        self.setWindowTitle("Paint CO")
        self.show()

        self.CentralWidget = QWidget()
        self.setCentralWidget(self.CentralWidget)
        self.CentralLayout = QVBoxLayout()
        self.CentralWidget.setLayout(self.CentralLayout)

        self.fillerWidget = ClickableWidget(timeManager)
        self.fillerWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


        self.saluteButton = QPushButton("Salute!")
        self.saluteButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.saluteButton.clicked.connect(self.salute)
        self.CentralLayout.addWidget(self.saluteButton, stretch=1)
        self.CentralLayout.addWidget(self.fillerWidget, stretch=1)


    def salute(self):
        print(timeManager.timeToString() + "I salute you!")
    '''

if __name__ == "__main__":
    #Define app window and timer
    timeManager = TimeManager()
    app = QApplication(sys.argv)
    window = MyMainWindow()
    timeManager.start()

    window.menuWidg = MenuWidget()
    window.label1 = QLabel("CO Paint")
    window.label2 = QLabel("Paint Battle")
    window.label3 = QLabel("Free Draw")
    window.label4 = QLabel("Gallery")

    window.menuWidg.COPaintButton.clicked.connect(window.LaunchCOPaint)
    window.menuWidg.BattleButton.clicked.connect(window.LaunchPaintBattle)
    window.menuWidg.FreeDrawButton.clicked.connect(window.LaunchFreeDraw)
    window.menuWidg.GalleryButton.clicked.connect(window.LaunchGallery)



    window.setCentralWidget(window.menuWidg)

    app.exec()