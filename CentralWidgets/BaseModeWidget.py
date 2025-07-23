from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from CentralWidgets.BaseHeaderWidget import BaseHeaderWidget

class BaseModeWidget(QWidget):
    def __init__(self, receivedContentWidget = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if receivedContentWidget is None: receivedContentWidget = QWidget()

        self.baseLayout = QVBoxLayout()
        self.baseLayout.setSpacing(0)
        self.setLayout(self.baseLayout)

        self.headerWrapper = BaseHeaderWidget()
        self.contentWrapper = receivedContentWidget
        self.backButton = self.headerWrapper.backButton

        self.headerWrapper.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.contentWrapper.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.headerWrapper.setAutoFillBackground(True)
        self.contentWrapper.setAutoFillBackground(True)

        #self.headerWrapper.setStyleSheet("background-color: blue")
        #self.contentWrapper.setStyleSheet("background-color: red")

        self.baseLayout.addWidget(self.headerWrapper, stretch=8)
        self.baseLayout.addWidget(self.contentWrapper, stretch=92)


