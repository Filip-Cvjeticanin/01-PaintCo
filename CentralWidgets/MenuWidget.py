from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *



class MenuWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Init layout.
        self.HorizontalLayout = QHBoxLayout()
        self.setLayout(self.HorizontalLayout)

        # Init basic widgets.
        self.leftFiller = QWidget()
        self.buttonsWrapper = QWidget()
        self.rightFiller = QWidget()
        #self.buttonsWrapper.setStyleSheet("background-color: #ffcccb;")  # light red
        self.HorizontalLayout.addWidget(self.leftFiller, stretch=5)
        self.HorizontalLayout.addWidget(self.buttonsWrapper, stretch=10)
        self.HorizontalLayout.addWidget(self.rightFiller, stretch=5)

        # Customize button wrapper.
        self.WrapperLayout = QVBoxLayout()
        self.buttonsWrapper.setLayout(self.WrapperLayout)

        self.title = QLabel("CO Paint")
        self.title.setStyleSheet("font-size: 36px;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.COPaintButton = QPushButton("CO Paint")
        self.BattleButton = QPushButton("Paint Battle")
        self.FreeDrawButton = QPushButton("Free Draw")
        self.GalleryButton = QPushButton("Gallery")
        self.blank1 = QWidget()
        self.blank2 = QWidget()
        self.blank3 = QWidget()
        self.blank4 = QWidget()
        self.blank5 = QWidget()

        self.COPaintButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.BattleButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.FreeDrawButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.GalleryButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.COPaintButton.setStyleSheet("font-size: 20px; ")
        self.BattleButton.setStyleSheet("font-size: 20px; ")
        self.FreeDrawButton.setStyleSheet("font-size: 20px; ")
        self.GalleryButton.setStyleSheet("font-size: 20px; ")

        self.WrapperLayout.addWidget(self.title, stretch=18)
        self.WrapperLayout.addWidget(self.blank1, stretch=2)
        self.WrapperLayout.addWidget(self.COPaintButton, stretch=10)
        self.WrapperLayout.addWidget(self.blank2,stretch=5)
        self.WrapperLayout.addWidget(self.BattleButton, stretch=10)
        self.WrapperLayout.addWidget(self.blank3, stretch=5)
        self.WrapperLayout.addWidget(self.FreeDrawButton, stretch=10)
        self.WrapperLayout.addWidget(self.blank4, stretch=5)
        self.WrapperLayout.addWidget(self.GalleryButton, stretch=10)
        self.WrapperLayout.addWidget(self.blank5, stretch=25)