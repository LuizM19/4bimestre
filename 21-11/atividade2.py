import math 
numero1=int(input('Informe o primeiro numero inteiro'))
if numero1 >= 0:
    raiz= math.sqrt(numero1)
    print(f"A raiz é {raiz}")
elif numero1 < 0:
    print('O numero é negativo')