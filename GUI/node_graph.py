from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QVBoxLayout

from node import Square

from listener import Listener

class NodeGraph(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(NodeGraph, self).__init__(parent)
        self.resize(400, 400)
        self.offset = QtCore.QPoint(0, 0)
        self.scale_factor = 1.0
        self.setAttribute(QtCore.Qt.WA_StyledBackground)  
        self.setStyleSheet("""
            background-color: #212121;
        """)

        label = QLabel("Chat")
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addStretch(1)
        self.setLayout(layout)

        self.layout = layout
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        Listener.Get("data").subscribe(self.create)

    def create(self, data):
        old_layout = self.layout
        if old_layout is not None:
            while old_layout.count():
                item = old_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        label = QLabel("DNSSEC")
        label.setStyleSheet("""
            padding-bottom: 30px;
        """)

        self.layout.addWidget(label)

        for dns in data['dnssec']['dnssec']:
            label = QLabel(dns)
            if "NOT" in dns:
                label.setStyleSheet("""
                    color: red;
                    font-size: 16px;
                    padding: 4px;
                """)
            else:
                label.setStyleSheet("""
                    color: green;
                    font-size: 16px;
                    padding: 4px;
                """)
            self.layout.addWidget(label)

    def addNode(self):
        # Calculate the position for the first square to be in the middle of the window
        window_width = self.width()
        window_height = self.height()
        square_size = 100  # Assume square size

        square1_x = int((window_width - square_size) / 2)
        square1_y = int((window_height - square_size) / 2)

        # Create the first square and set its position
        self.square1 = Square(self)  # Red square
        self.square1.scale_factor = self.scale_factor
        self.square1.move(square1_x, square1_y)

        # Position the second square to the right of the first square
        square2_x = square1_x + (square_size*2)  # Position it to the right
        square2_y = square1_y  # Align vertically with the first square

        # Create the second square and set its position
        self.square2 = Square(self)  # Blue square
        self.square2.offset = self.offset
        self.square2.scale_factor = self.scale_factor
        self.square2.move(square2_x, square2_y)
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & QtCore.Qt.RightButton:
            delta = event.pos() - self.last_pos
            self.offset += delta
            self.last_pos = event.pos()
            self.square1.move(self.last_pos.x(), self.last_pos.y())
            self.square2.move(self.last_pos.x(), self.last_pos.y())
            self.update()


