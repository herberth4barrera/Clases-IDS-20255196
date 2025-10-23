#Trabajando con listas
"""nombre = "Antonio"
repetido = nombre.lower().count("a")
print(repetido)"""

nombres = ["Ana", "Antonio", "Ana", "Jose"]
"""repetidos_a = 0
print(nombres.count("Maria"))
repetidos_a = repetidos_a + nombres[0].lower().count("a")
repetidos_a = repetidos_a + nombres[1].lower().count("a")
repetidos_a = repetidos_a + nombres[2].lower().count("a")
repetidos_a = repetidos_a + nombres[3].lower().count("a")
print(repetidos_a)"""

#print(nombres.index("Ana", 1))

#int(nombres.index("Ana", nombres.index("Ana")+1))

"""nombres = ["Antonio", "Maria", "Jose", "Carlos"]
nombres.append("Aby")
print(nombres)
nombres.insert(int(input("Posicion: ")))
print(nombres)
nombres[int(input("Posicion: "))] = input("Nuevo nombre: ")
print(nombres)
posicion = int(input("Posicion: "))
nombres[posicion] = input("Nombre Nuevo sustituir: ")
print(nombres)
nombres.remove("Carlos")
print(nombres)
nombre_borrado = nombres.pop(3)
print(f"Nombre borrado: {nombre_borrado}")"""

#HERRAMIENTAS DE CONTROL DE FLUJO

numero = 6

captura = int(input("Adivina el numero (un intento): "))

if captura == numero:
    print("Le acertaste!")
else:
    print("Ese numero no era")
print("Puedes seguir jugando")

#Ejemplo de notas

nota = float(input("Ingrese la nota: "))

if nota > 8:
    print("Aprobado")
    if nota == 10:
        print("Excelente")
    else:
        print("Buen trabajo")