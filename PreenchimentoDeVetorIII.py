Variavel = float(input())

Lista = []

for i in range(100):

    if i == 0:

        Variavel2 = Variavel
        Lista.insert(i,Variavel2)
        
    else:

        Variavel2 = Variavel2 / 2
        Lista.insert(i,Variavel2) 

for i in range(100):
    print('N[{0}] = {1:.4f}'.format(i,Lista[i]))