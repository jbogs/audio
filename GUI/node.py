from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class Square(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(100, 100)
        self.offset = QtCore.QPoint(0, 0)
        self.scale_factor = 1.0
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setStyleSheet("background-color: red;")  # Set the background color to red

        # Create widgets
        self.label = QLabel("Hop1")

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addStretch(1)  # Add some vertical stretch

        self.setLayout(layout)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.translate(self.offset)
        qp.scale(self.scale_factor, self.scale_factor)
        pen = QtGui.QPen(QtGui.QColor(QtCore.Qt.black), 5)
        qp.setPen(pen)
        qp.drawRect(50, 50, 200, 200)