a = []
for b in range(5):
    b = int(input())
    a.append(int(b))

p = 0
i = 0
po = 0
neg = 0

for variavel in range(5):
    if a[variavel] %2 == 0:
        p += 1
    if a[variavel] %2 == 1:
        i += 1
    if a[variavel] > 0:
        po += 1
    if a[variavel] < 0:
        neg += 1

print(p, "valor(es) par(es)")
print(i, "valor(es) impar(es)")
print(po, "valor(es) positivo(s)")
print(neg, "valor(es) negativo(s)")