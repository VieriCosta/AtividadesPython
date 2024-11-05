ListaV=[0,1]

Variavel1 = 0

Variavel2 = 1

for i in range(60):

    Variavel3 = Variavel2 + Variavel1

    ListaV.append(Variavel3)

    Variavel1 = Variavel2

    Variavel2 = Variavel3

T = int(input())

for i in range(T):

    N=int(input())

    print('Fib(%d) = %d' %(N, ListaV[N]))