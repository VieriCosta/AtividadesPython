Variavel1 = int(input())
Variavel2 = int(input())

M = Variavel1 if Variavel1 > Variavel2 else Variavel2
M2 = Variavel2 if Variavel2 < Variavel1 else Variavel1
M2+=1
soma = 0

while (M2 < M):
    if(M2 % 2 != 0):
        soma+=M2
    M2+=1
print(soma)