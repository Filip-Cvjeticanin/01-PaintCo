from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *



class MenuWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.HorizontalLayout = QHBoxLayout()
        self.setLayout(self.HorizontalLayout)

        widg1 = QLabel("Label1")
        widg2 = QLabel("Label2")
        widg3 = QLabel("Label3")

        widg1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        widg2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        widg3.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        widg1.setStyleSheet("background-color: #ffcccb;")  # light red
        widg2.setStyleSheet("background-color: #ffcccb;")  # light red
        widg3.setStyleSheet("background-color: #ffcccb;")  # light red

        self.HorizontalLayout.addWidget(widg1, stretch=1)
        self.HorizontalLayout.addWidget(widg2, stretch=1)
        self.HorizontalLayout.addWidget(widg3, stretch=1)