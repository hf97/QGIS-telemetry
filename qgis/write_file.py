import json
from datetime import datetime, timezone
import uuid
import os
import json
import platform
from qgis.core import *
import qgis


################################################################
# from qgis.core import (
#   QgsProject,
#   QgsSettings,
#   QgsVectorLayer
# )
###################################
# Settings do qgis
# s = QgsSettings()
# s.value("UI/UITheme")
# s.value("locale/userLocale")
###################################

sid = uuid.UUID(bytes = os.urandom(16))
QgsExpressionContextUtils.setGlobalVariable("sid", str(sid))

# QgsExpressionContextUtils.setGlobalVariable("openQgis", 0)

try:
    openQgisGlobal = int(QgsExpressionContextUtils.globalScope().variable("openQgis"))
    QgsExpressionContextUtils.setGlobalVariable("openQgis", openQgisGlobal+1)
except:
    QgsExpressionContextUtils.setGlobalVariable("openQgis", 1)

def startUp():
    sessionId = str(sid)
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
        action_start = {"sessionId": sessionId, "type" : "start", "datetime" : datetime.now(timezone.utc).astimezone().isoformat(), "interface": interface,"plugins": plugins}
    except:
        action_start = {"sessionId": sessionId, "type" : "start", "datetime" : datetime.now(timezone.utc).astimezone().isoformat()}
    try:
        f = open(appdata + "/telemetry.json", "r+")
        obj = json.loads(f.read())
        f.close()
        f = open(appdata + "/telemetry.json", "w+")      
        obj["actions"].append(action_start)
        json.dump(obj, f, indent=4)
        f.close()
    except:
        f = open(appdata + "/telemetry.json", "w")
        json.dump({"actions":[action_start]}, f, indent=4)
        f.close()
startUp()




def onAddedChildren(node, indexFrom, indexTo):
    appdata=QgsApplication.qgisSettingsDirPath()
    layer = node.children()[indexFrom].layer()
    nome = layer.name()
    tipo = layer.providerType()
    now = datetime.now()
    sessionId = str(sid)
    addedLayer = {"sessionId": sessionId, "type" : "addedLayer", "datetime" : datetime.now(timezone.utc).astimezone().isoformat(),"name": nome,"extension":tipo}
    try:
        f = open(appdata + "/telemetry.json", "r+")
        obj = json.loads(f.read())
        f.close()
        print("ola")
        f = open(appdata + "/telemetry.json", "w+")
        obj["actions"].append(addedLayer)
        json.dump(obj, f, indent=4)
        f.close()
    except:
        print("except")
        f = open(appdata + "/telemetry.json", "w")
        json.dump({"actions":[addedLayer]}, f, indent=4)
        f.close()
    print("'{}': '{}'".format(nome, tipo))
root = QgsProject.instance().layerTreeRoot()
root.addedChildren.connect(onAddedChildren)



# MACRO CLOSE PROJECT ---------------------------

session = QgsExpressionContextUtils.globalScope().variable("sid")

def closeProject():
    openQgisGlobal = int(QgsExpressionContextUtils.globalScope().variable("openQgis"))
    QgsExpressionContextUtils.setGlobalVariable("openQgis", openQgisGlobal-1)
    appdata = QgsApplication.qgisSettingsDirPath()
    sessionId = session
    action_close = {"sessionId": sessionId, "type" : "close", "datetime" : datetime.now(timezone.utc).astimezone().isoformat()}
    try:
        f = open(appdata + "/telemetry.json", "r+")
        # f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "r+")
        obj = json.loads(f.read())
        f.close()
        f = open(appdata + "/telemetry.json", "w+")
        # f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w+")
        obj["actions"].append(action_close)
        json.dump(obj, f, indent=4)
        f.close()
    except:
        f = open(appdata + "/telemetry.json", "w")
        # f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w")
        json.dump({"actions":[action_close]}, f, indent=4)
        f.close()
    if (openQgisGlobal-1 <= 0):
        # url = 'http://localhost:8000/jsonfile'
        url="https://qgis-telemetry.herokuapp.com/jsonfile"
        myobj = appdata + "/telemetry.json"
        # myobj = 'C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json'
        f = open(myobj)
        text = f.read()
        x = requests.post(url, files = dict(telemetry = text), headers = {'User-Agent': 'QGIS-Telemetry'})
        f = open(appdata + "/telemetry.json", "w")
        f.close()
        QgsExpressionContextUtils.removeGlobalVariable("openQgis")
        
