print('-----------  Mostra type della classe  ------------------')
class MyClass(object):
    pass
# mostra che la classe è MyClass è un'istanza della classe 'type'
# per contro, 'type' è un tipo predefinito di Python, è una classe che ha come istanze tutte le classi che andremo a definire nei nostri programmi
print (type(MyClass))

print('\n-----------  Mostra attributi della classe e delle sue istanze e la loro differenza dopo averne settato uno a 90 ------------------')
class MyClass(object):
    myAttr = 10    #Attributo di classe, e non di istanza
print ('MyClass.myAttr: ',MyClass.myAttr)  #mostrerà 10, sempre lo stesso valore
m1 = MyClass()  #istanzia classe
m2 = MyClass()  #istanzia classe

#mostra il valore attributo nelle due istanze.... uguale a quello della classe originaria.
print('m1.myAttr = ', m1.myAttr)
print('m2.myAttr = ', m2.myAttr)
print ()
m1.myAttr = 90   #Modificherà solo l'attributo di questa istanza, lasciando invariato quello di classe e di tutte le altre istanze della classe
print ('MyClass.myAttr: ',MyClass.myAttr)
print('m1.myAttr = ', m1.myAttr)
print('m2.myAttr = ', m2.myAttr)



#Metodi di istanza
print('\n-----------  Metodi: il metodo di istanza MyMethod  ------------------')
print('-----------  i metodi di istanza ricevono tutti il parametro self  ------------------')
print('-----------  questo riceve anche una stringa che poi stampa a video dopo l\'ID della istanza (self) --------')
class MyClass():
    def myMethod(self, message):   #metodo creato con parametro che passa l'istanza di classe stessa
        print(id(self))   #stampa l'identificativo dell'istanza della classe.
        print(message)

m1 = MyClass()  #istanzia classe
m2 = MyClass()  #istanzia classe
m1.myMethod('hey')    # self non si passa, è implicito, e l'istruzione corrisponde a MyClass.myMethod(m1)
m2.myMethod('ciao')   # come sopra


#Costruttore di istanza __init___
print('\n-----------  Costruttore d\'istanza __init__  ------------------')
print('-----------  i costruttori di istanza ricevono tutti il parametro self  ------------------')
print('-----------  questo riceve anche una stringa che usa per inizializzare l\'attributo message --------')
print('-----------  printmessage() poi lo stampa  --------')
class MyClass():
    def __init__(self, message):   #Costruttore __init__ della classe
        self.message = message     #In questo caso init

    def printMessage(self):
        print(self.message)

m1 = MyClass('ciao')  # Quando si instanzia questa classe  è necessario fornire parametro message, che verrà usato dal costruttore per inizializzare l'attributo d'istanza
m1.printMessage()



#Metodi di classe
print('\n-----------  Metodi di classe @classmethod  ------------------')
print('-----------  i metodi di classe ricevono come parametro l\'oggetto classe cls   ------------------')
print('-----------  cls autoreferenzia la classe stessa, e attraverso di esso è possibile accedere agli attributi ----')
print('-----------  qui il @classmethod istanze() stampa l\'attributo counter, usato come contatore delle istanze  ---')
class MyClass():
    counter = 0
    def __init__(self):
        MyClass.counter+=1   #il costruttore dell'istanza incrementa l'attributo counter della classe madre MyClass, che quindi rappresenterà il numero di istanze create dalla classe MyClass

    @classmethod   #decoratore @classmethod dichiara che questo metodo è un metodo di classe, e quindi non di istanza, e agisce sulla classe
    def istanze(cls):   #un metodo di classe riceve di default il parametro (oggetto) cls (invece di self)
        print('Istanze di MyClass: ',cls.counter)  #stampa il numero di istanze create dalla classe MyClass

m1 = MyClass()
MyClass.istanze()  #mi aspetto 1
m2 = MyClass()
MyClass.istanze()  #mi aspetto 2
m3 = MyClass()
MyClass.istanze()  #mi aspetto 3


#Metodi statici
print('\n-----------  Metodi statici @staticmethod  ------------------')
print('-----------  i metodi statici non ricevoo come argomento implicito ne self ne cls   ------------------')
print('-----------  metodi statici non hanno accesso agli attributi di istanza o classe -------')
print('-----------  possono essere usati funzioni semplici, aggregate in un contenitore classe  -------')

class MyClass():
    @staticmethod
    def somma(a,b):
        return (a+b)
s = MyClass.somma(10,5)
print ('Metodo statico somma, risultato: ',s)


