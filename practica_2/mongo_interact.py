from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# with client:
#     db = client.coches
#     db.cars.insert_many([{"coche": "Tesla"}, {"coche": "Lada"}])

db = client["coches"]
collection = db["cars"]
collection.insert_one({"coche": "Tesla"})
