calificacion1 = float(input())
calificacion2 = float(input())
calificacion3 = float(input())
calificacion4 = float(input())
calificacion5 = float(input())
calificacion6 = float(input())

suma_calificaciones = calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5 + calificacion6

numero_materias = 6
promedio = suma_calificaciones / numero_materias

if promedio > 9.5:
    print("Gana Premio :)")
else:
    print("No Gana Premio :(")