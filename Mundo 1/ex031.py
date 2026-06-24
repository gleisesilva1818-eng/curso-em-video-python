# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 para viagens mais longas:

dist = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {dist}Km/h')
if dist <= 200:
    price = dist * 0.50
    print(f'O preço da sua passagem será de R${price:.2f}.')
else:
    price = dist * 0.45
    print(f'O preço da sua passagem será de R${price:.2f}.')
