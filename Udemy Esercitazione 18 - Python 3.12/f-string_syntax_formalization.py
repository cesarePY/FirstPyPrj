

libro = {
    "titolo": "L'isola misteriosa",
    "autore": "Jules Verne",
    "anno": 1875
}


#Con python 3.12 è possibile utilizzare lo stesso tipo di apici all'interno dell'espressione {} della stringa formattata
prima_stringa = f"Prima stringa: Libro: {libro["titolo"]}"
print(prima_stringa)

print("###########")
#E' stata aggiunta anche la possibilità di specificare caratteri speciali, as esempio '\n' nelle espressioni {}
seconda_stringa = f"Vado{"\n"}a capo"
print(seconda_stringa)

print("###########")
#Infine è stata aggiunta la possibilità di aggiungere commenti nelle espressioni {} multi linea.
terza_stringa = f"""Questo è l'autore del libro: {
libro['autore'].lower() #nome in minuscolo
}"""
print(terza_stringa)