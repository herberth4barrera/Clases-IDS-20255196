#Condicionales

#} if(if, else, elif), 
# bucle }finito(for) - coleccion (string, lista, tipla, dictionario)
# infinito

"""palabra = "Hola"
print(len(palabra))
lista = [10, 11, 12, 13, 14]
print(len(lista))
dias = ["Lunes", "Martes", "Miercoles", 
        "Jueves", "Viernes", "Sabado", "Domingo"]
print(len(dias))

for i in palabra: 
    print("Hola profe")
    
for i in lista: 
    print(i)
    
for i in dias[3]:
    print(i)"""
    

valores = [[1,3,6], [2,7,4], [6,5,9], [1,10,20]]
mayores = []

for i in valores:
    for x in i:
        if x > 6:
            mayores.append(x)
            
print(mayores)
