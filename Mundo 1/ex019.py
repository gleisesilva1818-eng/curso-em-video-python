# Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido:

from random import choice
pri = input('Primeiro aluno: ')
seg = input('Segundo aluno: ')
ter = input('Terceiro aluno: ')
qua = input('Quarto aluno: ')
lista = [pri, seg, ter, qua]
escolhido = choice(lista)
print(f'O aluno escolhido foi: {escolhido}')
