from math import sqrt
LadoDelTriangulo = float(input("Lado del triangulo: "))
#supongo que el algoritmo me pide que imprima los valores#
ValorDeLaAltura = sqrt(LadoDelTriangulo**2 - (LadoDelTriangulo/2)**2)
print("Perimetro:",LadoDelTriangulo * 3 )
print("Altura:", ValorDeLaAltura)
print("Area:",(LadoDelTriangulo*ValorDeLaAltura)/2)