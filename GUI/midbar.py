from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QSplitter, QPushButton
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QSize

from node_graph import NodeGraph

class Mid(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Mid, self).__init__(parent)
        self.resize(400, 400)
        self.offset = QtCore.QPoint(0, 0)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

        self.setStyleSheet("""
            QWidget {
                background-color: #212121;        
            }
        
            QSplitter:handle {
                background-color: #c0c0c0;
            }
        """)

        # Create widgets
        self.graph = NodeGraph()
        self.side = IconButton()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.side)
        layout.addWidget(self.graph)
        self.setLayout(layout)



class IconButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setFixedSize(30,30)

        self.activeIcon = QIcon("./GUI/hide.png")
        self.inactiveIcon = QIcon("./GUI/show.png")
        self.setIcon(self.activeIcon)
        self.setIconSize(QSize(25,25))
        
        self.setStyleSheet("""          
            QPushButton {
                padding: 0px;
                outline: none;
                border: none;
            }
        """)

    def pressEvent(self):
        self.setIcon(self.inactiveIcon)

    def resetEvent(self):
        self.setIcon(self.activeIcon)