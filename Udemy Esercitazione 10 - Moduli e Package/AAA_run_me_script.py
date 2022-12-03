#Moduli
import modulo1 as m1, modulo2 as m2 #Importa moduli e associa nome per comodità
m1.myFunc(10)   #Funzione myFunc è un attributo del modulo
m2.myFunc(20)   #Stesso nome funzione di cui sopra, ma da modulo diverso

#importa solo una classe dal modulo
from modulo3 import MyClass
myCl = MyClass("ciao") #In questo modo Si accede all'oggetto importato senza usare la dot notation modulo3.MyClass

#Packages
import subPackage.submodulo1 as sm1   #Importa da package
import subPackage.subSubPackage.subsubmodulo1 as ssm1  #Importa da package dentro altro package