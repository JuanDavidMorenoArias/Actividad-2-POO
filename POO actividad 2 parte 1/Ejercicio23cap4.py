import math
A = float(input("Inserte A: "))
B = float(input("Inserte B: "))
C = float(input("Inserte C: "))

if A != 0:
    dis = B**2 - 4*A*C
    raiz = math.sqrt(abs(dis))
    print("Soluciones")
    print("x =",(-B + raiz)/(2 * A))
    print("x =",(-B - raiz)/(2 * A))


