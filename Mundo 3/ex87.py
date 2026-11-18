# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = mai = somacoluna = 0
for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = (int(input(f'Digite um valor para [{linha}, {c}] ')))
print('--' * 30)
for linha in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[linha][c]:^5}]', end= '')
        if matriz[linha][c] % 2 == 0:
            somapar += matriz[linha][c]
    print()
print('--' * 30)
print(f'A soma dos valores pares é de {somapar}')
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é de {somacoluna}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
