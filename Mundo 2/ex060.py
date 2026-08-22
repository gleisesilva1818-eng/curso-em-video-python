# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número para calcular seu Fatorial: '))
cont = num
fac = 1
print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fac *= cont
    cont -= 1
print(f'{fac}')
