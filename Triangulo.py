variavel = input().split()

a, b, c = float(variavel[0]), float(variavel[1]), float(variavel[2])

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)
else:
    area = ((a + b) / 2) * c
    print("Area = %.1f" % area)