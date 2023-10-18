#PATTERN LETTERALI, il match viene specificato letteralmente
print("Primo esempio. Pattern letterali")
subject_value = [1,2,3,4]

match subject_value:
    case [1, 2 ,3 ,4]:
        print(f"Nell'oggetto di partenza è stata trovata la lista [1, 2 ,3 ,4]")


#Nell'esempio successivo il matching pattern chiede che venga riconosciuta una qualunque lista, il cui
#primo elemento è 1, e qualunque siano i restanti valori della lista, rappresentati dal carattere jolly "*",
#essi vengono assegnati alla variabile "resto" con l'espressione "*resto".
print("##################")
print("Secondo esempio. Operatore jolly '*'")
subject_value = [1,2,3,4]

match subject_value:
    case [1, *resto]:
        print(f"Il resto è {resto}")

