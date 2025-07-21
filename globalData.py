class GlobalData:
    _instance = None
    playerNames = []

    def __init__(self):
        self.COPaintTurn = 120
        self.resolutionChoice = 1
        for i in range(16):
            self.playerNames.append("Player " + str(i + 1))

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()  # __init__ runs only once
        return cls._instance