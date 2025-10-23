#Realizamos los ejercicios del parcial, para un mayor entendimiento de los conceptos

#Ejercicio 1

"""num1 = input()
num2 = input()

son_iguales = num1 == num2
print(son_iguales)"""


#Listasprint

datos = [1,2,"tres", ["lunes","martes","miercoles"]]
#print(datos[2][1])
print(datos[-1][-1][3])

numero = ["uno", "dos", "tres"]
print(numero)
numeros = numero + ["cuatro", "cinco", "seis"]
print (numeros)
print(len(numeros))

numeros[2] = "trois"
print(numeros)

numeros.append(input("Ingrese un numero: Escriba el siguiente numero: "))
print(numeros)
numeros.insert(2, input("Einender nummer:"))
print(numeros)