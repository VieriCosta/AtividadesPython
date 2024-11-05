Numeros = []
for i in range(10):
    value = int(input())
    if value <= 0:
        value = 1
        Numeros.insert(i,value)
    else:
        Numeros.insert(i,value)

for i in range(10):
    print('X[{0}] = {1}'.format(i,Numeros[i]))