Variavel1 = input()

SomaDosPontos = 0

Conti = 0

X = 11

Quantidade = 0

NaoE = Conti

entra = X

for i in range(144):

    numero1 = float(input())

    if entra > 0:

        entra -= 1

        SomaDosPontos += numero1

        Quantidade += 1

        continue

    if NaoE > 0:

        NaoE -= 1

        continue

    if NaoE + entra == 0:

        Conti += 1

        X -= 1

        NaoE = Conti

        entra = X


if Variavel1 == "S":

    print("%.1f" % SomaDosPontos)

elif Variavel1 == "M":

    print("%.1f" % (SomaDosPontos / float(Quantidade)))