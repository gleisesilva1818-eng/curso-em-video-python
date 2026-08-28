# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser
# que quer mostrar 0 termos.

print('GERADOR DE PA')
print('--=--' * 12)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end= ' - ')
        termo += razão
        cont += 1
    print('PAUSA')
    print('--=--' * 12)
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('--=--' * 12)
print(f'PROGRESSÃO FINALIZADA COM {total} TERMOS MOSTRADOS!')
