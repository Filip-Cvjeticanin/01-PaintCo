from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class BaseHeaderWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.baseHeaderLayout = QHBoxLayout()
        self.baseHeaderLayout.setSpacing(0)
        self.baseHeaderLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.baseHeaderLayout)

        #self.setStyleSheet("background-color: blue;")  # ✅ Background color
        #self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)  # ✅ Ensures it's painted

        self.backButton = QPushButton("← BACK")
        self.contentWrapper = QWidget()

        self.backButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.backButton.setMaximumSize(100,50)
        self.contentWrapper.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        #self.backButton.setStyleSheet("background-color: green")
        #self.contentWrapper.setStyleSheet("background-color: pink")

        self.baseHeaderLayout.addWidget(self.backButton, stretch=5)
        self.baseHeaderLayout.addWidget(self.contentWrapper, stretch=95)