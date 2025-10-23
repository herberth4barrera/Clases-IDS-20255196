monto = float(input("Ingrese un monto: "))
tipo = input("tipo(local/internacional): ")

impuesto = 0

if tipo.lower() == "local":
    if monto >100:
        impuesto = 0.07
    else:
        if monto >75: 
            impuesto = 0.05
        else:
            impuesto = 0 
elif tipo.lower() == "internacional":
    if monto >100:
        impuesto = 0.12
    elif monto >75:
            impuesto = 0.09
    else:
            impuesto = 0    
else:
    print("Tipo de impuesto no reconocido")
print(f"El tipo {tipo} con monto {monto:,.2f}")
print(f"paga un impuesto de {impuesto*monto:.2f}")
        