#RAIZ QUADRA, DOBRO E TRIPLO
import math

numero = int(input('Digite um numero: '))
raiz = math.sqrt(numero)
#raiz = numero ** (1/2)
#raiz = math.pow(numero, 1/2)
dobro = numero * 2
triplo = numero * 3

print("A raiz quandrada é {:.3f} \nO dobro é: {} \nO triplo é: {} ".format(raiz, dobro, triplo))
