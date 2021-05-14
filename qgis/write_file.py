import json

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

def openProject():
    try:
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "r+")
        obj = json.loads(f.read())
        f.close()
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w+")
        obj["actions"].append({"type" : "start"})
        json.dump(obj, f, indent=4)
        f.close()
    except:
        f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w")
        json.dump({"actions":[]}, f, indent=4)
        f.close()



def saveProject():
    pass

def closeProject():
    f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "w+")
    json.dump({"type" : "close"}, f)
    f.close()

openProject()