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

    def LaunchMenu(self):
        pass

    def LaunchCOPaint(self):
        pass

    def LaunchPaintBattle(self):
        pass

    def LaunchFreeDraw(self):
        pass

    def LaunchGallery(self):
        pass
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

    menuWidg = MenuWidget()
    window.setCentralWidget(menuWidg)


    app.exec()