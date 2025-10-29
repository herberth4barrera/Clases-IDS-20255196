#Voy a iniciar mi variable en True

ejecucion = True

while ejecucion:
    opcion = input("Estamos ejecctando el menu? Y/N:")
    if opcion.lower() == "n":
        ejecucion = False
    elif opcion.lower() == "y":
        print("La opcion elegida no es valida")
        
print("Gracias por usar nuestro sistema")

#Ejecicio 2
alumnos = 0
lista_alumnos = []

alumno = input("Digite nombre" )
lista_alumnos.append(alumno)
alumno = input("Digite nombre" )
lista_alumnos.append(alumno)
alumno = input("Digite nombre" )
lista_alumnos.append(alumno)

print(alumnos)