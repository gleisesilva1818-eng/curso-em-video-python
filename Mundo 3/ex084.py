# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

temp = []
lista = []
mai = men = tot = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(lista) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    lista.append(temp[:]) # -> Faz a cópia
    temp.clear() # -> Limpa a lista temp
    tot += 1
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('--' * 30)
print(f'Ao todo você cadastrou {tot} pessoas.') # -> Ou {len(lista)}
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print() # -> Pula pra linha de baixo
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
