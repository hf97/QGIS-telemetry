import json
from datetime import datetime
import uuid, OpenSSL
import json
import datetime
import random
import platform

################################################################
# Usar isto mas nÃ£o sei meter a dar sem ser no qgis
# from qgis.core import (
#   QgsProject,
#   QgsSettings,
#   QgsVectorLayer
# )
###############################################################
# def openProject():
#     f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "r+")
#     # print(f.read())
#     # f.seek(0)
#     obj = json.loads(f.read())
#     # obj = json.loads("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json")
#     try:
#         # obj["actions"].append({"type" : "start"})
#         obj["actions"].update({"type" : "start"})
#         json.dump(obj, f, indent=4)
#         # json.dump(obj, f)
#         pass
#     except:
#         pass
#     print(obj)
#     f.close()

# como vamos fazer para o sessionid ser armazendado na execucao e sabermos qual e sempre que se guarda coisas no json
sessionId = 0

def openProject():
    # sessionId = uuid.UUID(bytes = OpenSSL.rand.bytes(16))
    now = datetime.now()
    action_start = {"sessionId": sessionId, "type" : "start", "datetime" : now.isoformat()}
    try:
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "r+")
        obj = json.loads(f.read())
        f.close()
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w+")
        currentPlatform = platform.system()
        j={}
        j["sessionId"] = sessionId
        j["type"] = "open"
        j["datetime"] = str(x)
        interface={}
        interface["OS"] = currentPlatform
        j["interface"] = interface
        
        ###################################
        # Isto vai buscar a settings do qgis
        # s = QgsSettings()
        # s.value("UI/UITheme")
        # s.value("locale/userLocale")
        ###################################
        obj["actions"].append(action_start)
        json.dump(obj, f, indent=4)
        f.close()
    except:
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w")
        json.dump({"actions":[action_start]}, f, indent=4)
        f.close()



def saveProject():
    pass



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

openProject()
closeProject()

