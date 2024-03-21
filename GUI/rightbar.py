from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QSplitter

from tabs import Varying
from info import Info

class Right(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Right, self).__init__(parent)
        self.resize(400, 400)
        self.offset = QtCore.QPoint(0, 0)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

        self.setStyleSheet("""
            QLabel {
                
            }

            QPushButton {
                background-color: #2f2f2f;
                font-size: 12pt;
            }
                           
            QLineEdit {
                border: 2px solid gray;
                border-radius: 10px;
                padding: 2px;
                font-size: 12px;
            }
        """)

        # Create widgets
        self.variying = Varying()
        self.info = Info()

        # Set up layout with splitter
        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(self.variying)
        #splitter.addWidget(self.info)
        splitter.setHandleWidth(4) 

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(splitter)
    
        self.setLayout(layout)