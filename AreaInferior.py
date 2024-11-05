X = []
Variavel = input()

for i in range(12):
    X.append([])

    for j in range(12):
        num = float(input())
        X[i].append(num)

Soma1 = 0
Baixo1 = 5
Cima1 = 7
cont1 = 0

for i in range(7, 12):
    for j in range(Baixo1, Cima1):
        Soma1 += X[i][j]
        cont1 += 1
    Baixo1 -= 1
    Cima1 += 1

media = Soma1 / cont1

if Variavel == "S":
    print("%.1f" % Soma1)
else:
    print("%.1f" % media)