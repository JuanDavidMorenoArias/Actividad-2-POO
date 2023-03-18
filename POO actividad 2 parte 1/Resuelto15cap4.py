A = float(input("Peso de A: "))
B = float(input("Peso de B: "))
C = float(input("Peso de C: "))
D = float(input("Peso de D: "))
if  B == C == D: 
    if A == min(A,B,C,D):
        print("A es la de menor peso")  
    else:
        print("A es la de mayor peso")
elif  A == C == D: 
    if B == min(A,B,C,D):
        print("B es la de menor peso")  
    else:
        print("B es la de mayor peso")
elif  A == B == D: 
    if C == min(A,B,C,D):
        print("C es la de menor peso")  
    else:
        print("C es la de mayor peso")
elif  A == B == C: 
    if D == min(A,B,C,D):
        print("D es la de menor peso")  
    else:
        print("D es la de mayor peso")
