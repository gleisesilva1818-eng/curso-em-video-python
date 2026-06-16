# Faça um programa que leia um ângulo qualquer, e mostre na tela o valor do seno, cosseno e tangente desse ângulo:

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(ang))
print(f'O ângulo de {ang} tem o SENO de {sen:.2f}')
cos = cos(radians(ang))
print(f'O ângulo de {ang} tem o COSSENO de {cos:.2f}')
tang = tan(radians(ang))
print(f'O ângulo de {ang} tem a TANGENTE de {tang:.2f}')
