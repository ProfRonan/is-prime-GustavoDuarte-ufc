a = int(input())
if a > 0:
    b = 2
    while b == 2:
        a = int(input())
        b = 0
        for i in range(1, a+1):
            if a % i == 0:
                print(end='')
                b += 1
            else:
                print(end='')
    if b != 0:
        while b != 2:
            a = int(input())
            b = 0
            for i in range(1, a+1):
                if a % i == 0:
                    print(end='')
                    b += 1
                else:
                    print(end='')
elif a <= 0:
    while a <= 0:
        a = int(input())
        b = 0
        for i in range(1, a+1):
            if a % i == 0:
                print(end='')
                b += 1
            else:
                print(end='')
elif b != 2:
    if b != 2:
            while b != 2:
                a = int(input())
                b = 0
                for i in range(1, a+1):
                    if a % i == 0:
                        print(end='')
                        b += 1
                    else:
                        print(end='')


    