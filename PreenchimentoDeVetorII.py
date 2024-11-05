Variavel = int(input())
Variavel2 = [] 
for i in range(1000):
    j = 0
    while j < Variavel:
        Variavel2.append(j)
        j = j + 1
    print('N[{0}] = {1}'.format(i,Variavel2[i]))