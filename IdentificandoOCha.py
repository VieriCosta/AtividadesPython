T = int(input())  # Tipo de chá correto
respostas = list(map(int, input().split()))  # Respostas dos competidores

# Contar o número de acertos
acertos = sum(1 for resposta in respostas if resposta == T)

# Exibir o número de acertos
print(acertos)
