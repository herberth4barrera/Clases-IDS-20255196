def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):
    carnet_estudiante = input("Ingrese el carnet del estudiante: ")
    estudiante_encontrado = None
    for estudiante in lista_estudiantes:
        if estudiante["codigo"] == carnet_estudiante:
            estudiante_encontrado = estudiante
            break
    if not estudiante_encontrado:
        print("Error: Estudiante no encontrado.")
        return 
    codigo_libro = input("Ingrese el código del libro: ")
    libro_encontrado = None
    for libro in lista_libros:
        if libro["codigo"] == codigo_libro:
            libro_encontrado = libro
            break
    if not libro_encontrado:
        print("Error: Libro no encontrado.")
        return
        
    if not libro_encontrado["disponible"]:
        print("Error: El libro no está disponible para préstamo.")
        return
    fecha_prestamo = input("Ingrese la fecha del préstamo: ")
    lista_prestamos.append({"carnet_estudiante": carnet_estudiante, "codigo_libro": codigo_libro, "fecha": fecha_prestamo})
    libro_encontrado["disponible"] = False
    print("Préstamo registrado exitosamente.")

def mostrar_prestamos(lista_prestamos):
    if not lista_prestamos:
        print("No hay préstamos registrados en el sistema.")
        return
    print("\n--- Préstamos Registrados ---")
    print(f"{'Carnet Estudiante':<20} | {'Código Libro':<15} | {'Fecha Préstamo'}")
    print("-" * 60)
    for prestamo in lista_prestamos:
        print(f"{prestamo['carnet_estudiante']:<20} | {prestamo['codigo_libro']:<15} | {prestamo['fecha']}")
    print("-" * 60)