from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QTabWidget, QLabel, QHBoxLayout

from map import MapWidget
from chart import LatencyChart
from general_data import General

class Varying(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Varying, self).__init__(parent)

        self.setStyleSheet("""
            QTabWidget {
                padding: 0px;
            }
                           
            QTabWidget::tab-bar {
                alignment: center;
            }

            QTabWidget::pane {
                border-top: 2px solid #C2C7CB; /* Top border color */
            }

            QTabBar::tab {
                background-color: #171717;
                font-size: 12pt;
                padding: 0px;
                border: 1px solid #C2C7CB; /* Border color of tabs */
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }

            QTabBar::tab:selected {
                background-color: #2f2f2f; /* Background color of selected tab */
            }

        """)

        # Create a layout for the widget
        main_layout = QVBoxLayout(self)

        # Create a label
        #label = QLabel("Statistics")
        #main_layout.addWidget(label)

        # Create a QHBoxLayout for the tab widget and the label
        tab_layout = QHBoxLayout()

        # Create a QTabWidget
        tab_widget = QTabWidget()

        # Add existing widgets to each tab
        map_widget = MapWidget()
        chart_widget = LatencyChart()
        general_widget = General()

        # Add tabs to the tab widget
        tab_widget.addTab(general_widget, "Stats")
        tab_widget.addTab(map_widget, "Location")
        tab_widget.addTab(chart_widget, "Latency")


        tab_layout.addWidget(tab_widget)
        main_layout.addLayout(tab_layout)