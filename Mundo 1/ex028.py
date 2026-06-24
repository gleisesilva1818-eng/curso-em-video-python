# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu:

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "pensar"
print('--=--' * 15)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('--=--' * 15)
jogador = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(2)
print('--=--' * 15)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'VOCÊ PERDEU! O número que pensei foi {computador}.')
print('--=--' * 15)
