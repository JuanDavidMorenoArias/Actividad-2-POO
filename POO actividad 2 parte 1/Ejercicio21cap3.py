from math import sqrt
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))
perimetro = a+b+c
semiperimetro = (a+b+c)/2
print("perimetro:", perimetro )
print("Semiperimetro:", semiperimetro )
print("Area:", sqrt(semiperimetro*(semiperimetro-a)*(semiperimetro-b)*(semiperimetro-c)))
