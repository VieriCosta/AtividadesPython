valor = input()
valor = int(valor)

ano = valor // 365
valor = valor - (ano *365)
mes = valor // 30
valor = valor - (mes *30)
dias = valor

print(ano, "ano(s)")
print(mes, "mes(es)")
print(dias, "dia(s)")