# def onAddedChildren(node, indexFrom, indexTo):
#     layer = node.children()[indexFrom].layer()
#     nome = layer.name()
#     tipo = layer.providerType()
#     f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "a")
#     f.write("'{}': '{}'".format(nome, tipo))
#     f.close()
#     print("'{}': '{}'".format(nome, tipo))

# root = QgsProject.instance().layerTreeRoot()
# root.addedChildren.connect(onAddedChildren)

# f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "a")
# f.write("cenas")
# f.close()

import requests

url = 'http://localhost:8000/jsonfile'
myobj = 'C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json'
f = open(myobj)
text = f.read()
print(text)

x = requests.post(url, files = dict(telemetry = text))

# myobjtelemetry = 'C:/Users/hugof/Dropbox/Agora/Projeto/telemetry.json'
# f2 = open(myobjtelemetry)
# text2 = f2.read()
# print(text2)

# x = requests.post(url, files = dict(telemetry = text2))