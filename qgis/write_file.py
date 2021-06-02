import json
from datetime import datetime
# import pytz
import uuid
import os
import json
import random
import platform
import requests


################################################################
# Usar isto mas nÃ£o sei meter a dar sem ser no qgis
# from qgis.core import (
#   QgsProject,
#   QgsSettings,
#   QgsVectorLayer
# )
###################################
# Isto vai buscar a settings do qgis
# s = QgsSettings()
# s.value("UI/UITheme")
# s.value("locale/userLocale")
###################################


# como vamos fazer para o sessionid ser armazendado na execucao e sabermos qual e sempre que se guarda coisas no json
sessionId = ""

# TODO meter sessionID como uuid no json

def startUp():
    sid = uuid.UUID(bytes = os.urandom(16))
    sessionId = str(sid)
    # now = datetime.now(pytz.utc)
    now = datetime.now()
    try:
        s = QgsSettings()
        interface = {}
        interface["OS"] = platform.system()
        interface["language"] = s.value("locale/userLocale")
        interface["locale"] = s.value("locale/globalLocale")
        interface["uiTheme"] = s.value("UI/UITheme")
        interface["version"] = Qgis.QGIS_VERSION

        #Buscar os plugins
        appdata=QgsApplication.qgisSettingsDirPath()
        loc = appdata + "/python/plugins"
        plugins={}
        for x in qgis.utils.findPlugins(loc):
            plugin={}
            plugin["version"] = x[1].get('general',"version")
            plugins[x[0]] = plugin
        action_start = {"sessionId": sessionId, "type" : "start", "datetime" : now.isoformat(), "interface": interface,"plugins": plugins}
    except:
        action_start = {"sessionId": sessionId, "type" : "start", "datetime" : now.isoformat()}
    try:
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "r+")
        obj = json.loads(f.read())
        f.close()
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w+")      
        obj["actions"].append(action_start)
        json.dump(obj, f, indent=4)
        f.close()
    except:
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w")
        json.dump({"actions":[action_start]}, f, indent=4)
        f.close()

# execute startup
startUp()




def closeProject():
    # now = datetime.now(pytz.utc)
    now = datetime.now()
    sessionId = 0
    action_close = {"sessionId": sessionId, "type" : "close", "datetime" : now.isoformat()}
    try:
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "r+")
        obj = json.loads(f.read())
        f.close()
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w+")
        obj["actions"].append(action_close)
        json.dump(obj, f, indent=4)
        f.close()
    except:
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w")
        json.dump({"actions":[action_close]}, f, indent=4)
        f.close()
    url = 'http://localhost:8000/jsonfile'
    myobj = 'C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json'
    f = open(myobj)
    text = f.read()
    # print(text)
    x = requests.post(url, files = dict(telemetry = text))

closeProject()

def postQGIS():
    req = QNetworkRequest (QUrl("http://127.0.0.1:8000/jsonfile"))
    manager=QNetworkAccessManager()
    data= QByteArray()
    data.append("name=Filipe")
    manager.post(req,data)

def onAddedChildren(node, indexFrom, indexTo):
    layer = node.children()[indexFrom].layer()
    nome = layer.name()
    tipo = layer.providerType()
    now = datetime.now()
    sessionId = 0
    addedLayer = {"sessionId": sessionId, "type" : "addedLayer", "datetime" : now.isoformat(),"name": nome,"extension":tipo}
    try:
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "r+")
        obj = json.loads(f.read())
        f.close()
        print("ola")
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w+")
        obj["actions"].append(addedLayer)
        json.dump(obj, f, indent=4)
        f.close()
    except:
        print("except")
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w")
        json.dump({"actions":[addedLayer]}, f, indent=4)
        f.close()
    print("'{}': '{}'".format(nome, tipo))

root = QgsProject.instance().layerTreeRoot()
root.addedChildren.connect(onAddedChildren)