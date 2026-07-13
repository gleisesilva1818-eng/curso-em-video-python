# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com:
# Abaixo de 18.5: Abaixo do peso; Entre 18.5 e 25: Peso ideal; 20 até 30: Sobrepeso; 30 até 40: Obesidade; Acima de 40: Obesidade mórbida.

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.1f}.')
if imc < 18.5:
    print('Você está ABAIXO do peso normal!')
elif 18.5 <= imc < 25:
    print('Você está no peso IDEAL, parabéns!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, CUIDADO!')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA, MUITO CUIDADO!')
