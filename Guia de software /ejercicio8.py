A = int(input())

personas_que_ingresan = 0

i = 0

while i < A:
    edad = int(input())
    if edad >= 15:
        personas_que_ingresan = personas_que_ingresan + 1
    i = i + 1

print(personas_que_ingresan)