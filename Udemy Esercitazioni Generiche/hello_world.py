

a = 20
b = a
c = b * 1

print (id(a))
print (id(b))
print (id(c))
#print id(b)



myList = [10,20,30]
print (myList[1])
print (myList[-1])
myList[1] = 50
print(myList[:2])
print('lunghezza lista: '+str(len(myList)))
myList.insert(len(myList),60)
myList.append(70)
print(myList)  ### Stampa lista
print(20 in myList)  # Stampa risultato a domanda 0 è nella mia lista?




myList = [[1,2],[2,3],[6,7]]
print(myList[1][1])

inp = input("Inserisci un numero: ")
x = int(inp)
if x < 10:
    se = "Numero minore di 10"
    print (se)
else:
    se = "Numero MAGGIORE UGUALE di 10"
    print (se)


x = 0
while x < 3:
    print(x)
    x += 1
    break
else:
    print (str(x)+ ' <= last')


for x in range(1,10,2):
    print(x)