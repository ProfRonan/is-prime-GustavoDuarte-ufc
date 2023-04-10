a = int(input())
b = 0
c = 1
while c < a+1:
    if a % c == 0:
        print(end='')
        b += 1
    else:
        print(end='')
    c = c + 1
if b == 2:
    print("Primo")
elif b != 2 and a > 0:
    print("Não primo")
elif a <= 0:
    print("Número inválido")



    