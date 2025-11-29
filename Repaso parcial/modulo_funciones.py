from modulo_datos import LISTA_ESTUDIANTES, CATALOGO_CURSOS, LISTA_INSCRIPCIONES

def carnet_existe(carnet):
    for estudiante in LISTA_ESTUDIANTES:
        if estudiante['carnet'] == carnet:
            return True
    return False

def validar_carnet(mensaje):
    while True:
        try:
            carnet = input(mensaje).strip()
            
            if not (6 <= len(carnet) <= 10):
                print("El carnet debe tener entre 6 y 10 caracteres.")
                continue
            
            if carnet_existe(carnet):
                print("Este carnet ya existe. Solicite otro carnet.")
                continue
                
            return carnet
        except Exception:
            print("Entrada inválida. Intente de nuevo.")

def validar_nombre_o_apellido(campo):
    while True:
        try:
            valor = input(f"Ingrese {campo} (mínimo 2 caracteres): ").strip()
            
            if len(valor) < 2:
                print(f"El {campo} debe tener mínimo 2 caracteres. Solicite el campo nuevamente.")
                continue
                
            return valor
        except Exception:
            print("Entrada inválida. Intente de nuevo.")


def registrar_estudiante():
    print("\n REGISTRAR ESTUDIANTE ")
    try:
        carnet = validar_carnet("Ingrese Carnet (6-10 caracteres): ")
        nombre = validar_nombre_o_apellido("Nombre")
        apellido = validar_nombre_o_apellido("Apellido")
        nuevo_estudiante = {
            'carnet': carnet,
            'nombre': nombre,
            'apellido': apellido
        }
        LISTA_ESTUDIANTES.append(nuevo_estudiante)
        print("\nEstudiante registrado exitosamente.")
    except Exception as e:
        print(f"Error al registrar estudiante: {e}")

def inscribir_en_curso():
    print("\n INSCRIBIR EN CURSO ")
    while True:
        carnet = input("Ingrese el carnet del estudiante (o 'salir' para menú): ").strip().upper()
        if carnet == "SALIR":
            return
        if carnet_existe(carnet):
            break
        else:
            print("Carnet no encontrado.")
    print("\n Cursos Disponibles ")
    for codigo, descripcion in CATALOGO_CURSOS.items():
        print(f"[{codigo}] - {descripcion}")
    while True:
        codigo_curso = input("Ingrese el código del curso a inscribir: ").strip().upper()
        if codigo_curso not in CATALOGO_CURSOS:
            print("Código de curso no válido. Solicite nuevamente.")
            continue
        inscripcion_actual = (carnet, codigo_curso)
        if inscripcion_actual in LISTA_INSCRIPCIONES:
            print(f"El estudiante {carnet} ya tiene inscrito el curso {codigo_curso}.")
            return
        LISTA_INSCRIPCIONES.append(inscripcion_actual)
        print(f"\nInscripción registrada: {carnet} en {CATALOGO_CURSOS[codigo_curso]}.")
        break


def generar_reporte():
    if not LISTA_INSCRIPCIONES:
        print("\nNo hay inscripciones registradas para generar reportes.")
        return
    while True:
        print("\nSUBMENÚ DE REPORTES ")
        for codigo in CATALOGO_CURSOS.keys():
            print(f"[{codigo}] - Estudiantes inscritos en {CATALOGO_CURSOS[codigo]}")
        print("[SIN] - Estudiantes sin inscripción")
        print("[S] - Regresar al Menú Principal")
        opcion = input("Seleccione una opción de reporte: ").strip().upper()
        if opcion == "S":
            return
        elif opcion in CATALOGO_CURSOS.keys():
            curso_seleccionado = opcion
            carnets_en_curso = [carnet for carnet, curso in LISTA_INSCRIPCIONES if curso == curso_seleccionado]
            print(f"\nCARNETS INSCRITOS EN {CATALOGO_CURSOS[curso_seleccionado]} ({curso_seleccionado}) ")
            if not carnets_en_curso:
                print("No hay estudiantes inscritos en este curso.")
            else:
                for carnet in sorted(list(set(carnets_en_curso))):
                    print(f" * {carnet}")
        elif opcion == "SIN":
            carnets_inscritos = {carnet for carnet, in LISTA_INSCRIPCIONES}
            estudiantes_sin_curso = [
                estudiante for estudiante in LISTA_ESTUDIANTES 
                if estudiante['carnet'] not in carnets_inscritos
            ]
            print("\n ESTUDIANTES SIN INSCRIPCIÓN ")
            if not estudiantes_sin_curso:
                print("Todos los estudiantes registrados tienen al menos una inscripción.")
            else:
                for estudiante in estudiantes_sin_curso:
                    print(f" * {estudiante['carnet']} - {estudiante['nombre']} {estudiante['apellido']}")
        else:
            print("Opción de reporte no válida.")