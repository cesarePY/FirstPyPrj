#Introdotto con Python 3.8, PEP 572, il Walrus operator ":=" permette di anticipare lo svolgimento di un espressione per poterne utilizzare il
#risultato immediatamente.

#Al fine di dimostrare l'utilità del Walrus operator, definiamo una funzione semplicissima "somma" da usare più in basso
def somma(a,b) -> int:
    return a + b
print(F"La somma è: {somma(5,3)}")

#Nel test condizionale  "x := somma(5, 8)" viene svolto immediatamente, grazie all'operatore ":=" (al posto di "="), e
#il suo risultato, 8, viene poi confrontato con 6:
if x := somma(5,3) > 6:
    print ("Somma è maggiore di 6")

#Altro esempio di come il Walrus operator permette di anticipare il calcolo di un'espressione, e ritornarlo per usarlo
#in runtime. Qui sotto ad ogni iterazione del ciclo while, ad x viene assegnato, grazie al Walrus operator, la
#lunghezza della lista mylist in quel preciso momento..
#e nel body del ciclo viene stampato lo stato del check booleano "x è diverso da zero"
# contestualmente viene rimosso "mylist.pop()" l'ultimo elemento della lista, riducendola di un element
#prima della prossima iterazione...
#Senza il Walrus operator non sarebbe stato possibile valutare la lunghezza della lista così elegantemente.
mylist = [1,2,3,4,5]
while x:= len(mylist) != 0:
    print(x, mylist.pop())


#Il Walrus operator non può essere utilizzato al primo livello come se fosse "x = somma(5,3)"
#ma solo come parte di un espressione, per esempio all'interno di una condizione da verificare
# infatti "x := somma(5,3)" darebbe un errore di sintassi
#se proprio volessimo utlizzare, anche se ha poco senso, il Walrus operator in un contesto così semplice
#basterebbe racchiudere l'espressione in parentesi tonde per farla risultare al secondo livello
(y := somma(5,3))


#Infine il Walrus operator serve anche nel passaggio dei parametri a una funzione, per
#esempio per conservare il valore di default di un parametro e usare tale valore
#anche nel caso in cui il parametro fosse fornito nella chiamata
#Nell'esempio qui sotto, il default "Susanna" viene messo da parte in "n", poi
#a runtime viene passata la stringa "Alessandro" come parametro, ma grazie al walrus operator
#noi, volendo, possiamo utilizzare il valore che avrebbe avuto di default.

def saluta(nome = (n := "Susanna")):
    print(F"Ciao '{nome}'")
    print(F"Ciao '{n.upper()}'")

#Faccio override del default, quindi nome e n differiscono
saluta("Alessandro")
print("-")
#Non specifico il parametro, e quindi "nome" e "n" coincidono
saluta()
