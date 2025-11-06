"""surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):
    print(position, surname)
    """


#------------------------------------------

"""people = ['Nick', 'Rick', 'Roger', 'Syd']
ages = [23,24,23,21]

for person, age in zip(people, ages):
    print(person,age)"""
    
#------------------------------------------

#Ejercicio de clase


"""menu = input()
print(menu)

clientes = []
codigo_cliente = input()
nombre = input()
correo = input()
telefono = input()

clientes.append([codigo_cliente,nombre,correo,telefono])

productos = []
codigo_producto = input()
nombre = input()
categoria = input()
precio = []

productos.append([codigo_producto,nombre,categoria,precio])

pedidos = [codigo_cliente,codigo_producto]"""



#------------------------------------------

CLIENTES = []

PRODUCTOS = [
    {'codigo': 'P001', 'nombre': 'Espresso', 'categoria': 'Bebidas', 'precio': 2.00},
    {'codigo': 'P002', 'nombre': 'Capuccino', 'categoria': 'Bebidas', 'precio': 3.00},
    {'codigo': 'P003', 'nombre': 'Muffin de Arándanos', 'categoria': 'Postres', 'precio': 2.50},
    {'codigo': 'P004', 'nombre': 'Sandwich de Pavo', 'categoria': 'Comidas', 'precio': 4.50},
]

PEDIDOS = []
ID_PEDIDO_COUNTER = 1 


