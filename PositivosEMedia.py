Variavel = 0

Variavel2 = 0.0

for i in range(1,7):
    n = float(input())
    if(n>0):
        Variavel2 = Variavel2 + n
        Variavel=Variavel+1
average = Variavel2/Variavel
print(f"{Variavel} valores positivos")
print(f"{average:0.1f}")