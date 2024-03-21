from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from random import randint

from listener import Listener

class LatencyChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Latency Chart')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create a PlotWidget
        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)

        # Set up the plot
        self.plot_widget.setLabel('left', 'Latency', units='ms')
        self.plot_widget.setLabel('bottom', 'Router Hops')
        self.plot_widget.showGrid(x=True, y=True)

        # Add a line plot item
        self.line = self.plot_widget.plot(pen='b')

        # Generate some sample data
        self.x_data = np.arange(10)  # Router hops
        self.y_data = [randint(10, 100) for _ in range(10)]  # Latency data

        Listener.Get("data").subscribe(self.update_plot)

    def update_plot(self, data):
        latencys = data['dnssec']['latency']

        x = []
        y = []
        for i in range(len(latencys)):
            x.append(latencys[i])
            y.append(i)
        # Update the line plot with new data
        self.line.setData(y, x)