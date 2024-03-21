from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QCursor

from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtCore import QSize


from listener import Listener

class History(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(History, self).__init__(parent)
        self.resize(400, 400)
        self.offset = QtCore.QPoint(0, 0)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)

        self.setStyleSheet("""
            QPushButton {
                background-color: #2f2f2f;
                font-size: 12pt;
            }
        """)

        # Create a scroll area
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)  # Allows the scroll area to resize its widget

        scroll_area.setStyleSheet(
            """
            QScrollArea {
                border: none;
                background: none;
            }

            QScrollBar:vertical {
                border: none;
                background: transparent; /* Background color of the scrollbar */
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

        # Create widgets
        self.label = QLabel("Voice Call")
        self.label.setStyleSheet("""
            QLabel {
                padding-bottom: 30px;
            }
        """)
        

        # Create a widget to contain the layout
        container = QtWidgets.QWidget()

        layout = QVBoxLayout(container)
        layout.addWidget(self.label)
        

        for i in range(5):
            layout.addWidget(BorderedWidget({
                'name' : "Jonathan",
                'icon' : "witch"
            }))
        
        scroll_area.setWidget(container)

        # Set up layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        self.layout = layout
        layout.addStretch(1)

        Listener.Get("user_added").subscribe(self.addUser)
        Listener.Get("user_removed").subscribe(self.removeUser)
        
    def removeUser(self, data, arg2=None):
        pass

    def addUser(self, data, arg2=None):
        self.layout.addWidget(BorderedWidget(data))

class IconButton(QPushButton):
    def __init__(self, icon, parent=None):
        super().__init__(parent)
        
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setFixedSize(30,30)

        self.activeIcon = QIcon(f"./GUI/imgs/{icon}.png")
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
    def __init__(self, data, parent=None):
        super().__init__(parent)

        name = data['name']
        icon = data['icon']
        
        # Set the frame style to include a border
        self.setFrameStyle(QFrame.Box | QFrame.Plain)

        # Create a layout to arrange child widgets within the frame
        layout = QHBoxLayout(self)
        
        self.text_input = QLineEdit()
        self.button = IconButton(icon)
        self.label = QLabel("Jonathan")

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setStyleSheet("""
            QFrame {
                background-color: #171717;
                border-radius: 8px;
                border: 2px solid #2f2f2f;
                padding: 0px;
            }
                           
            QLabel {
                border: none;
            }
             
            QLineEdit {
                font-size: 12px;
                border: none;
                padding: 0px;
            }
                           
            QLabel {
                padding: 0px;
            }
        """)


class HistoryButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        # Set the default style
        self.setStyleSheet('''
            QPushButton {
                background-color: #171717;
                font-size: 12pt;
                border-radius: 5px;
                text-align: left;
                padding: 10px;
            }
            
            QPushButton:hover {
                background-color: #2f2f2f;
            }
            
            QPushButton:pressed {
                background-color: #2f2f2f;
            }
        ''')

        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


    def mousePressEvent(self, event):
        #self.callback(self.text)
        pass

