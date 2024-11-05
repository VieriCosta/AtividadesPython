Variavel = int(input())

Lista = []

a = list(map(int,input().split()))

for i in range (Variavel):

    Lista.insert(i,a[i])
print("Menor valor: %d" %(min(Lista)))

for i in range(Variavel): 

    if Lista[i]==min(Lista):
        pos=i
print("Posicao: %d" %pos)