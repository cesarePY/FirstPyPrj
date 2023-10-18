import pymongo
from pymongo import MongoClient

# eseguo la connessione con mongodb
client = MongoClient('localhost', 27017)

# accede al db testdb, se non ci fosse stato, lo avrebbe creato
# L'istruzione qui sotto crea il database "testdb" se non esiste già
db = client.testdb

# creo la collection (tipo tabella) persone
# L'istruzione qui sotto permettere di accedere alla collection "persone"
#se non fosse esistita l'avrebbe creata, ma vuota
persone_coll = db.persone

#trova il primo documento nella collezione "persone"
print("#########\nPrima persona")
p = persone_coll.find_one()
print(p)


print("#########\nPersone con computer Apple")
persone = persone_coll.find({"computer": "apple"})
for persona in persone:
    print(persona)

print("#########\nAggiorna l'età di Giuseppe a 50 anni")
res = persone_coll.update_one({"nome": "Giuseppe"}, {"$set": {"eta": 50}})
p = persone_coll.find_one({"nome": "Giuseppe"})
print(p)


print("#########\nAggiorna l'età di Giuseppe a 60 anni")
res = persone_coll.update_one({"nome": "Giuseppe"}, {"$set": {"eta": 60}})
p = persone_coll.find_one({"nome": "Giuseppe"})
print(p)

#Filtro più complesso
#trova il primo documento nella collezione "persone" con il nome maggiore di "Giuseppe"
print("#########\nPrima persona con il nome > di Giuseppe")
p = persone_coll.find_one({"nome" : {"$gt": "Giuseppe"}})
print(p)

