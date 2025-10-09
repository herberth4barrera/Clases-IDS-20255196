###Ejercicios sobre tuplas

tupla1 = (1,12,255,1289,60000)
lista1 = [1,12,255,1289,60000]    #La lista es mutable
print(len(tupla1))
print(tupla1[3:])


tupla1[-1] = 3
print(tupla1)      #La tupla es inmutable

lista1[-1] = 3

print(lista1)

lista1.index