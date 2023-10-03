#Operatori di unione "|" e "|-" per dizionari
#Inizializziamo due dizionari my_dict1 e my_dict2
my_dict1 = {"a": "primo", "b": "secondo", "c": "terzo"}
my_dict2 = {"d": "quarto", "a": "quinto"}

#Operatore di unione "|" UNION
#Da notare che la chiave "a" è presente in entrambe, e come valore viene preso l'ultimo, di my_dict2
#che sovrascrive quello di my_dict1
my_dict3 = my_dict1 | my_dict2
print(f'my_dict3 = my_dict1 | my_dict2 = {my_dict3}')


#Operatore di IN PLACE UNION "|=" fa l'unione e di my_dict2 e my_dict1 e riassegna il risultato a my_dict2
#In questo caso il valore di "a" riportato è quello di my_dict1 perchè my_dict1 è il secondo operando dell'unione
my_dict2 |= my_dict1
print(f'my_dict2 |= my_dict1 = {my_dict2}')
