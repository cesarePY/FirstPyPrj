import os

with open("isolamisteriosa.txt","rb") as f:
    #leggi "quattro" dal file
    f.seek(119, os.SEEK_SET)
    parola = f.read(7).decode('utf-8')
    print(parola)

    #Leggi "uragano" dal file
    f.seek(-9, os.SEEK_END)
    parola = f.read(7).decode('utf-8')
    print(parola)

