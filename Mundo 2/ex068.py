# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.

print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-=' * 20)
from random import randint
vit = 0
perda = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}, total de {total}.')
    print('Deu PAR!' if total % 2 == 0 else 'Deu ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vit += 1
        else:
            print('Você PERDEU!')
            perda += 1
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vit += 1
        else:
            print('Você PERDEU!')
            perda += 1
            break
    print('--' * 20)
    print('Vamos jogar novamente...')
print('--' * 20)
print('GAME OVER!')
print(f'''VITÓRIAS: {vit}
DERROTAS: {perda}''')
print('--' * 20)

