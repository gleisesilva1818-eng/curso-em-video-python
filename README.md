# Curso em Vídeo: Python 3 - Gustavo Guanabara 🎓

<p align="center">
  <img src="https://img.shields.io/badge/Curso%20em%20V%C3%ADdeo-Python%203-blue?style=for-the-badge&logo=python&logoColor=yellow" alt="Badge Python">
  <img src="https://img.shields.io/badge/Status-Em%20Progresso-green?style=for-the-badge" alt="Badge Status">
</p>

Este repositório reúne os exercícios e desafios que desenvolvi ao longo do curso de Python do Gustavo Guanabara. Utilizo este espaço para consolidar minha lógica de programação, documentar os conceitos aprendidos e construir meu portfólio prático na tecnologia.

---

## 💡 O Diferencial deste Repositório

Como as aulas originais utilizam a sintaxe antiga de formatação (`.format()`), decidi **atualizar todos os códigos para o padrão moderno do mercado (`f-strings`)**. Em alguns arquivos, fiz questão de deixar a sintaxe antiga comentada para registrar e comparar a evolução da própria linguagem Python.

---

## 📂 Exercícios Inclusos (Mundo 1)

### 01. Olá, Mundo!
* **Descrição:** Primeiros testes com saída de dados no terminal.
* **Conceitos:** Uso do comando `print()` exibindo texto direto e através de variáveis.

### 02. Respondendo ao Usuário
* **Descrição:** Script de boas-vindas personalizado.
* **Conceitos:** Captura de dados com `input()` e interpolação de strings.

### 03. Somando Dois Números
* **Descrição:** Programa que lê dois valores e exibe a soma entre eles.
* **Conceitos:** Conversão de tipos de dados (`int`) e comparação entre a sintaxe antiga e a nova com `f-strings`.

### 04. Dissecando uma Variável
* **Descrição:** Analisador de propriedades de um valor digitado pelo teclado.
* **Conceitos:** Métodos internos de validação de strings (`.isnumeric()`, `.isalpha()`, `.isspace()`, etc.) e limpeza de vírgulas no código.

### 05. Antecessor e Sucessor
* **Descrição:** Lê um número inteiro e mostra quem vem antes e quem vem depois.
* **Conceitos:** Operações aritméticas simples realizadas diretamente dentro das chaves `{}` da string.

### 06. Dobro, Triplo e Raiz Quadrada
* **Descrição:** Exibe os cálculos matemáticos derivados de um número.
* **Conceitos:** Uso de operadores aritméticos, ordem de precedência (`** (1/2)`) e formatação de casas decimais (`:.2f`).

### 07. Média Aritmética
* **Descrição:** Calcula a média simples entre duas notas de um aluno.
* **Conceitos:** Manipulação de números de ponto flutuante (`float`) e controle de exibição de casas decimais com `:.1f`.

### 08. Conversor de Medidas
* **Descrição:** Transforma um valor em metros para centímetros e milímetros.
* **Conceitos:** Lógica de conversão matemática por multiplicação.

### 09. Tabuada v1.0
* **Descrição:** Exibe a tabuada completa de um número inteiro de 1 a 10.
* **Conceitos:** Repetição manual de operações, alinhamento visual de texto no terminal e uso de multiplicadores de strings (`'-' * 12`) para criar divisórias.

### 10. Conversor de Moedas
* **Descrição:** Lê quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar.
* **Conceitos:** Operações matemáticas de divisão com números de ponto flutuante (`float`) e formatação de casas decimais (`:.2f`) para representar valores monetários de forma realista.

### 11. Pintando Parede
* **Descrição:** Calcula a área de uma parede e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta cobre 2m².
* **Conceitos:** Operações matemáticas básicas e lógica de conversão proporcional baseada em variáveis.

### 12. Calculando Desconto
* **Descrição:** Aplica um desconto de 5% sobre o preço de um produto e exibe o valor final.
* **Conceitos:** Cálculo de porcentagem e formatação de saída de dados monetários com duas casas decimais (`:.2f`).

### 13. Reajuste Salarial
* **Descrição:** Calcula o novo salário de um funcionário com base em um aumento de 15%.
* **Conceitos:** Manipulação de variáveis com incremento percentual e formatação monetária.

