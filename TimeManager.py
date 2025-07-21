from PySide6.QtCore import QTimer


class TimeManager:
    _instance = None

    def __init__(self):
        self.timeElapsed = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()  # __init__ runs only once
        return cls._instance

    def start(self):
        print("Starting application...")
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def getTime(self):
        return self.timeElapsed

    def tick(self):
        self.timeElapsed += 10

    def timeToString(self):
        time = self.timeElapsed
        sec = int(time / 1000)
        msec = int(time - sec * 1000)
        returnString = f"[{sec:0>4}:{msec:0>3}]: "
        return returnString