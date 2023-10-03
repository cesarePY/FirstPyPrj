#Introdotti con Python 3.8, PEP 570, i "positional-only parameters" mettono un limite alla possibilità di passare
#parametri in ordine sparso, in maniera non posizionale, attraverso "keywords arguments"

#La seguente funzione permette di fornire tutti gli argomenti in maniera posizionale, come "keyword arguments"
def somma(a, b, c):
    return a + b + c

print(F"Somma: '{somma(c=20, a= 1, b=11)}'")


#Definendo nel modo seguente somma2(), con il divisore "/", il parametro "a" sarà positional-only,
# "a" dovrà quindi essere passato per primo e senza la notazione "a= xxxx"
#  mentre b e c continueranno ad essere passabili in ordine sparso, come "keyword arguments"
# quindi un'espressione "somma2(a=10, c=20, b=11)" non verrà accettata, mentre "somma2(10, c=20, b=11)" sì
def somma2(a, /, b, c):
    return a + b + c
print(F"Somma2: '{somma2(10, c=20, b=11)}'")



