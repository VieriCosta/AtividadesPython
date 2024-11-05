a , b , c= input().split()

a = float(a)
b = float(b)
c = float(c)

areaTriangulo = a * c / 2
areaCirculo = 3.14159 * (c**2)
areaTrapezio = (a + b) * c / 2
areaQuadrado = b**2
areaRetangulo = a * b

print("TRIANGULO: %.3f" %areaTriangulo)
print("CIRCULO: %.3f" %areaCirculo)
print("TRAPEZIO: %.3f" %areaTrapezio)
print("QUADRADO: %.3f" %areaQuadrado)
print("RETANGULO: %.3f" %areaRetangulo)