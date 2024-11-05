VMatriz = []

Variavel1 = input()

for i in range(12):

    VMatriz.append([])

    for F in range(12):

        VariavelX = float(input())
        VMatriz[i].append(VariavelX)

if Variavel1 == "S":

    SomaDosProdutos = 0

    Continuacao = 11

    for i in range(11, 0, -1):

        for F in range(0, Continuacao):

            SomaDosProdutos += VMatriz[i][F]
        Continuacao -= 1

    print("%.1f" % SomaDosProdutos)

elif Variavel1 == "M":

    SomaDosProdutos = 0
    Continuacao = 11
    Continuacao2 = 0
    for i in range(11, 0, -1):

        for F in range(0, Continuacao):

            SomaDosProdutos += VMatriz[i][F]
            Continuacao2 += 1
        Continuacao -= 1

    media = SomaDosProdutos / (Continuacao2)

    print("%.1f" % media)