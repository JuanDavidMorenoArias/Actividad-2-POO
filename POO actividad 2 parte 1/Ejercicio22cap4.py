EmpleadoNombre = input("Nombre: ")
SalarioPorHora = float(input("Salario Basico: "))
Horas = int(input("Horas Trabajadas al Mes: "))
print("Nombre:", EmpleadoNombre)
if SalarioPorHora*Horas > 450000:
    print("Salario Mensual:",SalarioPorHora*Horas)
