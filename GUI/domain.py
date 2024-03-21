from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtCore import QSize
import re

from listener import Listener

class IconButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setFixedSize(30,30)

        self.activeIcon = QIcon("./GUI/select.png")
        self.inactiveIcon = QIcon("./GUI/select-inactive.png")
        self.setIcon(self.activeIcon)
        self.setIconSize(QSize(25,25))
        
        self.setStyleSheet("""          
            QPushButton {
                background-color: #171717;
                padding: 0px;
                outline: none;
                border: none;
            }
        """)

    def pressEvent(self):
        self.setIcon(self.inactiveIcon)

    def resetEvent(self):
        self.setIcon(self.activeIcon)

class BorderedWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.active = True

        Listener.Get("data").subscribe(self.ready_again)
        
        # Set the frame style to include a border
        self.setFrameStyle(QFrame.Box | QFrame.Plain)

        # Create a layout to arrange child widgets within the frame
        layout = QHBoxLayout(self)
        
        self.text_input = QLineEdit()
        self.button = IconButton()

        # Connect the returnPressed signal to the on_enter_pressed method
        self.text_input.returnPressed.connect(self.activated)
        self.button.clicked.connect(self.activated)

        # Add child widgets to the layout
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)

        self.setStyleSheet("""
            QFrame {
                background-color: #171717;
                border-radius: 8px;
                border: 2px solid #2f2f2f;
                padding: 0px;
            }
             
            QLineEdit {
                font-size: 12px;
                border: none;
                padding: 0px;
            }
        """)

    def activated(self):
        if not self.active:
            return

        input = self.text_input.text().split(" ")


        arg1, arg2 = None, None
        
        if len(input) == 1:
            if self.is_ip_address(input[0]):
                arg1 = input[0]
            else:
                return
        elif len(input) == 2:
            if self.is_ip_address(input[0]) and self.is_domain_name(input[1]):
                arg1 = input[0]
                arg2 = input[1]
            else:
                return
        else:
            return

        self.active = False
        self.button.pressEvent()

        Listener.Get("query").notify(arg1, arg2)

        self.text_input.clear()

    def is_ip_address(self, string):
        ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        #ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        return re.match(ipv4_pattern, string) #or re.match(ipv6_pattern, string)

    def is_domain_name(self, string):
        domain_pattern = r'^([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
        return re.match(domain_pattern, string)

    def ready_again(self, data):
        self.active = True
        self.button.resetEvent()

class DomainInput(QFrame):
    def __init__(self, parent=None):
        super(DomainInput, self).__init__(parent)
        self.resize(400, 400)
        self.offset = QtCore.QPoint(0, 0)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

        self.setStyleSheet("""
            QLabel {
                padding-bottom: 10px;
            }
        """)

        # Create widgets
        self.label = QLabel("Voice Call")
        self.inputWidget = BorderedWidget()
        
        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.inputWidget)
        layout.addStretch(1)  # Add some vertical stretch
        self.setLayout(layout)

        