# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
ímpar = []
while True:
    lista.append(int(input('Digite um número: '))) 
    while True: # -> Loop de validação
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'SsNn':
            break # -> Sai do loop da pergunta
        print('Resposta inválida... Tente novamente')
    if resp in 'Nn':
        break # -> Sai do loop de validação
print('--' * 30)
print(f'A lista completa é: {lista}')
for i, v in enumerate(lista): # -> Separa os pares e ímpares
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpar.append(v)
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {ímpar}')
