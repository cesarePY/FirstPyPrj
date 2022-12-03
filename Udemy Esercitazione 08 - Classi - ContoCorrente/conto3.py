# Esercitazione Conto Corrente
print('\n----------- Esercitazione Conto Corrente ------------------')
print('----------- Terza versione con superclass Conto contenente attributi "nome" e "conto" ------------------')
print('----------- e subclass ContoCorrente attributo __saldo nascosto e @property getter e setter "saldo" ------------------')
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

ccn1 = ContoCorrente("Cesare Mastromatteo", "1000" , 100)
ccn1.descrizione()



