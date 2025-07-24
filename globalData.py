from PySide6.QtCore import *

class GlobalData:
    _instance = None
    playerNames = []
    playerNumber = 5
    secondsPerTurn = 45
    availableColors = [Qt.GlobalColor.black,
                       Qt.GlobalColor.white,
                       Qt.GlobalColor.red,
                       Qt.GlobalColor.blue,
                       Qt.GlobalColor.yellow,
                       Qt.GlobalColor.green,
                       Qt.GlobalColor.magenta]
    availableSizes = [1, 2, 4, 6, 9, 12, 15, 30]

    def __init__(self):
        self.COPaintTurn = 120
        self.resolutionChoice = 1
        for i in range(16):
            self.playerNames.append("")

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()  # __init__ runs only once
        return cls._instance