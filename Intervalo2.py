n = int(input())

dentros = 0
foras = 0


for x in range(1, n + 1):

    x = int(input())

    if n >= 10 and x <= 20:
        dentros = dentros + 1
    else:
        foras = foras + 1

print("%d in" % dentros)
print("%d out" % foras)