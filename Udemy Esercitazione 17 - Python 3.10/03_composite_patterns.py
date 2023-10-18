#PATTERN OR "|", In questo esempio il case composito OR, definito dall'operatore "|", riconosce, in alternativa,
#una lista il cui elemento è "autunno", oppure (OR, "|") una lista
#il cui primo elemento è "inverno" e, in entrambi i casi, vediamo che ne assegna i restanti valori alla stessa
#variabile "msg"
print("Primo esempio. Pattern composito OR '|'")
subject_value = ["autunno", "stagione autunnale"]

match subject_value:
    case ["autunno", msg] | ["inverno", msg] | ["primavera", msg] :
        print(f"Nella {msg} fa più freddo.")


#PATTERN AS, In questo esempio attraverso la keyword "as", siamo in grado di assegnare ad una variabile il pattern
# che stato matchato
print("##################")
print("Secondo esempio. Pattern 'as' per salvare il pattern matchato")
subject_value = "estate"

match subject_value:
    case "autunno" | "inverno" as stagione:
        print(f"In {stagione} fa più freddo.")
    case "primavera" | "estate" as stagione:
        print(f"In {stagione} fa più caldo.")


