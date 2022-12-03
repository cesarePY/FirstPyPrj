# Esercitazione Conto Corrente
print('\n----------- Esercitazione Conto Corrente ------------------')
print('----------- Prima versione classe con attributi visibili all\'esterno ------------------')
print('----------- Metodo preleva senza controlli ------------------')
print('----------- Metodo deposita ------------------')
print('----------- Metodo descrizione per saldo ------------------')
class ContoCorrente:
    def __init__(self, nome, conto, importo):  # costruttore della classe, riceve un parametro in entrata (oltre all'oggetto self)
        self.nome = nome
        self.conto = conto
        self.saldo = importo

    def preleva(self, importo):
        self.saldo -= importo

    def deposita(self, importo):
        self.saldo += importo

    def descrizione(self):
        print(self.nome,  self.conto , self.saldo)


ccn1 = ContoCorrente("Cesare Mastromatteo", "1000" , 100)
ccn2 = ContoCorrente("Luigi Rossi" , "1001", 2300)
ccn1.descrizione()
ccn2.descrizione()
print("----")

ccn1.preleva(10)
ccn1.descrizione()
print("----")

ccn2.deposita(111)
ccn2.descrizione()
