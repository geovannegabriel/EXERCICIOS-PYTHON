#CONVERSOR DE MOEDAS

real = float(input("Quanto dinheiro voce tem na carteira? "))
dolar = real / float(5.25)

print("Com {} reais voce pode comprar {:.3} dollares. ".format(real, dolar))
