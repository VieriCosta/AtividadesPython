Variavel = int(input())
for i in range(0,Variavel):
    a = input().split()
    x,y = a
    y = int(y)
    x = int(x)
    soma = 0
    j = 1
    while j <= y:
        if x % 2 != 0:
            soma = soma + x
           
            x = x + 1
            j = j + 1
        if x % 2 == 0:
            x = x + 1
    print(soma)