Variavel = 0
Variavel2 = 1
for j in range(1,40,2):
    Variavel = float(Variavel + j / Variavel2)
    Variavel2 = Variavel2 * 2
print('{:.2f}'.format(Variavel))