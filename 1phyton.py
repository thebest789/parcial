
n=int(input("ingrese el numero n"))
m=int(input("ingrese el numero m"))
n,m =sorted([n,m])
suma = sum(x for x in range(n,m+1))

print(suma)