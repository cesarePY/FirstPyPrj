from pathlib import Path

#
home = Path.home()
print(home)

#Context manager permette di assegnare ad una variabile il puntatore ad un file
#modalità di apertura "rt" = read + text
with open("isolamisteriosa.txt","rt") as f:
    print(f.encoding)  #mostra la codifica del file UTF-8
    print("#######################")
    text = f.read(33)  # legge i primi 33 caratteri del file e li assegna alla variabile
    print(text)
    print("#######################")
    text = f.read() #legge l'intero file, a partire dal punto in cui il puntatore è arrivato
                    # e lo assegna alla variabile
    print(text)
    #content manager rilascia le risorse all'uscita del blocco "with"
    #quindi il file aperto puntato da "f" viene automaticamente chiuso al posto nostro

