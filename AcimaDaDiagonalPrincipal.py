Variavel1 = input()

Matriz1 = []

for i in range(12):

    Matriz1.append([])

    for J in range(12):

        num = float(input())

        Matriz1[i].append(num)

if Variavel1 == "S":

    SomaDosValores = 0

    cont = 1

    for i in range(0, 11):
        for J in range(cont, 12):
            SomaDosValores += Matriz1[i][J]
        cont += 1
    print("%.1f" % SomaDosValores)

elif Variavel1 == "M":

    SomaDosValores = 0

    cont = 1

    cont2 = 0

    for i in range(0, 11):

        for J in range(cont, 12):
            SomaDosValores += Matriz1[i][J]
            cont2 += 1
        cont += 1

    MediaDosValores = SomaDosValores / cont2
    print("%.1f" % MediaDosValores)