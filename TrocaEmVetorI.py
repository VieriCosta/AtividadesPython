Lista = [] 

for i in range(20):

    Variavel=int(input())

    Lista.append(Variavel)

V = Lista[::-1]

for j in range(20):

    print('N[{}] = {}'.format(j, V [j] ))