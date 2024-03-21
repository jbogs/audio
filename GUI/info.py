from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QVBoxLayout

from listener import Listener

class Info(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Info, self).__init__(parent)
        self.resize(400, 400)
        self.offset = QtCore.QPoint(0, 0)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

        self.setStyleSheet("""
            QLabel {
                padding-bottom: 10px;
            }
        """)


        # Create a scroll area
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)  # Allows the scroll area to resize its widget

        scroll_area.setStyleSheet(
            """
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0; /* Background color of the scrollbar */
                width: 10px; /* Width of the scrollbar */
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #606060; /* Color of the scrollbar handle */
                min-height: 20px; /* Minimum height of the scrollbar handle */
                border-radius: 5px; /* Border radius of the scrollbar handle */
            }
            QScrollBar::add-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            """
        )

   
        label = QLabel("Router Hops")
        
        # Create a widget to contain the layout
        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(container)


        # Set the container widget as the widget of the scroll area
        scroll_area.setWidget(container)

        # Set up layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(label)
        main_layout.addWidget(scroll_area)

        self.layout = layout

        Listener.Get("data").subscribe(self.update)


    def update(self, data):
        hops = data['hops']

        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)

        for hop in hops:
            self.layout.addWidget(Ele(hop))
        



class Ele(QtWidgets.QWidget):
    def __init__(self, data, parent=None):
        super(Ele, self).__init__()
        self.resize(100, 100)
        self.offset = QtCore.QPoint(0, 0)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

        self.setStyleSheet("""
            QWidget {
                border: 2px solid gray;
            }
                           
            QLabel {
                border: 0px;
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

        # Set up layout
        layout = QVBoxLayout()

        self.label1 = QLabel("Hop: " + str(int(data['num']) + 1))
        layout.addWidget(self.label1)

        if data['lat'] and data['long']:
            self.label2 = QLabel("Coords: " + str(data['lat']) + ", " + str(data['long']))
            layout.addWidget(self.label2)
        if data['city'] and data['country']:
            self.label4 = QLabel("Location: " + data['city'] + ", " + data['country'])
            layout.addWidget(self.label4)
        
        self.setLayout(layout)