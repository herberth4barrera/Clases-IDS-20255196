def registrar_libro(lista_libros):
    nombre = input("Ingrese el nombre del libro: ")
    autor = input("Ingrese el autor del libro: ")
    nuevo_id = len(lista_libros) + 1
    codigo = f"L{nuevo_id:03d}"
    lista_libros.append({"nombre": nombre, "autor": autor, "codigo": codigo, "disponible": True})
    print(f"Libro {nombre} registrado con el código {codigo}.")

def mostrar_libros(lista_libros):
    if not lista_libros:
        print("No hay libros registrados en el sistema.")
        return
    print("\n--- Catálogo de Libros ---")
    print(f"{'Código':<10} | {'Título':<30} | {'Autor':<25} | {'Estado'}")
    print("-" * 75)
    for libro in lista_libros:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"{libro['codigo']:<10} | {libro['nombre']:<30} | {libro['autor']:<25} | {estado}")
    print("-" * 75)