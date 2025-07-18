from PyQt5.QtCore import QTimer


class TimeManager:
    def __init__(self):
        self.timeElapsed = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)

    def start(self):
        print("Starting application...")
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def getTime(self):
        return self.timeElapsed

    def tick(self):
        self.timeElapsed += 10
        #if self.timeElapsed % 1000 == 0:
        #    sec = int(self.timeElapsed / 1000)
        #    msec = int(self.timeElapsed - sec * 1000)
        #    print(f"[{sec:0>4}:{msec:0>3}]: second passed!")

    def timeToString(self):
        time = self.timeElapsed
        sec = int(time / 1000)
        msec = int(time - sec * 1000)
        returnString = f"[{sec:0>4}:{msec:0>3}]: "
        return returnString