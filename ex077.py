# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.

palavras = ('Programar', 'Python', 'Curso', 'Linguagem',
            'Algoritmos', 'Logica', 'Estudar', 'Aprender',
            'Trabalhar', 'Praticar', 'Programador', 'Estudante')
for p in palavras: # -> laço'for' para isolar cada palavra
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiouAEIOU':
            print(letra, end=' ')
