import json
from datetime import datetime
import uuid
import os
import json
import random
import platform


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
    now = datetime.now()
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
