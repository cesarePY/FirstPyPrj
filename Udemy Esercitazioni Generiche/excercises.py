

#####################    CREATE A FUNCTION
def myFirstFunction (firstPrm):
    print(firstPrm)
    return {'a':10,'b':10,10:20}  #Return a dictionary
# END OF FUNCTION
#Try function
print (myFirstFunction(firstPrm=2303))



########## Try for and range
myList = []   #Create an empty list
#Range between 10 and 30, with offset 2.
for x in range(10,30,2):
    if x < 25:
        myList.append(x)

print (myList)

#List Comprehension example - creates a new list quadrati, by cycling trough existing myList and only adding squares of items > 19
quadrati  = [oggetto * oggetto for oggetto in myList if oggetto > 19]
print(quadrati)

#List Comprehension, creating a list containing items in range 10-30 which are even and smaller than 25
print('#List Comprehension')
resultList  = [oggetto for oggetto in range(10,30) if oggetto % 2 == 0 and oggetto <25]
print (resultList)




#Create a function returning the difference between two lists. Items of l1 not in l2
#l2 is optional with default [1,2,3,4,5]
def ListaDiff (l1, l2 = [1,2,3,4,5]):
    l = []
    for item in l1:
        if item not in l2:
            l.append(item)

    return l

#Call function ListaDiff, without specifying l2
print (ListaDiff((1,2,3,7)))

#Call function ListaDiff, specifying l2
print ( ListaDiff([1,2,3,7],[7,2]) )




#Scope and namespace
primo = 100  #Variable primo from Namespace Global (outside of any function and present in the basic program, used in the function
def myFunc(secondo):

   print('x+y= ',primo+secondo)

myFunc(20)



#### Global and Nonlocal: (shadowing) mechanism, object extvariable declared in function hides external object
print()
print('#### Global and Nonlocal: (shadowing) mechanism, object extvariable declared in function hides external object')
extvariable = 100
def myFuncGlob():
    extvariable = 20   #this operation creates a new object, whose scope is limited to this function, and assigns 20
    print('extvariable = ',extvariable)

# Print shows that ojbect extvariable has NOT been modified
myFuncGlob()
print('extvariable = ',extvariable)



print()
print('#### Global and Nonlocal:  keyword \'global\' allows to avoid \'variable hiding\' (shadowing) mechanism')
extvariable = 100
def myFuncGlob():
    global extvariable
    extvariable = 20   #this operation will change the value of external object extvariable, instead of declaring a new
                       # object whose scope is limited to this function, and assigne 20, modifying the external object
    print('extvariable = ',extvariable)

# Print shows that ojbect extvariable has been modified
myFuncGlob()
print('extvariable = ',extvariable)


#### Global and Nonlocal:  shows how keyword \'global\' work in a three level context (global, outer, inner)
print()
print('#### Global and Nonlocal:  shows how keyword \'global\' work in a three level context (global, outer, inner)')
extvariable1 = 11
extvariable2 = 21
print('global extvariable1 = ',extvariable1)
print('global extvariable2 = ',extvariable2)
def myOuterFunc():
    extvariable1 = 12
    extvariable2 = 22
    def myInnerFunc():
        nonlocal extvariable1
        extvariable1 = 13
        global extvariable2
        extvariable2 = 23
        print('       inner extvariable1 = ', extvariable1, ' #nonlocal causes modification to outer value')
        print('       inner extvariable2 = ', extvariable2, ' #global causes modification to global value, but not to outer')

    print('   outer extvariable1 = ', extvariable1)
    print('   outer extvariable2 = ', extvariable2)
    myInnerFunc()
    print('   outer extvariable1 = ', extvariable1)
    print('   outer extvariable2 = ', extvariable2)
# Print shows that ojbect extvariable has been modified

myOuterFunc()
print('global extvariable1 = ',extvariable1)
print('global extvariable2 = ',extvariable2)
