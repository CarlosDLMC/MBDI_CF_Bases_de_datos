from pymongo import MongoClient

client = MongoClient('localhost')

lista = client.list_database_names()
lista.remove('admin')
lista.remove('config')
lista.remove('local')
print(lista)
print(type(client.list_database_names()))
db = client["love4pets"]
departamento = db["departamento"]
# departamento.insert_one({"nombre": "Pedro", "Hijos": ["Vadim", "Alfonso", "Pepe"]})


print("Antes:", departamento.count_documents({}))
# departamento.delete_many({"nombre": "Pedro"})
print("Después:", departamento.count_documents({}))

for d in departamento.find():
    print(d)
