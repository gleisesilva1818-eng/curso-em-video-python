# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial
num = int(input('Digite um número para calcular seu Fatorial: '))
fac = factorial(num)
print(f'O Fatorial de {num} é {fac}.')