#Inheritance
print('\n----------- Inheritance ------------------')
print('----------- un istanza di una classe è istanza anche delle super classi della classe di cui è istanza -----')
print('----------- per cui ne eredita attributi e metodi  -----')
class BClass:
    def setMessage(self, message):
        self.message = message
    def printMessage(self):
        print(self.message)

class AClass(BClass):    #Create AClass as a sub-class of BClass
    pass

m1 = AClass()   #istanzia m1 da AClass
print('m1 è istanza di AClass? ',isinstance(m1,AClass)) #m1 is obviously instance of AClass
print('m1 è istanza di BClass? ',isinstance(m1,BClass)) #but it's also instance of AClass's super-class BClass
m1.setMessage('messaggio ereditato da BClass')          #as a result m1 inherits methods from BClass
m1.printMessage()                                       #both setmessage('xxx') and printmessage() are usable on m1




#Override
print('\n----------- Override ------------------')
print('----------- Quando si deriva una sottoclasse da una superclass è possibile ridefinire nella sottoclasse -----')
print('----------- gli attributi ereditati dalla superclass e così cambiarli -----')
print('----------- In questo caso printMessage originario di BClass, viene ridefinito nella sua sottoclass AClass ---')
print('----------- in modo che stampi un prefisso \"AClass: \" prima del messaggio definito in istanziazione ---')
class BClass:
    def setMessage(self, message):
        self.message = message
    def printMessage(self):
        print(self.message)

class AClass(BClass):    #Create AClass as a sub-class of BClass
    def printMessage(self):
        print("AClass: " + self.message)

m1 = AClass()   #istanzia m1 da AClass
m1.setMessage('messaggio settato runtime')          #as a result m1 inherits methods from BClass
m1.printMessage()                                       #both setmessage('xxx') and printmessage() are usable on m1




#Override
print('\n----------- Funzione Super ------------------')
print('----------- Utilizzata per invocare un qualunque method di una superclass dall\'interno di una subclass ----')
print('----------- In questo caso è utilizzata per risolvere il problema che il constructor __init__  -----')
print('----------- della subclass, previene l\'esecuzione del constructor della sua superclass ---')
print('----------- se quest\'ultimo non viene invocato esplicitamente attraverso la funzione super() ---')
print('----------- Questo è utile quando non vogliamo fare un override totale di un methodo di una superclass ---')
class BClass:
    def __init__(self, message):        #define superclass constructor
        self.message = message          #to set message attribute with value provided at instance creation time
    def printMessage(self):
        print(self.message)

class AClass(BClass):    #Create AClass as a sub-class of BClass
    def __init__(self, message, valore): #constructor of subclass AClass overrides superclass' BClass constructor, but also prevents
        super().__init__(message) #the superclass' constructor from running, so we need to explicitly invoke it via the function super()
        self.valore = valore  #and then execute subclass constructor co
    def printValore(self):
        print(self.valore)

m1 = AClass('messaggio settato runtime',10) #instantiate m1 from subclass AClass, with constructor receiving two parameters: message,valore
m1.printMessage()                           #Prints message, provided on subclass instance creation to superclass constructor
m1.printValore()                            #Prints valore, provided on subclass instance creation time to subclass constructor





#Properties - leggere e scrivere le proprietà di una classe
print('\n----------- Legge e scrivere le proprietà ------------------')
print('----------- modalità semplice che non nasconce il contenuto dell\'attributo interno priv_attr ------------------')
print('----------- Peculiarità: prende in input getter e setter methods e li associa ad una associa ------------------')
print('----------- ad una proprietà attraverso il costruttore property  ------------------')
class MyClass():
    def __init__(self, my_attr):   #costruttore della classe, riceve un parametro in entrata (oltre all'oggetto self)
        self.priv_attr = my_attr
    def get_attr(self):             #getter method, metodo per ottenere il valore dell'attributo interno priv_attr
        return self.priv_attr
    def set_attr(self, attr):        #setter method, metodo per modificare il valore dell'attributo interno priv_attr con parametro ricevuto
        self.priv_attr = attr
    attr = property (get_attr, set_attr)    #il costruttore property ritorna una proprietà, ricevendo i due metodi di cui sopra, e la associa al nome attr

obj = MyClass('python')
print("Attributo dopo istanziazione classe: " + obj.attr)     #utilizzo di del getter method della proprietà attr
obj.attr  = 'prova'                       #utilizzo del setter method della proprietà attr
print("Attributo dopo averlo cambiato: " + obj.attr)


