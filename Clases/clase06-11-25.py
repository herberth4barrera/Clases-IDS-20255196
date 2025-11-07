#Este es yn docstring de modulo
#Vamos a crear varias funciones

#""""def saludar():
## nombre = input("Ingrese su nombre: ")
    #apellido = input("Ingrese su apellido: ")
    #nombre_completo = f"{nombre.title()} {apellido.title()}"
    #print(f"Hola {nombre_completo}")
    
#def saludar_con_param(nombre):
#   """Es una funcion que va a saludar"""
    
    #print(f"Hola {nombre}")
    
#saludar_con_param("Her")"""
#------------------------------------------

def dui_validacion(dui_a_validar):
    cantidad_condicion = 0
    if len(dui_a_validar) == 10:
        cantidad_condicion += 1
    cond2_cumplida = "-" in dui_a_validar
    if cond2_cumplida:
        cantidad_condicion += 1
        indice_guion = dui_a_validar.find("-")
        parte_despues_guion = dui_a_validar[indice_guion + 1:]
    if len(parte_despues_guion) == 1:
        cantidad_condicion += 1
    print(f"cumple {cantidad_condicion} condiciones")
    return cantidad_condicion