while True:
    print("BIENVENIDO a ESEN Brew - Sistema de Gestión ")
    print("1. Mostrar productos (Menú)")           
    print("2. Agregar producto al menú")             
    print("3. Mostrar categorías disponibles")     
    print("4. Registrar nuevo cliente")             
    print("5. Mostrar clientes")                    
    print("6. Registrar pedido")                    
    print("7. Mostrar pedidos del día")             
    print("8. Salir")                             
    
    opcion = input("Ingrese su opción (1-8): ").strip()
    
    if opcion == '8':
        print("Gracias por usar el sistema de ESEN Brew. ¡Hasta pronto!")
        break
    elif opcion == '1':
        if not PRODUCTOS:
            print("El menú está vacío.")
        else:
            print("\n--- MENÚ DE PRODUCTOS ---")
            print(f"{'Código':<10} | {'Nombre':<30} | {'Categoría':<15} | {'Precio':<10}")
            print("-" * 65)
            for producto in PRODUCTOS:
                
                print(f"{producto['codigo']:<10} | {producto['nombre']:<30} | {producto['categoria']:<15} | ${producto['precio']:<9.2f}")

    elif opcion == '2':
        print("\n--- AGREGAR NUEVO PRODUCTO ---")
        nuevo_id = len(PRODUCTOS) + 1
        codigo_producto = f"P{nuevo_id:03d}" 
        nombre = input("Ingrese el nombre del producto: ").strip()
        categoria = input("Ingrese la categoría (Ej: Bebidas, Postres, Comidas): ").strip()
        
        precio = -1.0 
        precio_str = input("Ingrese el precio del producto: ")
        if '.' in precio_str or ',' in precio_str:
            if precio_str.replace('.', '', 1).replace(',', '', 1).isdigit():
                precio = float(precio_str)
        elif precio_str.isdigit():
            precio = float(precio_str)
        
        if not all([nombre, categoria]) or precio <= 0:
            print("Error: Todos los campos son obligatorios y el precio debe ser un número positivo.")
        else:
            nuevo_producto = {
                'codigo': codigo_producto,
                'nombre': nombre,
                'categoria': categoria, 
                'precio': precio 
            }
            PRODUCTOS.append(nuevo_producto) 
            print(f"Producto '{nombre}' agregado exitosamente. Código: {codigo_producto}")

    elif opcion == '3':
        categorias = set()
        for p in PRODUCTOS:
            categorias.add(p['categoria'])
            
        if not categorias:
            print("No hay categorías disponibles.")
        else:
            print("\n--- CATEGORÍAS DISPONIBLES ---")
            for cat in sorted(list(categorias)):
                print(f"* {cat}")
                
    elif opcion == '4':
        print("\n--- REGISTRAR NUEVO CLIENTE ---")
        
        nuevo_id = len(CLIENTES) + 1
        codigo_cliente = f"C{nuevo_id:03d}" 
        nombre = input("Ingrese el nombre del cliente: ").strip()
        correo = input("Ingrese el correo del cliente: ").strip()
        telefono = input("Ingrese el teléfono del cliente: ").strip()
        
        if not all([nombre, correo, telefono]):
            print("Error: Todos los campos (nombre, correo, teléfono) son obligatorios.")
        else:
            nuevo_cliente = {
                'codigo': codigo_cliente, 
                'nombre': nombre, 
                'correo': correo, 
                'telefono': telefono 
            }
            CLIENTES.append(nuevo_cliente) 
            print(f"Cliente registrado exitosamente. Código: {codigo_cliente}")

    elif opcion == '5':
        if not CLIENTES:
            print("No hay clientes registrados aún.")
        else:
            print("\n--- LISTA DE CLIENTES ---")
            print(f"{'Código':<10} | {'Nombre':<25} | {'Correo':<30} | {'Teléfono':<15}")
            print("-" * 85)
            for cliente in CLIENTES:
                print(f"{cliente['codigo']:<10} | {cliente['nombre']:<25} | {cliente['correo']:<30} | {cliente['telefono']:<15}")

    elif opcion == '6':
        print("\n--- REGISTRAR NUEVO PEDIDO ---")
        
        codigo_cliente = input("Ingrese el código del cliente (Ej: C001): ").strip().upper()
        cliente_encontrado = None
        for c in CLIENTES:
            if c['codigo'] == codigo_cliente:
                cliente_encontrado = c
                break
        
        if not cliente_encontrado:
            print(f"Error: Cliente con código {codigo_cliente} no encontrado.")
            continue 
            
        print(f"Cliente encontrado: {cliente_encontrado['nombre']}")
        
        productos_seleccionados = []
        productos_codigos = []
        total_pedido = 0.0
        
        while True:
            if not PRODUCTOS:
                print("El menú está vacío, no se pueden hacer pedidos.")
                break
            print("\n--- MENÚ DE PRODUCTOS PARA SELECCIÓN ---")
            print(f"{'Código':<10} | {'Nombre':<30} | {'Precio':<10}")
            print("-" * 55)
            for producto in PRODUCTOS:
                print(f"{producto['codigo']:<10} | {producto['nombre']:<30} | ${producto['precio']:<9.2f}")
            
            print("\nPara terminar el pedido, ingrese 'FIN'.")
            cod_producto = input("Ingrese el código del producto a agregar (Ej: P001): ").strip().upper()
            
            if cod_producto == 'FIN':
                break
            
            producto_encontrado = None
            for p in PRODUCTOS:
                if p['codigo'] == cod_producto:
                    producto_encontrado = p
                    break
            
            if producto_encontrado:
                productos_codigos.append(cod_producto) 
                productos_seleccionados.append(producto_encontrado) 
                total_pedido += producto_encontrado['precio']
                print(f"Producto '{producto_encontrado['nombre']}' agregado. Total provisional: ${total_pedido:.2f}")
            else:
                print(f"Error: Producto con código {cod_producto} no encontrado en el menú.")

        if not productos_codigos:
            print("Pedido cancelado: No se seleccionaron productos.")
            continue
            
        nuevo_pedido = {
            'id_pedido': ID_PEDIDO_COUNTER,
            'codigo_cliente': codigo_cliente, 
            'productos': productos_codigos, 
            'total': round(total_pedido, 2) 
        }
        
        PEDIDOS.append(nuevo_pedido)
        print(f"\n--- RESUMEN DEL PEDIDO #{ID_PEDIDO_COUNTER} ---")
        print(f"Cliente: {cliente_encontrado['nombre']} ({codigo_cliente})")
        print(f"Total de items: {len(productos_codigos)}")
        print(f"TOTAL DEL PEDIDO: ${total_pedido:.2f}")
        
        ID_PEDIDO_COUNTER += 1 
        
    elif opcion == '7':
        if not PEDIDOS:
            print("No hay pedidos registrados aún.")