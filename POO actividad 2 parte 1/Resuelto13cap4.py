BolasDescuentos = {"blanca": 0, "verde": 10, "amarilla": 25, "azul": 50, "roja":100}
ValorCompra = float(input("Valor: "))
Color = input("Color de la bola(minuscula y femenino): ")
print("Valor con descuento :",ValorCompra*(1-BolasDescuentos[Color]/100))