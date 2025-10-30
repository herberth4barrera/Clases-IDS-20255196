N = int(input())
P = list(map(int, input().split(" ")))
Pa = int(P[0])
Pb = int(P[1])
Pc = int(P[2])
combos = []
for elemento in range(N):
    A = input().upper()
    combos.append(A)
daño = []
x = 0
for i in combos:
    A = (combos[x].count("A")*Pa)+(combos[x].count("B")*Pb)+(combos[x].count("C")*Pc)
    daño.append(A)
    x +=1 
y = 0
for i in daño:
    print(daño[y])
    y+=1