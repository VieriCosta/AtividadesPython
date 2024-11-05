Variavel = int(input())

for i in range(Variavel):
    V1,V2,V3,V4 = input().split()
    V1 = int(V1)
    V2 = int(V2)
    V3 = float(V3)
    V4 = float(V4)
    
    A = 0
    while(V1 <= V2):
        VV1 = int((V1*(V3/100)))
        VV2 = int((V2*(V4/100)))
        A += 1
        V1 += VV1
        V2 += VV2
        
        if(A > 100):
            break

    if(A>100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos." %A)