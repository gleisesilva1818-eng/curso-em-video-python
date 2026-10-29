# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
while True:
    lista.append(int(input('Digite um número: '))) 
    while True: # -> Loop de validação
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'SsNn':
            break # -> Sai do loop da pergunta
        print('Resposta inválida... Tente novamente')
    if resp in 'Nn': # -> Sai do loop de validação
        break
print('--' * 30)
print(f'A lista completa é: {lista}')