### 14. Conversor de Temperaturas
* **Descrição:** Transforma uma temperatura de graus Celsius para Fahrenheit.
* **Conceitos:** Aplicação de fórmulas matemáticas de conversão com operadores aritméticos.

### 15. Aluguel de Carros
* **Descrição:** Calcula o preço total a pagar pelo aluguel de um carro com base nos dias utilizados e Km rodados.
* **Conceitos:** Acumulação de valores baseados em taxas fixas e variáveis.

### 16. Quebrando um Número
* **Descrição:** Lê um número real qualquer e exibe apenas a sua porção inteira.
* **Conceitos:** Importação e uso da função `trunc` do módulo `math`.

### 17. Catetos e Hipotenusa
* **Descrição:** Calcula o comprimento da hipotenusa a partir dos comprimentos dos catetos de um triângulo retângulo.
* **Conceitos:** Uso da função `hypot` do módulo `math` para simplificar cálculos geométricos.

### 18. Seno, Cosseno e Tangente
* **Descrição:** Lê um ângulo qualquer e exibe os valores de seu seno, cosseno e tangente.
* **Conceitos:** Conversão de graus para radianos (`radians`) e funções trigonométricas (`sin`, `cos`, `tan`) do módulo `math`.

### 19. Sorteando um Item na Lista
* **Descrição:** Escolhe aleatoriamente o nome de um entre quatro alunos para realizar uma tarefa.
* **Conceitos:** Estruturação de listas e uso da função `choice` do módulo `random`.

### 20. Sorteando uma Ordem na Lista
* **Descrição:** Sorteia e exibe a ordem de apresentação de quatro alunos.
* **Conceitos:** Embaralhamento de estruturas de dados usando a função `shuffle` do módulo `random`.

### 21. Tocando um MP3
* **Descrição:** Script que inicializa e reproduz o áudio de um arquivo MP3.
* **Conceitos:** Importação, inicialização e manipulação de recursos multimídia com a biblioteca externa `pygame`.

### 22. Analisador de Textos
* **Descrição:** Lê o nome completo de uma pessoa e faz diversas análises (letras maiúsculas, minúsculas, contagem total sem espaços e tamanho do primeiro nome).
* **Conceitos:** Métodos de strings (`.upper()`, `.lower()`, `.strip()`, `.count()`, `.split()`) e a função `len()`.

### 23. Separando Dígitos de um Número
* **Descrição:** Desembala um número de 0 a 9999 e mostra na tela as suas unidades, dezenas, centenas e milhares.
* **Conceitos:** Lógica matemática com operadores de divisão inteira (`//`) e resto da divisão (`%`).

### 24. Primeiras Letras de uma String
* **Descrição:** Verifica se o nome de uma cidade começa ou não com a palavra "SANTO".
* **Conceitos:** Fatiamento de strings (`[:5]`), padronização de caixa de texto e validação booleana.

### 25. Procurando uma String dentro de Outra
* **Descrição:** Identifica se uma pessoa possui o sobrenome "SILVA" em qualquer parte do nome completo.
* **Conceitos:** Uso do operador de associação `in` combinado com manipulação de strings.

### 26. Primeira e Última Ocorrência de uma String
* **Descrição:** Analisa uma frase para encontrar quantas vezes a letra "A" aparece, além das posições exatas da sua primeira e última ocorrência.
* **Conceitos:** Métodos `.count()`, `.find()` e `.rfind()`, aplicando ajuste de índice para o usuário final (`+1`).

### 27. Primeiro e Último Nome de uma Pessoa
* **Descrição:** Isola e exibe separadamente apenas o primeiro e o último nome de uma pessoa.
* **Conceitos:** Divisão de strings com `.split()` e indexação dinâmica usando o tamanho da lista (`len(nome)-1`).

---

## 🛠️ Ferramentas e Bibliotecas

* **Python 3**
* **Visual Studio Code (VS Code)**
* **Git & GitHub**

### 📦 Bibliotecas Externas

Para rodar o **Exercício 21 (Tocando um MP3)**, é necessário instalar a biblioteca **pygame**. Você pode instalá-la executando o seguinte comando no seu terminal:

*_pip install pygame_*

## 👤 Autora

* **Gleise** - [Meu LinkedIn](https://www.linkedin.com/in/gleisepacificosilva)
