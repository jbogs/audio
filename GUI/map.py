from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import folium
import io
import pandas as pd
from ip2geotools.databases.noncommercial import DbIpCity

from listener import Listener

class MapWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Folium in PyQt Example')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.webView = QWebEngineView()
        layout.addWidget(self.webView)

        Listener.Get("data").subscribe(self.create)
        self.empty()

    def empty(self):
        coordinate = (39.8283, -98.5795)
        m = folium.Map(
            title='Stamen Terrain',
            zoom_start=3,
            location=coordinate
        )

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)
        data.seek(0)

        html = data.getvalue().decode()
        self.webView.setHtml(html)

    def ip_to_location(self, ip_address):
        response = DbIpCity.get(ip_address, api_key='free')
        return response.latitude, response.longitude
    
    def create(self, data):
        # starting point
        coordinate = (39.8283, -98.5795)
        m = folium.Map(
            title='Stamen Terrain',
            zoom_start=3,
            location=coordinate
        )

        hops = data['hops']
        locs = []

        for i in range(len(hops)):
            hop = hops[i]
            coord = (hop['lat'], hop['long'])
            locs.append(coord)
            color = 'blue'
            if i == 0:
                color = 'green'
            elif i == len(hops)-1:
                color = 'red'
            
            folium.Marker(
                location=coord,
                icon=folium.Icon(color=color, icon='none')
            ).add_to(m)

        folium.PolyLine(locations=locs, color='blue').add_to(m)

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)
        data.seek(0)

        html = data.getvalue().decode()

        self.webView.setHtml(html)

