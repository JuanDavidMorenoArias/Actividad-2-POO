Numero = input("Numero de inscripcion: ")
Nombre = input("Nombres: ")
Patrimonio = float(input("Patrimonio(sin comas ni comillas): "))
Estrato = int(input("Estrato Social: "))
PagoDeMatricula = 50000
if Patrimonio > 2000000 and Estrato > 3:
    PagoDeMatricula += Patrimonio*(3/100)
print("Numero:",Numero)  
print("Nombre:",Nombre)    
print("Pago :",int(PagoDeMatricula))      
    