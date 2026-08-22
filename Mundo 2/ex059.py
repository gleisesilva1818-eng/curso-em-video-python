# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar [2] multiplicar [3] maior [4] novos números [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('-=-' * 14)
opc = 0
while opc != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opc = int(input('Digite a sua opção: '))
    if opc == 1:
        soma = n1 + n2
        print(f'>>>>> A soma entre {n1} + {n2} é: {soma}.')
    elif opc == 2:
        mult = n1 * n2
        print(f'>>>>> O resultado de {n1} x {n2} é: {mult}.')
    elif opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'>>>>> Entre {n1} e {n2}, o MAIOR valor é {maior}.')
    elif opc == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('FINALIZANDO...')
    else:
        print('Opção inválida. Tente novamente!')
    print('-=-' * 14)
    sleep(2)

print('FIM DO PROGRAMA! VOLTE SEMPRE!')
