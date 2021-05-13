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

f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/telemetry.json", "a")
f.write("cenas")
f.close()
