agente = "encargado" 
platillo = [] 
precios = [] 

nombre_ingresado = ""

while nombre_ingresado != agente:
    nombre_ingresado = input("Ingresar nombre del agente: ") 
    if nombre_ingresado != agente:
        print("Agente no registrado")

opcion = 0 
salir = 4

while opcion != salir:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Creación de platillos.") 
    print("2. Consulta de platillos y precios.") 
    print("3. Colocar un pedido.") 
    print("4. Salir.") 
    print("----------------------")
    
    opcion = int(input("Ingresar opción: "))
    
    if opcion == 1:
        nombre_platillo = input("Ingrese nombre del platillo a crear: ") 
        precio_platillo = float(input("Ingrese precio del platillo a crear: "))
        
        platillo.append(nombre_platillo)
        precios.append(precio_platillo)
        print(nombre_platillo + " agregado con éxito.")

    elif opcion == 2:
        if len(platillo) == 0:
            print("Actualmente no hay platillos ingresados") 
        else:
            print("\n--- PLATILLOS Y PRECIOS ---")
            i = 0
            while i < len(platillo):
                print(platillo[i] + ": $" + str(precios[i]))
                i = i + 1
            print("---------------------------")
            
    elif opcion == 3:
        orden_nombre = input("Indique nombre del platillo para su orden:").lower()
        
        encontrado = 0 
        indice_encontrado = -1
        
        i = 0
        while i < len(platillo):
            if orden_nombre == platillo[i].lower():
                encontrado = 1
                indice_encontrado = i
                break
            i = i + 1
            
        if encontrado == 1:
            nombre = platillo[indice_encontrado]
            precio = precios[indice_encontrado]
            print("Usted ha elegido " + nombre + " con un precio de $" + str(precio))
        else:
            print("Platillo no encontrado. Regresando al menú anterior.")
            
    elif opcion == salir:
        print("Saliendo de la aplicación. ¡Hasta pronto!")
    else:
        print("Opción no válida. Por favor, elija un número del 1 al 4.")