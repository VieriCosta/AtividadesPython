DIAD = input().split()
HORAD = input().split()
DIAF = input().split()
HORAF = input().split()


di, df = int(DIAD[1]), int(DIAF[1])
hi, mi, si = int(HORAD[0]), int(HORAD[2]), int(HORAD[4])
hf, mf, sf = int(HORAF[0]), int(HORAF[2]), int(HORAF[4])  


MS = 60
HS = MS * 60
DS = HS * 24
i = si + mi*MS + hi*HS + di*DS
f = sf + mf*MS + hf*HS + df*DS
if i < f:
    tempo = f - i
    dias = int(tempo/DS)
    tempo = tempo%DS
    horas = int(tempo/HS)
    tempo = tempo%HS
    minutos = int(tempo/MS)
    tempo = tempo%MS
    segundos = tempo
    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))