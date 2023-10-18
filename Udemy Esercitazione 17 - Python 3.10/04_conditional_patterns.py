#Pattern con test condizionale. Nell'esempio successivo, i primi due case si aspettano un valore di tipo lista,
#con primo valore, rispettivamente, "pari" e "dispari", e testano il fatto che il valore successivo sia pari o
#dispari come test condizionale per eseguire il contenuto del case.
#L'esempio finisce con un case di default "_", che si attiva qualora nessuno dei due case precedenti venisse
#attivato con successo.
print("Primo esempio. Pattern matching con test condizionale 'if'")
subject_value = ["pari", "50"]

match subject_value:
    case ["pari", valore] if int(valore) % 2 == 0:
        print(f"{valore} è un numero pari.")

    case ["dispari", valore] if int(valore) % 2 == 1:
        print(f"{valore} è un numero dispari.")

    case _:
        print("Errore nei dati.")


