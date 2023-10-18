import pymongo
from pymongo import MongoClient

# eseguo la connessione con mongodb
client = MongoClient('localhost', 27017)

# crea un database e lo chiamo testdb
# L'istruzione qui sotto crea il database "testdb" se non esiste già
db = client.testdb

# creo la collection (tipo tabella) persone
# L'istruzione qui sotto crea la collection "persone" se non esiste già
persone_coll = db.persone

persone_coll.create_index([("nome", pymongo.ASCENDING)])
persone_coll.create_index([("cognome", pymongo.ASCENDING)])
persone_coll.create_index([("computer", pymongo.ASCENDING)])

#crea un documento
p1 = {"nome": "Mario", "cognome": "Rossi", "eta": 30, "computer": ["asus", "apple"]}

#inserisce il documento nella collection in mongodb
persone_coll.insert_one(p1)

#crea un documento
p2 = {"nome": "Giuseppe", "cognome": "Verdi", "eta": 45, "computer": ["apple"]}

#inserisce il documento nella collection in mongodb
persone_coll.insert_one(p2)

