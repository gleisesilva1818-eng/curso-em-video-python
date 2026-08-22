# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar [2] multiplicar [3] maior [4] novos números [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('-=-' * 8)


print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
opc = str(input('Digite a sua opção: '))
print('-=-' * 8)
