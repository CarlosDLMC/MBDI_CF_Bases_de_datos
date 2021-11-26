from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['love4pets']
# collection = db["empleado"]
#
# documentos = collection.find()
#
# for d in documentos:
#     print(d)

# detalle_orden
# suministro
# producto
# departamento
# empleado
# mascota
# cliente
# proveedor
# orden

orden = db['orden']
for document in orden.find():
    print(document)
    print(type(document))
