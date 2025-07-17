from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

from PyQt5.QtWidgets import QVBoxLayout


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def salute():
    print("Hello from button!")

app = QApplication(sys.argv)






window = MyMainWindow()
window.setWindowTitle("Paint CO")
window.show()
window.resize(800, 600)
window.show()

widget = QWidget()
window.setCentralWidget(widget)

layout = QVBoxLayout()
button = QPushButton("Salute!")

layout.addWidget(button)
widget.setLayout(layout)

button.clicked.connect(salute)




app.exec_()