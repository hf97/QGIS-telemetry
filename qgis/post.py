import json
import requests
# req = QNetworkRequest (QUrl("http://127.0.0.1:8000/jsonfile"))
# manager=QNetworkAccessManager()
# url="http://127.0.0.1:8000/jsonfile"
url="https://qgis-telemetry.herokuapp.com/jsonfile"
f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "r+")
obj = f.read()
x = requests.post(url, files = dict(telemetry = obj), headers = {'User-Agent': 'QGIS-Telemetry'})
# x = requests.post(url, files = dict(telemetry = obj))
