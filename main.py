from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from TimeManager import TimeManager
from ClickableWidget import ClickableWidget

import sys

from PyQt5.QtWidgets import QVBoxLayout


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setMinimumSize(800, 600)
        self.setMaximumSize(1200,900)
        self.setWindowTitle("Paint CO")
        self.show()

        self.CentralWidget = QWidget()
        self.setCentralWidget(self.CentralWidget)
        self.CentralLayout = QVBoxLayout()
        self.CentralWidget.setLayout(self.CentralLayout)

        self.fillerWidget = ClickableWidget(timeManager)
        self.fillerWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.CentralLayout.addWidget(self.fillerWidget, stretch=1)

        self.saluteButton = QPushButton("Salute!")
        self.saluteButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.saluteButton.clicked.connect(self.salute)
        self.CentralLayout.addWidget(self.saluteButton, stretch=1)

        #self.fillerWidget.mousePressEvent()

    def salute(self):
        time = timeManager.getTime()
        sec = int(time / 1000)
        msec = int(time - sec * 1000)
        print(timeManager.timeToString() + "I salute you!")


app = QApplication(sys.argv)
timeManager = TimeManager()
window = MyMainWindow()

timeManager.start()


app.exec_()