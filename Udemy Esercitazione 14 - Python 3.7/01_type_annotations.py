#annotazioni di tipo per parametri e valore di ritorno di funzioni
#E' possibile specificare il tipo dei parametri di input e del valore di ritorno

def myFunc(x: int, s: str = "python") -> str:
    print(x)
    return s

#Nell'esempio qui sotto, abbiamo anche sovrascritto il default per la stringa "s"
res = myFunc(10, "hey")
print(F'res = "{res}"')
#mostra il tipo del valore ritornato dalla funzione "myFunc"
print(F'tipo di res = "{type(res)}"')
#stampa le annotazioni di tipo della funzione, prendendole da un dizionario
#"__annotations__" che viene creato automaticamente alla definizione della funzione
print(F'myFunc.__annotations__ = "{myFunc.__annotations__}"')

#annotazione di tipo per variabile, è ora possibile specificare il tipo della
#variabile quando la initializza.
a: int = "hey"
print(F'a = "{a}"')
#stampa tutte le annotazioni di tipo del modulo stesso
print(F'__annotations__ = "{__annotations__}"')


class MyClass:
    #Le annotazioni di tipo sono opzionali, servono a segnalare ad analizzatori del codice che
    #queste variabili saranno utilizzate, e inizializzate nel costruttore della classe
    nome: str
    cognome: str
    def __init__(self, receivedNome, receivedCognome):
        self.nome = receivedNome
        self.cognome = receivedCognome

print ("##################")
mc = MyClass(receivedNome= "Mario", receivedCognome= "Rossi")
print(mc)
print(f'mc.nome = "{mc.nome}"')
print(f'mc.cognome = "{mc.cognome}"')