numeros = int(input())

for i in range(0,numeros):
    numeros2 = int(input())
    j = 1
    s = 0
    while j < numeros2:
        if numeros2 % j == 0:
            s = s + j
           
        j = j + 1
       
    if s == numeros2:
        print('{} eh perfeito'.format(numeros2))
    else:
        print('{} nao eh perfeito'.format(numeros2))