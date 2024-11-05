x = int(input())

for n in range(1, x + 1):
    y = n**2
    if (n % 2) == 0:
        print("{}^2 = {}".format(n, y))