# Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triângulo retângulo , calcule e mostre
# o comprimento da hipotenusa:

from math import hypot
cop = float(input('Comprimento do cateto oposto: '))
caa = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cop, caa)
print(f'A hipotenusa vai medir: {hip:.2f}')
