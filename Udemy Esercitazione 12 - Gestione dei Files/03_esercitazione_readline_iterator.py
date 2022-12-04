with open("isolamisteriosa.txt", "rt") as f:
    lineCounter = 0
    for linea in f:  #questo loop ad ogni iterazione legge una linea intera,
        # e quando sente l'EOL si ferma, e assegna alla variabile "linea"
        lineCounter += 1
        print(f"{lineCounter}: {linea}", end="")
    print("#######################")

#Altro modo per ottenere lo stesso risultato
print("########## RISULTATO SIMILE MA CON readlines() #############")
with open("isolamisteriosa.txt", "rt") as f:
    lineCounter = 0
    lines = f.readlines() #readlines ritorna una lista, dove ogni elemento è una linea del file di testo letto
    for linea in lines:  #questo loop scorre la lista "lines"

        lineCounter += 1
        print(f"{lineCounter}: {linea}", end="")
