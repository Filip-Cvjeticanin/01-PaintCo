from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from CentralWidgets.BaseModeWidget import BaseModeWidget
from globalData import GlobalData
from TimeManager import  TimeManager

class BaseSetup(BaseModeWidget):
    def __init__(self, title="", *args, **kwargs):
        super().__init__(*args, **kwargs)

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
        self.input1Layout = QHBoxLayout()
        self.input2Layout = QHBoxLayout()

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
        self.input1Wrapper = QWidget()
        self.input2Wrapper = QWidget()

        # Functional Widgets:
        self.title = QLabel(title)          #QLABEL
        self.startButton = QPushButton("Start")    #QPUSHBUTTON

        globalData = GlobalData.getInstance()
        self.playerNumberLabel = QLabel("Number of players:")
        self.playerNumberValue = QSpinBox()
        self.playerNumberValue.setMinimum(2)
        self.playerNumberValue.setMaximum(16)
        self.playerNumberValue.setValue(globalData.playerNumber)

        self.secondsPerTurnLabel = QLabel("Seconds per turn:")
        self.secondsPerTurnValue = QSpinBox()
        self.secondsPerTurnValue.setMinimum(5)
        self.secondsPerTurnValue.setMaximum(3600)
        self.secondsPerTurnValue.setValue(45)

        self.playerInputWidgets = []
        for i in range(16):
            new = QLineEdit()
            new.setPlaceholderText("Player " + str(i+1))
            font = new.font()
            font.setPointSize(15)
            new.setFont(font)
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
        self.input1Layout.setContentsMargins(0,0,0,0)
        self.input2Layout.setContentsMargins(0,0,0,0)

        #self.configWrapper.setStyleSheet("border: 2px dashed black")
        #self.playerWrapper.setStyleSheet("border: 2px dashed black")
        #self.title.setStyleSheet("border: 2px dashed black")
        #self.startButton.setStyleSheet("border: 2px dashed black")

        self.playerNumberLabel.setStyleSheet("border-color: red")
        self.secondsPerTurnLabel.setStyleSheet("border-color: blue")

        self.playerWrapper.setMaximumSize(800,600)
        self.playerWrapper.setMaximumSize(800,600)
        self.configWrapper.setMaximumSize(4000,120)

        for i in range(16):
            self.playerInputWidgets[i].setMaximumSize(400,40)
            self.playerInputWidgets[i].setMinimumSize(170,40)

        font = self.title.font()
        font.setPointSize(30)
        font.bold()
        self.title.setFont(font)

        self.playerNumberLabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        font = self.playerNumberLabel.font()
        font.setPointSize(14)
        self.playerNumberLabel.setFont(font)
        self.secondsPerTurnLabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        font = self.secondsPerTurnLabel.font()
        font.setPointSize(14)
        self.secondsPerTurnLabel.setFont(font)

        self.startButton.setMaximumSize(600,300)
        self.startButton.setMinimumSize(200, 50)

        # Add to layouts:
        self.mainLayout.addWidget(self.title, stretch=10,alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.addWidget(self.configWrapper, stretch=20)
        self.mainLayout.addWidget(self.playerWrapper, stretch=60, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.addWidget(self.startButton, stretch=10, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        self.configLayout.addWidget(self.configBlocks[0])
        self.configLayout.addWidget(self.configBlocks[1])

        self.configBlockLayouts[0].addWidget(self.playerNumberLabel, stretch=1)
        self.configBlockLayouts[0].addWidget(self.input1Wrapper, stretch=1)
        self.configBlockLayouts[1].addWidget(self.secondsPerTurnLabel, stretch=1)
        self.configBlockLayouts[1].addWidget(self.input2Wrapper, stretch=1)

        self.playerLayout.addWidget(self.playerBlocks[0])
        self.playerLayout.addWidget(self.playerBlocks[1])
        self.playerLayout.addWidget(self.playerBlocks[2])
        self.playerLayout.addWidget(self.playerBlocks[3])

        for i in range(4):
            for j in range(4):
                self.playerBlockLayouts[i].addWidget(self.playerInputWidgets[i*4 + j], alignment=Qt.AlignmentFlag.AlignHCenter)

        self.input1Layout.addWidget(self.playerNumberValue, alignment=Qt.AlignmentFlag.AlignLeft)
        self.input2Layout.addWidget(self.secondsPerTurnValue, alignment=Qt.AlignmentFlag.AlignLeft)


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

        self.input1Wrapper.setLayout(self.input1Layout)
        self.input2Wrapper.setLayout(self.input2Layout)

        self.applySignal()

        globalData = GlobalData.getInstance()
        self.enablePlayerInputs(globalData.playerNumber)

    def applySignal(self):
        self.playerNumberValue.valueChanged.connect(self.enablePlayerInputs)
        self.secondsPerTurnValue.valueChanged.connect(self.saveTurnTimer)
        for i in range(16):
            self.playerInputWidgets[i].textChanged.connect(self.savePlayerNames)

    def enablePlayerInputs(self, playerNum):
        for i in range(playerNum):
            self.playerInputWidgets[i].show()

        for i in range(playerNum, 16):
            self.playerInputWidgets[i].hide()

        globalData = GlobalData.getInstance()
        globalData.playerNumber = playerNum

    def saveTurnTimer(self, sec):
        globalData = GlobalData.getInstance()
        globalData.secondsPerTurn = sec

    def savePlayerNames(self, text = ""):
        globalData = GlobalData.getInstance()
        for i in range(16):
            globalData.playerNames[i] = self.playerInputWidgets[i].text()
        t = TimeManager.getInstance()

    def updatePlayerNames(self):
        globalData = GlobalData.getInstance()

        for i in range(16):
            self.playerInputWidgets[i].textChanged.disconnect()
            if globalData.playerNames[i] == "":
                self.playerInputWidgets[i].setPlaceholderText("Player " + str(i + 1))
            self.playerInputWidgets[i].setText(globalData.playerNames[i])
            self.playerInputWidgets[i].textChanged.connect(self.savePlayerNames)

    def update_(self, text =""):
        globalData = GlobalData.getInstance()
        self.playerNumberValue.setValue(globalData.playerNumber)
        self.secondsPerTurnValue.setValue(globalData.secondsPerTurn)
        self.enablePlayerInputs(globalData.playerNumber)
        self.updatePlayerNames()