#Variable Mangling e Property decorators
print('\n----------- Esempio che illustra due concetti: attribute mangling(storpiamento) e property decorators ------------------')
print('-----------    Name Mangling: tramite il prefisso __ si mimetizza un attributo e impedisce che venga invocato ------------')
print('-----------       attraverso il proprio nome dal di fuori della classe ------------------')
print('-----------    Property decorators: ------------------')
print('-----------       @property: definisce metodo getter method ------------------')
print('-----------       @attr.setter: definisce setter method ------------------')
print('-----------      Equivalenti al costruttore property dell\'esempio precedente------------------')

class MyClass():
    def __init__(self, my_attr):   #costruttore della classe, riceve un parametro in entrata (oltre all'oggetto self)
        self.__priv_attr = my_attr    #associa parametro all'attributo mimetizzato (prefisso __)

    @property
    def attr(self):             #getter method, metodo per ottenere il valore dell'attributo interno priv_attr
        return self.__priv_attr

    @attr.setter
    def attr(self, attr):        #setter method, metodo per modificare il valore dell'attributo interno priv_attr con parametro ricevuto
        self.__priv_attr = attr

obj = MyClass('python')
print("Attributo dopo istanziazione classe: " + obj.attr)     #utilizzo di del getter method della proprietà attr
obj.attr  = 'prova'                       #utilizzo del setter method della proprietà attr
print("Attributo dopo averlo cambiato: " + obj.attr)





#Ereditarietà multipla e MRO
print('\n--- Ereditarietà multipla e MRO (Method Resolution Order) per risolvere conflitti d\'ereditarietà')
print('--- AClass deriva da due classi BClass e CClass, che hanno attributi con nomi uguali')
print('--- Python utilizza un MRO Method Resolution Order per decidere da quale classe l\'attributo verrà ereditato')
print('--- In ordine di priorita:')
print('--- 1) La classe stessa-')
print('--- 2) Le classi dalle quali deriva (e loro superclassi), in ordine di apparizione nella dichiarazione della classe derivata')
print('--- quindi in questo caso BCLass e poi CClass e, trovandola in BClass, esegue quella')
class BClass:
    b = 10 #s
    y = "b"
    def bFunc(self):
        print("eseguo bFunc: sono in BClass")
    def xFunc(self):
        print("eseguo xFunc: sono in BClass")


class CClass:
    c = 20 #s
    y = "c"  #attributo y con stesso nome di BClass
    def cFunc(self):
        print("eseguo cFunc: sono in CClass")
    def xFunc(self):  #metodo con stesso nome di BClass
        print("eseguo xFunc: sono in CClass")

class AClass(BClass, CClass):  #Dichiaro AClass come derivante da BClass e CClass
    pass

a = AClass() #Istanzio una AClass
print("Contenuto di y =",a.y)  #Stampo il contenuto dell'attributo y, che viene da BClass per via dell'MRO
a.bFunc()
a.cFunc()
a.xFunc()   #xFunc() esiste sia in BClass che in CCLass, grazie all'MRO, viene scelto il metodo da BClass
#--- fine Ereditarietà multipla e MRO




#Template esempio
print('\n--- Differenza tra costruttore e inizializzatore  ------------------')
print('---in realtà __init__ non è un costruttore ma un\'inizializzatore dell\'istanza di una classe ')
print('--- il vero costrutture dell\'istanza di una classe si chiama __new__ e ritorna l\'istanza appena costruita')
print('--- che viene, poi, ricevuta in input da __init__ come parametro self ')
print('--- in questo esempio ridefiniamo ___new__ e ___init___ e ne manteniamo le funzioni originali con un trucco super()')
print('--- NB: ___new___ deve ritornare l\'istanza di classe costruita a ___init___, altrimenti ___init___ non verrà eseguito')
class MyClass():
    def __new__(cls, message):
        istanza = super().__new__(cls)  #Se si vuole ridefinire __new__ occorre invocare lo stesso costruttore dalla super classe
        print("Stampo da ___new___: ", message)
        return istanza  #in modo da ottenere da esso la costruzione dell'istanza di classe, per poi ritornarla a __init__, altrimenti ___init__ non verrà eseguito
    def __init__(self, message):
        self.message = message
        print("Stampo da ___init___: ", self.message)
mc = MyClass(">>>Passa il messaggio da ___new___ a ___init___<<<")
#--- FINE - Differenza tra costruttore e inizializzatore  ------------------



#Template esempio
print('\n-----------  ------------------')
print('-----------  ------------------')
print('-----------  ------------------')
print('-----------  ------------------')
print('-----------  ------------------')




