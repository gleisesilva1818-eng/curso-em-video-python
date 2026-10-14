# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.

lista = ('Anel', 15.50,
        'Colar', 20,
        'Harness', 30,
        'Gargantilha', 45,
        'Cinto', 25,
        'Pulseira', 10,
        'Piercing', 35,
        'Alargador', 40)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
for pos in range(0, len(lista)): # pos = posição
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>5.2f}')
print('-' * 40)
