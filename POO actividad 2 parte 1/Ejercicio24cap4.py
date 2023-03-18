esferaA = float(input("A = "))
esferaB = float(input("B = "))
esferaC = float(input("C = "))
#sin usar la built-in function max()
if esferaA > esferaB and esferaA > esferaC:
    print("La esfera de mayor peso es A")
elif esferaB > esferaA and esferaB > esferaC:
    print("La esfera de mayor peso es B")
elif esferaC > esferaB and esferaC > esferaA:
    print("La esfera de mayor peso es C")