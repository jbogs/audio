from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QVBoxLayout

from listener import Listener

class General(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(General, self).__init__(parent)
        self.resize(400, 400)
        self.offset = QtCore.QPoint(0, 0)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

        self.setStyleSheet("""
            QWidget {
                border: 2px solid gray;
            }
                           
            QLabel {
                border: 0px;
            }
        """)

      
        Listener.Get("data").subscribe(self.create)
        self.create()

    def create(self, data=None):
        

        wins = 3
        avg = "23/100"

        self.label1 = QLabel(f"Total Wins: {wins}")
        self.label3 = QLabel(f"Avg Placing: {avg}")
        
        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label3)
        self.setLayout(layout)
