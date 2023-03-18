Nombre = input()
Horas = int(input())
ValorDeLaHora = int(input())
Salario = Horas*ValorDeLaHora
if Horas > 48:
    Salario = (Horas-48)*(ValorDeLaHora*3) + 8*(ValorDeLaHora*2) + 40*ValorDeLaHora
elif Horas > 40:
    Salario = (Horas-40)*(ValorDeLaHora*2) + 40*(ValorDeLaHora)
print(Nombre)
print("Salario :",Salario)
