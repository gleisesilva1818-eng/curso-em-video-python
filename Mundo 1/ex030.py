# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar:

from time import sleep
num = int(input('Digite um número qualquer: '))
print('Analisando...')
sleep(1)
result = num % 2
if result == 0:
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é Impar!')
