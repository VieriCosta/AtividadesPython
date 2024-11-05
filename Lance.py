Lanches = input().split()

codigo , valor = Lanches

if codigo == '1':
    print('Total: R$ {:.2f}'.format(4.00*float(valor)))
if codigo == '2':
    print('Total: R$ {:.2f}'.format(4.50*float(valor)))
if codigo == '3':
    print('Total: R$ {:.2f}'.format(5.00*float(valor)))
if codigo == '4':
    print('Total: R$ {:.2f}'.format(2.00*float(valor)))
if codigo == '5':
 print('Total: R$ {:.2f}'.format(1.50*float(valor)))