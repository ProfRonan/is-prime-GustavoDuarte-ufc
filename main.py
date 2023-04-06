a = int(input())
b = 0
for i in range(1, a+1):
    if a % i == 0:
        print(end='')
        b += 1
    else:
        print(end='')
if b == 2:
    print("Primo")
elif b != 2 and a > 0:
    print("Não primo")
elif a <= 0:
    print("Número inválido")


    