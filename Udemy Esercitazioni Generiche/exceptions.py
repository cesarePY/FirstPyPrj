#try: except:
print('\nEsempio che illustra un\'eccezione catturata con try: except: ')
print('Causa una divisione per zero')
print('E la intercetta, scrivendo \'ERRORE!\' a video')
print('')
print('-----------  INIZIO -----------')
def f(x,y):  #Definisce una funzione che ritorna l
    return x // y;

try:
    c = f(5, 0)
    print ('c = ' + str(c))  #Mostra risultato
except:
    print('ERRORE!')
print('-----------  FINE -------------')



#try: except(list, of, exceptiontypes):
print('\nEsempio che illustra un\'eccezione catturata con try: except: ')
print('Causa una divisione per zero')
print('Ma in questo caso specifica quali tipo di eccezioni intercettare')
print('e cioè solo quelle di tipo ZeroDivisionError e ValueError')
print('-----------  INIZIO -----------')
def f(x,y):  #Definisce una funzione che ritorna l
    return x // y;

try:
    c = f(5, 0)
    print ('c = ' + str(c))  #Mostra risultato
except (ZeroDivisionError, ValueError):   #Cattura eccezioni di tipo ZeroDivisionError, ValueError
    print("Divisione per zero!")
print('-----------  FINE -------------')




#try: except as:
print('\nEsempio che illustra un\'eccezione catturata con try: except as: ')
print('Causa una divisione per zero')
print('Ma in questo caso specifica come tipo di eccezione da catturare ZeroDivisionError')
print('ne cattura il contenuto con la parola chiave \"as\" e la assegna ad una variabile')
print('il cui contenuto può essere poi ispezionato ed utilizzato ai fini della gestione dell\'eccezione')
print('-----------  INIZIO -----------')
def f(x,y):  #Definisce una funzione che ritorna l
    return x // y;

try:
    c = f(4, 0)
    print ('c = ' + str(c))  #Mostra risultato
except ZeroDivisionError as myException:   #Cattura eccezioni di tipo ZeroDivisionError e la assegna a variabile di tipo object
    print(myException.args)   #Mostra list attributi dell'eccezione
print('-----------  FINE -------------')



#try: except: finally:
print('\nEsempio che illustra un\'eccezione catturata con try: except: finally: ')
print('Causa una divisione per zero')
print('La cattura con except ZeroDivisionError:')
print('E con finally: definisce un pezzo di codice che viene eseguito SEMPRE,')
print('sia che l\'eccezione venga catturata o meno, sia che non avvenga affatto')
print('-----------  INIZIO -----------')
def f(x,y):  #Definisce una funzione che ritorna l
    return x // y;

try:
    c = f(4, 0)
    print ('c = ' + str(c))  #Mostra risultato
except ZeroDivisionError:   #Cattura eccezioni di tipo ZeroDivisionError
    print("Divisione per zero!")
finally:   #Questo blocco di codice viene eseguito SEMPRE, a prescindere dal fatto che l'eccezione avvenga o venga gestito
    print("finally: Questo lo eseguo sempre!!!")
print('-----------  FINE -------------')


#try: except: else:
print('\nEsempio che illustra un\'eccezione catturata con try: except: else: ')
print('Definisce except per catturare eccezione di tipo ZeroDivisionError:')
print('E aggiunge dopo tutte le except la clausola else: che viene eseguita SOLO SE non si verifica alcuna eccezione')
print('-----------  INIZIO -----------')
def f(x,y):  #Definisce una funzione che ritorna l
    return x // y;

try:
    c = f(4, 2)
    print ('c = ' + str(c))  #Mostra risultato
except ZeroDivisionError:   #Cattura eccezioni di tipo ZeroDivisionError
    print("Divisione per zero!")
else:   #Questo blocco di codice viene eseguito solo se il blocco all'interno di try: non solleva alcuna eccezione
    print('else: Tutto bene, il risultato della divisione è: '+str(c))
print('-----------  FINE -------------')





#Eccezioni: lo statement assert
print('\nEsempio di statement assert che solleva eccezione di tipo AssertionError')
print('nel caso la la condizione non fosse verificata ')
print('-----------  INIZIO -----------')
x = 10
try:
    assert x == 5, "valori diversi"    # 10 !=5 => eccezione sollevata
except AssertionError as exx:  #gestisce eccezione
    print(exx)
print('-----------  FINE -------------')




#Eccezioni: lo statement raise
print('\nEsempio che illustra un\'eccezione catturata con try: except: ')
print('Causa una divisione per zero')
print('La gestisce e poi la risolleva per lasciare che venga ulteriormente gestita altrove nel programma')
print('!! Decommentare raise per testarlo !!')
print('-----------  INIZIO -----------')
def f(x,y):  #Definisce una funzione che ritorna l
    return x // y;
try:
    c = f(5, 0)
    print ('c = ' + str(c))  #Mostra risultato
except (ZeroDivisionError, ValueError):   #Cattura eccezioni di tipo ZeroDivisionError, ValueError
    print("Divisione per zero!")
   # raise    #DECOMMENTARE PER TESTARE - Risolleva eccezione per continuare a gestirla altrove
print('-----------  FINE -------------')





exit()
#Template esempio
print('\n-----------  ------------------')
print('-----------  ------------------')
print('-----------  ------------------')
print('-----------  ------------------')
print('-----------  INIZIO -----------')
print('-----------  FINE -------------')
