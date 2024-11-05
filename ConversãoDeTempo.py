segundos = int(input())
horas = segundos // 60**2
segundos = segundos - horas * 60**2
minutos = segundos // 60
segundos = segundos - minutos*60
print("{}:{}:{}".format(horas,minutos,segundos))