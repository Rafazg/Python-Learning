myList = ["Angel", 43, 667767250, ]
myList2 = [22, True, 'list', [1,2]]

print(type(myList))



#acessar uma lista dentro de outra lista
print(myList2[1:2])

#modificar um item da lista
myList[0] = 'Carlos'

#adicionar funções dentro de uma list
def myFunc(number, numberTwo):
   return number + numberTwo

myList.append(myFunc)

result = myList[3](2, 3)
print(result)



