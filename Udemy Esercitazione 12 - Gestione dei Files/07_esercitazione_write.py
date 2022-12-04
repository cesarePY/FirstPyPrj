#Consegna:
#Apri file isolamisteriosa.txt in modalità lettura/testo
#Apri file outputfile.txt in modalità scrittura/testo
#Leggi intero file in un loop for-in con readlines()
#Utilizza un contatore inizializzato a 1
#Scrivi in outputfile.txt solo le linee dispari di isolamisteriosa.txt
#Anteponendo il contatore come prefisso ad ogni linea

with open("isolamisteriosa.txt", "rt") as fileIn, open("outputfile.txt", "wt") as fileOut:
    lines = fileIn.readlines()
    lineCounter = 1
    for line in lines:
        if lineCounter % 2 == 1:
            fileOut.writelines(f'{lineCounter}: {line}')
        lineCounter += 1
