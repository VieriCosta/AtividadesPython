a = []
for b in range(5):
    b = int(input())
    a.append(int(b))

i = 0 
for c in range(5):
    if a[c] %2 == 0:
        i += 1

print(i, "valores pares")