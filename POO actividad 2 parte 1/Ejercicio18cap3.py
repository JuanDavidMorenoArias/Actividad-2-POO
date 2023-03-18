CodigoEmpleado = input("Codigo del empleado: ")
NombreEmpleado = input("Nombre del empleado: ")
HorasTrabajadas = int(input("Horas trabajadas al mes: "))
ValorPorHora = float(input("valor hora trabajada: "))
Retencion = float(input("porcentaje de retencion en la fuente: "))
sb = int(HorasTrabajadas*ValorPorHora)

print("codigo:", CodigoEmpleado, "Nombre:", NombreEmpleado, "Salario bruto:", sb, "Salario neto:", int(sb*(1-Retencion/100)))