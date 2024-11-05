Matriz1 = []

Variavel1 = input()

for V1 in range(12):

    Matriz1.append([])

    for Y in range(12):

        x = float(input())

        Matriz1[V1].append(x)

SomaDosPontos = 0

V1 = 0

V2 = 0

for i in range(11, 0, -1):

    V1 += 1

    for j in range(V1, 12):

        SomaDosPontos += Matriz1[i][j]

        V2 += 1

if Variavel1 == "S":

    print("%.1f" % SomaDosPontos)

elif Variavel1 == "M":

    media = SomaDosPontos / V2
    
    print("%.1f" % media)