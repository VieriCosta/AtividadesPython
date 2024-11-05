Variavel = 999
while Variavel !=0:
    Variavel=int(input())
    Soma1 = 0
    X = 1
    if Variavel != 0:
        while X <= 5:
           
            if Variavel % 2 == 0:
                Soma1 = Soma1 + Variavel
                Variavel = Variavel + 1
                X = X + 1
            else:
                Variavel = Variavel + 1
           
           
        print(Soma1)
    elif Variavel ==0:
        break