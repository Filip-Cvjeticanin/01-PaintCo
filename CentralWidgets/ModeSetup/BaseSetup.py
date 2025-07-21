from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from CentralWidgets.BaseModeWidget import BaseModeWidget

class BaseSetup(BaseModeWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        # Layouts:
        self.mainLayout = QVBoxLayout()
        self.configLayout = QVBoxLayout()
        self.playerLayout = QHBoxLayout()

        # Wrappers:
        self.configWrapper = QWidget()
        self.playerWrapper = QWidget()

        # Functional Widgets:
        self.title = QWidget()          #QLABEL
        self.startButton = QWidget()    #QPUSHBUTTON

        # Policy setup:
        self.configWrapper.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.playerWrapper.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.startButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Styling:
        self.baseLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.configWrapper.setStyleSheet("border: 2px dashed black")
        self.playerWrapper.setStyleSheet("border: 2px dashed black")
        self.title.setStyleSheet("border: 2px dashed black")
        self.startButton.setStyleSheet("border: 2px dashed black")

        # Add to layouts:
        self.mainLayout.addWidget(self.title, stretch=10)
        self.mainLayout.addWidget(self.configWrapper, stretch=20)
        self.mainLayout.addWidget(self.playerWrapper, stretch=60)
        self.mainLayout.addWidget(self.startButton, stretch=10)



        self.contentWrapper.setLayout(self.mainLayout)