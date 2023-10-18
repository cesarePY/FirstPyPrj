
#PATTERN MATCHING
#Il pattern matching serve a riconoscere strutture ed elementi in oggetti, ed estrarne il contenuto
#per poi riutilizzarlo nell'esecuzione del codice successivo
#Nell'esempio qui sotto, è stato riconosciuto che "subject_value" è una lista di due elementi
#questi due elementi sono stati estratti ed assegnati alle due variabili "p" ed "s".
subject_value = [1,2]
print("Primo esempio")
match subject_value:
    case [p, s]:
        print(f"Nell'oggetto di partenza sono stati trovati '{p}' e '{s}'")


#DEFAULT PATTERN MATCHING CASE
#In questo secondo esempio, una lista di 4 elementi non sarà riconosciuta nei due primi case
#che cercano di riconoscere, rispettivamente, una lista di 2 e di 3 elementi
#Quindi alla fine della struttura di match, possiamo definire un case finale
#di default con il carattere jolly "_", che verrà sempre riconosciuto
print("##################")
print("Secondo esempio")
subject_value = [1,2,3,4]

match subject_value:
    case [p, s]:
        print(f"Nell'oggetto di partenza sono stati trovati '{p}' e '{s}'")
    case [p, s, t]:
        print(f"Nell'oggetto di partenza sono stati trovati '{p}', '{s}' e '{t}'")
    case _:
        print(f"Nell'oggetto di partenza non sono stati trovati pattern riconoscibili")

