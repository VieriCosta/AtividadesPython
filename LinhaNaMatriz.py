Matriz1 = []

S = 0.0

I = int(input())

Operacao1 = input()

for i in range(12):
  Matriz2 = []
  for j in range(12):
    variavel = float(input())
    Matriz2.append(variavel)
  Matriz1.append(Matriz2)

for a in range(12):
  for b in range(12):
    if a == I:
      S+=Matriz1[a][b]

if Operacao1 == "S":      
  print("%.1f"%S)      
elif Operacao1 == "M":
  print(S/12)