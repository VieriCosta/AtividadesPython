Varivel1 = int(input())

Variavel2 = input()
   

Matriz1 = []
for i in range(12):
    Matriz1.append([])

for i in range(12):

    for j in range(12):
        x = float(input())
        Matriz1[i].append(x)
        

if Variavel2 == 'S':

    SomaDosProdutos = 0

    for Values in range(12):
        SomaDosProdutos = SomaDosProdutos + Matriz1[Values][Varivel1]
    print(SomaDosProdutos)

if Variavel2 == 'M':

    med = 0

    SomaDosProdutos = 0

    for Values in range(12):

        SomaDosProdutos = SomaDosProdutos + Matriz1[Values][Varivel1]

    med= SomaDosProdutos/12

    print('{:.1f}'.format(med))