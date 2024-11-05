Variavel = 0
Variavel2 = 0
while True:
    idade = int(input())
    if    idade<0:
        break
    else:
        Variavel +=    idade
        Variavel2 += 1
Variavel = Variavel/Variavel2
print("%.2f"%Variavel)