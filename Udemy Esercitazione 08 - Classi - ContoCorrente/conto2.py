# Esercitazione Conto Corrente
print('\n----------- Esercitazione Conto Corrente ------------------')
print('----------- Seconda versione classe con  ------------------')
print('----------- attributo __saldo nascosto e @property getter e setter "saldo" ------------------')
print('-----------  ------------------')
print('-----------  ------------------')
class ContoCorrente:
    def __init__(self, nome, conto, importo):  # costruttore della classe, riceve un parametro in entrata (oltre all'oggetto self)
        self.nome = nome
        self.conto = conto
        self.__saldo = importo

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
print ("Saldo>" , ccn1.saldo)
ccn1.deposita(222)
print ("Saldo>" , ccn1.saldo)
ccn1.saldo = 11001
print ("Saldo>" , ccn1.saldo)


