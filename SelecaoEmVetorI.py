lista = []


for i in range(100):

    Variavel = float(input())

    lista.append(Variavel)

    if Variavel <= 10.0:

        print('A[{}] = {}'.format(i,Variavel))