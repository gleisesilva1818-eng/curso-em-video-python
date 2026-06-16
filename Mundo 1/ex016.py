# Crie um programa que leia um número Real qualquer pelo teclado, e mostre na tela a sua porção inteira:

from math import trunc
valor = float(input('Digite um valor: '))
print(f'O valor digitado foi {valor}, e sua porção inteira é {trunc(valor)}')
