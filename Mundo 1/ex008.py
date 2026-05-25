# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros:

metros = float(input('Digite uma distância em metros: '))
cm = metros * 100
mm = metros * 1000
print(f'A medida de {metros}m corresponde a {cm}cm e {mm}mm.')
