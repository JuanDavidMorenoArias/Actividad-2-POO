ventasdep1 = int(input("ventas del departamento 1: "))
salariodep1 = float(input("Salario de los trabajadores en el departamento 1: "))
ventasdep2 = int(input("ventas del departamento 2: "))
salariodep2 = float(input("Salario de los trabajadores en el departamento 2: "))
ventasdep3 = int(input("ventas del departamento 3: "))
salariodep3 = float(input("Salario de los trabajadores en el departamento 3: "))

VentasTotales = ventasdep1 + ventasdep2 + ventasdep3
if ventasdep1 > VentasTotales /3:
    salariodep1 *= 1.2
if ventasdep2 > VentasTotales /3:
    salariodep2 *= 1.2
if ventasdep3 > VentasTotales /3:
    salariodep3 *= 1.2
print("Salario Departamento 1:",salariodep1, "Salario Departamento 2:", salariodep2, "Salario Departamento 3:",salariodep3 )    