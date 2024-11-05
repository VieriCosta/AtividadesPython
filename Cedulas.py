troco = int(input())
print(troco)

cem = troco // 100;

troco = troco - (cem *100);

cinquenta = troco // 50;

troco = troco - (cinquenta * 50);

vinte = troco // 20;

troco = troco - (vinte * 20);

dez = troco // 10;

troco = troco -(dez * 10);

cinco = troco // 5;

troco = troco - (cinco * 5);

dois = troco // 2;

troco = troco - (dois * 2);

print(cem ,"nota(s) de R$ 100,00")
print(cinquenta, "nota(s) de R$ 50,00")
print(vinte, "nota(s) de R$ 20,00")
print(dez, "nota(s) de R$ 10,00")
print(cinco, "nota(s) de R$ 5,00")
print(dois, "nota(s) de R$ 2,00")
print(troco, "nota(s) de R$ 1,00")