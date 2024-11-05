variavel = float(input())

if 0<= variavel <= 25:
    print("Intervalo [0,25]")
if 25 < variavel <= 50:
    print("Intervalo (25,50]")
if 50 < variavel <= 75:
    print("Intervalo (25,50]")
if 75 < variavel <= 100:
    print("Intervalo (75,100]")
if  variavel >100 or variavel<0:
    print("Fora de intervalo")