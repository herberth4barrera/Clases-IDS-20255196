def registrar_estudiante(lista_estudiantes):
    nombre= input("Ingrese el nombre del estudiante: ")
    nuevo_id = len(lista_estudiantes) + 1
    codigo = f"S{nuevo_id:03d}"
    lista_estudiantes.append({"nombre": nombre, "codigo": codigo})
    print(f"Estudiante {nombre} registrado con el código {codigo}.")

def mostrar_estudiantes(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes registrados en el sistema.")
        return
    print("\n--- Lista de Estudiantes ---")
    print(f"{'Carnet':<10} | {'Nombre'}")
    print("-" * 40)
    for estudiante in lista_estudiantes:
        print(f"{estudiante['codigo']:<10} | {estudiante['nombre']}")
    print("-" * 40)