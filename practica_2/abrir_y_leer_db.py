import sqlite3
from pandas import read_sql_query

def read_sqlite(dbfile):
    with sqlite3.connect(dbfile) as dbcon:
        tables = list(read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", dbcon)['name'])
        out = {tbl : read_sql_query(f"SELECT * from {tbl}", dbcon) for tbl in tables}
    return out

def object_dict(table, id):
    res = dict()
    for field in table:
        res[field] = table[field][id]
    return res

db = read_sqlite('love4pets.db')

print("CAMPOS:")
j = 1
for table in db:
    print(j, table)
    j += 1

print("\n\n")
# empleado = db['empleado'].to_dict()
# empleados = [employeer_dict(empleado, id) for id in range(len(empleado[list(empleado.keys())[0]]))]

def get_objects(db):
    for table in db:
        table_dict = db[table].to_dict()
        objects = [object_dict(table_dict, id) for id in range(len(table_dict[list(table_dict.keys())[0]]))]
        print(objects, end='\n\n\n\n')

# get_objects(db)
print(db['departamento'].to_dict())