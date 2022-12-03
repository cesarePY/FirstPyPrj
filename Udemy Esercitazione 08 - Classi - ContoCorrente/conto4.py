 # Esercitazione Conto Corrente
print('\n----------- Esercitazione Conto Corrente ------------------')
print('----------- Quarta versione con classe non istanziabile contenente un metodo statico bonifico------------------')
print('----------- che accetta come parametri conto sorgente, conto destinazione e importo bonifico ------------------')
print('-----------  ------------------')
print('-----------  ------------------')
class Conto:
    def __init__(self, nome, conto):  # costruttore della classe, riceve due parametri (oltre a self)
        self.nome = nome     #e inizializza i propri due attributi
        self.conto = conto

class ContoCorrente(Conto):   #Classe ContoCorrente deriva da superclass Conto
    def __init__(self, nome, conto, importo):  # costruttore della classe, riceve tre parametri in entrata (oltre all'oggetto self)
        super().__init__(nome,conto)   #passa i primi due parametri al costruttore della sua superclass
        self.__saldo = importo      #e utilizza il terzo per inizializzare il saldo

    def preleva(self, importo):
        self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += importo

    def descrizione(self):
        print(self.nome, self.conto, self.saldo)

    @property
    def saldo(self):  # getter method, metodo per ottenere il valore dell'attributo interno __saldo
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):       #setter method, metodo per settare il nuovo saldo, modificando l'attributo interno __saldo con l'importo ricevuto
        self.preleva(self.__saldo)  #azzera conto
        self.deposita(importo)      #setta nuovo saldo  (tutto questo è ai fini dell'esercizio)

class GestoreContiCorrenti:   #Classe non istanziabile (no costruttore __init__)
    @staticmethod      #Metodo statico che effettua bonifico da un conto all'altro
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)

ccn1 = ContoCorrente("Cesare Mastromatteo", "1000" , 10000)
ccn2 = ContoCorrente("Giuseppe Rossi", "1001" , 2000)
ccn1.descrizione()
ccn2.descrizione()

GestoreContiCorrenti.bonifico(ccn1, ccn2, 975)  #Effettua bonifico da a
print("-- dopo bonifico --")
ccn1.descrizione()
ccn2.descrizione()



