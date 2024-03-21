from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

from domain import DomainInput
from history import History

class Left(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Left, self).__init__(parent)
        self.resize(400, 400)
        self.offset = QtCore.QPoint(0, 0)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

        self.history = History()
        #self.input = DomainInput()
        #self.input.inputWidget.callback = self.history.addElement
        
        # Set up layout
        layout = QVBoxLayout()
        #layout.addWidget(self.input, 1)
        layout.addWidget(self.history)
        self.setLayout(layout)

    def domainSelected(text):
        pass
    
    def domainLoaded():
        pass
