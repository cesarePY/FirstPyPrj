#Iteratore di un iterabile (lista)
print('\nCostruisco un iteratore it1, a partire da un\'oggetto iterabile, la lista myList')
print('Dimostro come è possibile restituirne gli elementi, uno dopo l\'altro, col metodo next()')
print('-----------  ------------------')
print('-----------  ------------------')

mylist = ["primo","secondo","terzo"]
it1 = iter(mylist)
print(next(it1))
print(next(it1))
print(next(it1))
#print(next(it1))

print('Utilizzando un costrutto "for" per traversare la lista, equivale implicitamente ad usare un iteratore su di essa:')
for e in mylist:
    print(e)



#Costruiamo un oggetto che è sia un'iterabile che un'iteratore
print('\n--- Costruisco un\'oggetto che è, sia iterabile, sia iteratore. ---')
print('--- Affinchè l\'oggetto sia iterabile, deve contenere un metodo __iter__ che restituisce un\'iteratore. ---')
print('--- Affinchè l\'oggetto sia un\'iteratore, deve contenere un metodo __next__ ---')
print('-----------  ------------------')
print('-----------  ------------------')
print('-----------  ------------------')
print('-----------  ------------------')
class MyIterator:
    def __iter__(self):  #Implemento il metodo __iter__ per rendere MyIterator un oggetto ITERABILE
        self.myattr = 2  #Setto a 2 il valore iniziale di un'attributo
        return self      # __iter__ deve ritornare un'oggetto ITERATORE, che permetterà di scorrere l'ITERABILE dal quale è stato originato

    def __next__(self): #Implemento il metodo __next__ per rendere MyIterator un oggetto che è anche un ITERATORE (sarà iteratore di se stesso)
        if self.myattr < 300:   #Fino a che myattr non raggiunge 300, esegue il seguente
            n = self.myattr     #Parcheggia valore attuale myattr
            self.myattr *= 2    #Raddoppia valore myattr
            return n            #Ritorna valore precedentemente parcheggiato.
        else:
            raise StopIteration #myattr è maggiore uguale a 300, ritorno un'eccezione per fermare l'iterazione




#Template esempio
print('\n-----------  ------------------')
print('-----------  ------------------')
print('-----------  ------------------')
print('-----------  ------------------')
print('-----------  ------------------')

