Numero1, Numero2 = map(int, input().split())



i = 0
Numeros = []
Variavel = 0



while i < Numero2 - Numero1:
    for j in range(1, Numero1 + 1):
        Numeros.append(i + 1)
        div = Numeros[Variavel]
        Numeros[Variavel] = str(Numeros[Variavel])
        Variavel += 1
        i += 1


    Variavel = 0
    Numeros = " ".join(Numeros)
    print(Numeros)
    Numeros = []



Sobra = Numero2 % Numero1



if Sobra == 0:
    for x in range(Numero2 - Numero1, Numero2):
        Numeros.append(x + 1)
        Numeros[Variavel] = str(Numeros[Variavel])
        Variavel += 1
    Numeros = " ".join(Numeros)
    print(Numeros)

if Sobra != 0:
    for x in range(div, Numero2):
        Numeros.append(x + 1)
        Numeros[Variavel] = str(Numeros[Variavel])
        Variavel += 1
    Numeros = " ".join(Numeros)
    print(Numeros)