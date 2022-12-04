#annotazioni di tipo per parametri e valore di ritorno di funzioni
def myFunc(x: int, s: str = "python") -> str:
    print(x)
    return s

res = myFunc(10, "hey")
print(F'res = "{res}"')
print(F'tipo di res = "{type(res)}"')
#stampa le annotazioni di tipo della funzione
print(F'myFunc.__annotations__ = "{myFunc.__annotations__}"')

#annotazione di tipo per variabile
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