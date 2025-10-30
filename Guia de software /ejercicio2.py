entrada = input()
S = int(entrada)
par_posterior = 0

if (S % 2) == 0:
    par_posterior = S + 2
else:
    par_posterior = S + 1

impar_anterior = 0

if (S % 2) == 0:
    impar_anterior = S - 1
else:
    impar_anterior = S - 2

print(par_posterior)
print(impar_anterior)