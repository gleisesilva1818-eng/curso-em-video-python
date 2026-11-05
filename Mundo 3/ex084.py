# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

temp = []
lista = []
tot = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    lista.append(temp[:]) # -> Faz a cópia
    temp.clear() # -> Limpa a lista temp
    tot += 1
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Os dados foram {lista}')
print(f'Ao todo você cadastrou {tot} pessoas.') # -> Ou {len(lista)}
