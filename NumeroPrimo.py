numeros = int(input())

for i in range(0,numeros):
    numeros2 = int(input())
    s = 0
    j=1
    while j <= numeros2:
        if numeros2 % j == 0:
            s = s + 1
        j = j + 1
    if s > 2:
        print('{} nao eh primo'.format(numeros2))
    else:
        print('{} eh primo'.format(numeros2))