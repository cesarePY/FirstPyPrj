#importa decoratore "dataclass" da modulo "dataclasses"
from dataclasses import dataclass
#Scopo principale delle data classes è quello di costruire classi che rappresentano tipi di dato e i loro comportamenti
#Decoratore @dataclass permette a python di inferire la presenza di oggetti di tipo Field
#e permette la creazione dietro le quinte di 4 metodi speciali, utili quando si vuole rappresentate un tipo di dato
# init = indica se creare il costruttore __init__ automaticamente
# repr = indica se creare automaticamente il metodo __repr__
# order = indica se creare automaticament il metodo di confronto di minore o maggiore
# frozen = indica se impedire la modifica dei valori dei Field dopo l'inizializzazione
@dataclass(init= True, repr= True, order= True, frozen= False)
class MyClass:
    #Annotazione di tipo permettono fornire il tipo a questi Field
    # @dataclass aggiunge automaticamente, dietro le quinte, un costruttore che prende in input i Field dichiarati
    # __init__(self, nome: str, cognome: str) -> None:
    #ed anche i seguenti metodi
    # __repr__  metodo che rappresenta contenuto di un'istanza attraverso le sue proprietà (Field)
    # __eq__    ( == )
    # __ne__    ( != )
    nome: str
    cognome: str

#il comando qui sotto è possibile grazie a @dataclass(init = True)
mc = MyClass("Giulio","Verne")
#Visualizza l'istanza di classe, rappresentandola con i contenuti dei campi (Field) grazie al fatto che esiste __repr__
#@dataclass(repr = True)
print(f'mc            = "{mc}"')
mc2 = MyClass("Mario","Rossi")
print(f'mc2           = "{mc2}"')
#Il comando qui sotto "{mc < mc2}" è permesso grazie a @dataclass(order = True)
print(f'mc < mc2      = "{mc < mc2}"')

#Il comando qui sotto è possibile grazie a @dataclass(frozen = False)
mc2.nome = "Ciccio"
print(f'mc2.nome      = "{mc2.nome}"')

