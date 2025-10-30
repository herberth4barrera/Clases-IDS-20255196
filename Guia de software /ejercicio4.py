entrada_n = input()
N = int(entrada_n)

contador_siete = 0
contador_cinco = 0

i = 0

while i < N:
    entrada_numero = input()
    numero_actual = int(entrada_numero)
    
    if numero_actual == 7:
        contador_siete = contador_siete + 1
    elif numero_actual == 5:
        contador_cinco = contador_cinco + 1
    i = i + 1

print(contador_siete, contador_cinco)