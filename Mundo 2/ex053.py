# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. EX:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto [::-1]
print(f'O inverso de {junto} é: {inverso}')
if inverso == junto:
    print('A frase digitada É UM PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
