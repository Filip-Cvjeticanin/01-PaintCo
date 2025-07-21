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
        self.configBlockLayouts = []
        for i in range(2):
            new = QHBoxLayout()
            self.configBlockLayouts.append(new)
        self.playerBlockLayouts = []
        for i in range(4):
            new = QVBoxLayout()
            self.playerBlockLayouts.append(new)

        # Wrappers:
        self.configWrapper = QWidget()
        self.playerWrapper = QWidget()
        self.configBlocks = []
        for i in range(2):
            new = QWidget()
            self.configBlocks.append(new)
        self.playerBlocks = []
        for i in range(4):
            new = QWidget()
            self.playerBlocks.append(new)

        # Functional Widgets:
        self.title = QWidget()          #QLABEL
        self.startButton = QWidget()    #QPUSHBUTTON

        self.playerNumberLabel = QWidget()
        self.playerNumberValue = QWidget()

        self.secondsPerTurnLabel = QWidget()
        self.secondsPerTurnValue = QWidget()

        self.playerInputWidgets = []
        for i in range(16):
            new = QWidget()
            self.playerInputWidgets.append(new)

        # Policy setup:
        self.configWrapper.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.playerWrapper.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.startButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Styling:
        self.baseLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.configBlockLayouts[0].setContentsMargins(0, 0, 0, 0)
        self.configBlockLayouts[1].setContentsMargins(0, 0, 0, 0)
        self.playerLayout.setContentsMargins(0, 0, 0, 0)
        self.playerLayout.setSpacing(0)

        self.configWrapper.setStyleSheet("border: 2px dashed black")
        self.playerWrapper.setStyleSheet("border: 2px dashed black")
        self.title.setStyleSheet("border: 2px dashed black")
        self.startButton.setStyleSheet("border: 2px dashed black")

        self.playerNumberLabel.setStyleSheet("border-color: red")
        self.secondsPerTurnLabel.setStyleSheet("border-color: blue")

        for i in range(16):
            self.playerInputWidgets[i]

        # Add to layouts:
        self.mainLayout.addWidget(self.title, stretch=10)
        self.mainLayout.addWidget(self.configWrapper, stretch=20)
        self.mainLayout.addWidget(self.playerWrapper, stretch=60)
        self.mainLayout.addWidget(self.startButton, stretch=10)

        self.configLayout.addWidget(self.configBlocks[0])
        self.configLayout.addWidget(self.configBlocks[1])

        self.configBlockLayouts[0].addWidget(self.playerNumberLabel)
        self.configBlockLayouts[0].addWidget(self.playerNumberValue)
        self.configBlockLayouts[1].addWidget(self.secondsPerTurnLabel)
        self.configBlockLayouts[1].addWidget(self.secondsPerTurnValue)

        self.playerLayout.addWidget(self.playerBlocks[0])
        self.playerLayout.addWidget(self.playerBlocks[1])
        self.playerLayout.addWidget(self.playerBlocks[2])
        self.playerLayout.addWidget(self.playerBlocks[3])

        for i in range(4):
            for j in range(4):
                self.playerBlockLayouts[i].addWidget(self.playerInputWidgets[i*4 + j])

        # Apply layouts:
        self.contentWrapper.setLayout(self.mainLayout)
        self.configWrapper.setLayout(self.configLayout)
        self.playerWrapper.setLayout(self.playerLayout)

        self.configBlocks[0].setLayout(self.configBlockLayouts[0])
        self.configBlocks[1].setLayout(self.configBlockLayouts[1])

        self.playerBlocks[0].setLayout(self.playerBlockLayouts[0])
        self.playerBlocks[1].setLayout(self.playerBlockLayouts[1])
        self.playerBlocks[2].setLayout(self.playerBlockLayouts[2])
        self.playerBlocks[3].setLayout(self.playerBlockLayouts[3])