# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

print('==' * 15)
print('CADASTRE UMA PESSOA')
print('==' * 15)
tot18 = masc = fem = tot20m = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'F':
        fem += 1
    else:
        masc += 1
    if sexo == 'F' and idade < 20:
        tot20m += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('--' * 15)
    if resp == 'N':
        break
        print('--' * 15)
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {fem} mulheres e {masc} homens.')
print(f'{tot20m} Mulheres tem menos de 20 anos.')
