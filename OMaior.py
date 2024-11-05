a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

AB = (a+b+abs(a-b))/2
AB = (c+AB+abs(AB-c))/2

print ("%d eh o maior" %AB)