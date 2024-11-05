Variavel = []
for i in range(10):
    if i == 0:
        valores = int(input())
        X = valores
        Variavel.insert(i,valores)
    else:
        X = X * 2
        Variavel.insert(i,X)

for i in range(10):
    print('N[{0}] = {1}'.format(i,Variavel[i]))