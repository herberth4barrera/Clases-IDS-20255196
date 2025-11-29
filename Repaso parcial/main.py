from modulo_funciones import registrar_estudiante, inscribir_en_curso, generar_reporte

def menu_principal():
    while True:
        print("    SISTEMA ACADÉMICO BÁSICO:    ")
        print(" ")
        print("[1] Registrar estudiante")
        print("[2] Inscribir en curso")
        print("[3] Generar reportes")
        print("[4] Salir")
        opcion = input("Seleccione una opción: ").strip()
        try:
            if opcion == '1':
                registrar_estudiante()
            elif opcion == '2':
                inscribir_en_curso()
            elif opcion == '3':
                generar_reporte()
            elif opcion == '4':
                print("\nGracias por utilizar el Sistema Académico. ¡Hasta pronto!")
                break 
            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
        
        except Exception as e:
            print(f"Ocurrió un error inesperado en la ejecución: {e}")
if __name__ == "__main__":
    menu_principal()