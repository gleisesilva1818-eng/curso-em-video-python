# Curso em Vídeo: Python 3 - Gustavo Guanabara 🎓

<p align="center">
  <img src="https://img.shields.io/badge/Curso%20em%20V%C3%ADdeo-Python%203-blue?style=for-the-badge&logo=python&logoColor=yellow" alt="Badge Python">
  <img src="https://img.shields.io/badge/Mundo%201-Concluido-brightgreen?style=for-the-badge" alt="Mundo 1">
  <img src="https://img.shields.io/badge/Mundo%202-Em%20Progresso-orange?style=for-the-badge" alt="Mundo 2">
</p>

Este repositório foi criado para consolidar meu aprendizado prático em **Python 3** através do Curso em Vídeo. Aqui, organizo e documento cada desafio desenvolvido no VS Code, aplicando conceitos fundamentais de lógica de programação e estruturas de controle.

---

## 🎯 Progresso de Aprendizado

| Módulo | Status | Descrição |
| :--- | :---: | :--- |
| **Mundo 1: Fundamentos** | 🟢 Concluído | Tipos de dados primitivos, operadores aritméticos, integração de bibliotecas nativas, manipulação de strings e análise de textos, e estruturas de decisão (lógica condicional simples e composta). |
| **Mundo 2: Estruturas de Controle** | 🟡 Ativo | Condicionais aninhadas (lógica booleana ramificada), e estruturas de repetição controladas por contadores (for) e por teste lógico (while com interrupções de fluxo). |

---

## 📚 Módulos Desenvolvidos

<details>
<summary><b>🌍 Mundo 1: Fundamentos (Exercícios 01 a 35) — [CONCLUÍDO]</b></summary>

### 01. Olá Mundo
* **Descrição:** Seu primeiro programa em Python.
* **Conceitos:** Saída de dados simples utilizando o comando `print`.

### 02. Respondendo ao Usuário
* **Descrição:** Lê o nome de uma pessoa e mostra uma mensagem de boas-vindas.
* **Conceitos:** Interação básica com o usuário usando entrada de dados (`input`) e formatação de strings.

### 03. Somando Dois Números
* **Descrição:** Lê dois números e exibe a soma entre eles.
* **Conceitos:** Tipos primitivos (`int`), manipulação numérica e conversão de dados.

### 04. Dissecando uma Variável
* **Descrição:** Lê algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possíveis sobre ele (se é numérico, se está em maiúsculas, etc).
* **Conceitos:** Funções e métodos de teste de tipo e estado das strings (`isnumeric()`, `isalpha()`, etc).

### 05. Antecessor e Sucessor
* **Descrição:** Lê um número inteiro e mostra na tela o seu sucessor e seu antecessor.
* **Conceitos:** Operadores aritméticos simples de incremento e decremento.

### 06. Dobro, Triplo e Raiz Quadrada
* **Descrição:** Lê um número e mostra o seu dobro, triplo e raiz quadrada.
* **Conceitos:** Operações aritméticas e cálculo de potência (`**` ou usando `pow()`).

### 07. Média Aritmética
* **Descrição:** Lê duas notas de um aluno, calcula e mostra a sua média.
* **Conceitos:** Precedência de operadores aritméticos aplicados à média simples.

### 08. Conversor de Medidas
* **Descrição:** Lê um valor em metros e o exibe convertido em centímetros e milímetros.
* **Conceitos:** Regras de conversão de unidades através de multiplicação aritmética.

### 09. Tabuada v1.0
* **Descrição:** Lê um número inteiro qualquer e mostra na tela a sua tabuada completa.
* **Conceitos:** Operadores aritméticos aplicados repetidamente para gerar tabulações de dados simples.

### 10. Conversor de Moedas
* **Descrição:** Lê quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar.
* **Conceitos:** Cálculos aritméticos aplicados à conversão de moedas.

### 11. Pintando Parede
* **Descrição:** Lê a largura e a altura de uma parede em metros, calcula a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
* **Conceitos:** Resolução de problemas geométricos básicos e regras de proporção direta.

### 12. Calculando Descontos
* **Descrição:** Lê o preço de um produto e mostra seu novo preço, com 5% de desconto.
* **Conceitos:** Cálculos de porcentagem simples (redução).

### 13. Reajuste Salarial
* **Descrição:** Lê o salário de um funcionário e mostra seu novo salário, com 15% de aumento.
* **Conceitos:** Cálculos de porcentagem simples (acréscimo).

### 14. Conversor de Temperaturas
* **Descrição:** Escreve um programa que converte uma temperatura digitada em °C para °F.
* **Conceitos:** Aplicação de fórmulas físicas de conversão de dados decimais.

### 15. Aluguel de Carros
* **Descrição:** Escreve um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcula o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
* **Conceitos:** Lógica aplicada a problemas comerciais reais e múltiplas variáveis operacionais.

### 16. Quebrando um Número
* **Descrição:** Lê um número real qualquer pelo teclado e mostra na tela a sua porção inteira.
* **Conceitos:** Importação de módulos (`math`), uso da função `trunc` ou manipulação de conversão para `int`.

### 17. Catetos e Hipotenusa
* **Descrição:** Lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcula e mostra o comprimento da hipotenusa.
* **Conceitos:** Aplicação matemática de Teorema de Pitágoras com funções do módulo `math`.

### 18. Seno, Cosseno e Tangente
* **Descrição:** Lê um ângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo.
* **Conceitos:** Funções trigonométricas do módulo `math` e necessidade de conversão de graus para radianos.

### 19. Sorteando um Item na Lista
* **Descrição:** Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
* **Conceitos:** Manipulação de listas e o método `choice` da biblioteca `random`.

### 20. Sorteando uma Ordem na Lista
* **Descrição:** O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
* **Conceitos:** Estrutura de listas ordenáveis e o método `shuffle` da biblioteca `random`.

### 21. Tocando um MP3
* **Descrição:** Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
* **Conceitos:** Integração com bibliotecas externas (`pygame`) e manipulação de fluxos multimídia.

### 22. Analisador de Textos
* **Descrição:** Lê o nome completo de uma pessoa e mostra: o nome com todas as letras maiúsculas, minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.
* **Conceitos:** Funções nativas de strings (`upper()`, `lower()`, `len()`, `strip()`, `find()`, `split()`).

### 23. Separando Dígitos de um Número
* **Descrição:** Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados (unidade, dezena, centena, milhar).
* **Conceitos:** Manipulação matemática de divisões inteiras e restos ou formatação textual estrita.

### 24. Verificando as Primeiras Letras de um Texto
* **Descrição:** Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
* **Conceitos:** Fatiamento de strings e padronização com `upper()`.

### 25. Procurando uma String Dentro de Outra
* **Descrição:** Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
* **Conceitos:** Uso do operador de pertinência `in`.

### 26. Primeira e Última Ocorrência de uma String
* **Descrição:** Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
* **Conceitos:** Análise detalhada de strings usando funções como `count()`, `find()`, `rfind()`.

### 27. Primeiro e Último Nome de uma Pessoa
* **Descrição:** Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
* **Conceitos:** Fatiamento e indexação dinâmica de listas baseadas em strings com `split()`.

### 28. Jogo da Adivinhação v1.0
* **Descrição:** O computador escolhe um número inteiro entre 0 e 5 e o usuário tenta adivinhar. O programa avisa se o jogador venceu ou perdeu.
* **Conceitos:** Uso do método `randint` do módulo `random`, estruturas condicionais e efeito de transição com `sleep` do módulo `time`.

### 29. Radar Eletrônico
* **Descrição:** Lê a velocidade de um carro. Se ultrapassar 80 km/h, exibe uma mensagem dizendo que ele foi multado e calcula o valor (R$ 7,00 por cada km acima do limite).
* **Conceitos:** Estrutura condicional simples e cálculo de taxas operacionais baseadas em limites de variáveis.

### 30. Par ou Ímpar?
* **Descrição:** Lê um número inteiro qualquer e mostra na tela se ele é PAR ou ÍMPAR com um efeito de análise simulada.
* **Conceitos:** Operador de resto da divisão (`%`), condicionais e controle de tempo com `sleep`.

### 31. Custo da Viagem
* **Descrição:** Calcula o preço de uma passagem de viagem baseado na distância em km. Cobra R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
* **Conceitos:** Condicionais compostas para aplicação de tarifas dinâmicas e manipulação de ponto flutuante.

### 32. Ano Bissexto
* **Descrição:** Lê um ano qualquer e mostra se ele é bissexto. Permite usar o número 0 para puxar e validar dinamicamente o ano atual configurado no sistema.
* **Conceitos:** Importação e manipulação do módulo nativo `datetime` e lógica booleana complexa combinando os operadores `and` e `or`.

### 33. Maior e Menor Valores
* **Descrição:** Lê três números e mostra qual é o maior e qual é o menor deles.
* **Conceitos:** Lógica de atribuição e eliminação por comparações lógicas repetidas (estruturas condicionais em sequência).

### 34. Aumentos Múltiplos
* **Descrição:** Calcula o reajuste de um salário baseado em faixas: para salários superiores a R$ 1.250,00, aumento de 10%. Para os inferiores ou iguais, aumento de 15%.
* **Conceitos:** Estruturas condicionais compostas (`if/else`) aplicadas a regras de negócio e reajustes percentuais.

### 35. Analisando Triângulo v1.0
* **Descrição:** Lê o comprimento de três retas e diz ao usuário se elas podem ou não formar um triângulo.
* **Conceitos:** Operador lógico de conjunção (`and`) para validação matemática de condições de existência geométricas.

</details>

<details>
<summary><b>🚀 Mundo 2: Estruturas de Controle (Exercícios 36 ao 71) — [EM PROGRESSO]</b></summary>

### 🛠️ Práticas e Conceitos Aplicados nesta Etapa:
* **Condicionais Aninhadas:** Tomadas de decisão mais complexas utilizando a estrutura `if/elif/else`.
* **Estruturas de Repetição Controladas:** Laços contados iterativos através da instrução `for`.
* **Módulos Práticos:** Utilização e importação de módulos externos para controle de tempo (`time`) e geração de valores pseudoaleatórios (`random`).

*📂 Os scripts desenvolvidos estão organizados dentro da pasta `Mundo 2`.*

---

### 36. Aprovando Empréstimo
* **Descrição:** Avalia a viabilidade do empréstimo bancário para a compra de uma casa com base no valor do imóvel, salário do comprador e anos de financiamento. A prestação mensal não pode exceder 30% do salário.
* **Conceitos:** Condicionais compostas e operações matemáticas para cálculo de porcentagem e divisões de prazos.

### 37. Conversor de Bases Numéricas
* **Descrição:** Solicita um número inteiro e realiza a conversão para binário, octal ou hexadecimal com base na escolha de menu do usuário.
* **Conceitos:** Conversões nativas utilizando as funções built-in `bin()`, `oct()` e `hex()`, além de fatiamento de strings (`[2:]`) para remoção de prefixos.

### 38. Comparando Números
* **Descrição:** Lê dois números inteiros e os compara, retornando se o primeiro ou o segundo é maior, ou se ambos são iguais.
* **Conceitos:** Estrutura condicional aninhada (`if/elif/else`) aplicada a operadores de comparação.

### 39. Alistamento Militar
* **Descrição:** Lê o ano de nascimento de um jovem e calcula, baseado no ano atual do sistema, se ele ainda vai se alistar, se está no prazo imediato ou se já passou do tempo regulamentar, exibindo o saldo de anos em falta ou atraso.
* **Conceitos:** Manipulação e consulta dinâmica do ano do sistema utilizando a biblioteca nativa `datetime` (módulo `date`).

### 40. Aquele clássico da Média
* **Descrição:** Coleta duas notas, realiza o cálculo da média aritmética do aluno e exibe se ele está aprovado (>= 7.0), em recuperação (entre 5.0 e 6.9) ou reprovado (< 5.0).
* **Conceitos:** Operadores lógicos (`and`) e comparativos em estruturas de decisão.

### 41. Classificando Atletas
* **Descrição:** Com base no ano de nascimento, define a categoria ideal para um nadador da Confederação Nacional de Natação: Mirim (até 9 anos), Infantil (até 14), Júnior (até 19), Sênior (até 25) ou Master (acima disso).
* **Conceitos:** Condicionais em cadeia utilizando a biblioteca `datetime`.

### 42. Analisando Triângulos v2.0
* **Descrição:** Evolução do Desafio 35. Além de checar se três segmentos podem formar um triângulo, o sistema identifica e informa se ele é Equilátero, Isósceles ou Escaleno.
* **Conceitos:** Operadores lógicos de conjunção (`and`), igualdade em cadeia (`s1 == s2 == s3`) e desigualdade mútua.

### 43. Índice de Massa Corporal (IMC)
* **Descrição:** Recebe altura e peso do usuário para calcular e classificar o IMC entre: abaixo do peso, peso ideal, sobrepeso, obesidade e obesidade mórbida.
* **Conceitos:** Operador de potência (`**`) aplicado a cálculos biométricos decimais (`float`).

### 44. Gerenciador de Pagamentos
* **Descrição:** Realiza o cálculo do preço a ser pago por um produto de acordo com a condição escolhida no terminal: à vista (10% de desconto no dinheiro/cheque, 5% no cartão), 2x sem juros ou 3x ou mais com cobrança de 20% de juros.
* **Conceitos:** Lógica de negócios aplicada a porcentagens dinâmicas e parcelamento condicional de variáveis.

### 45. Game: Jokenpô
* **Descrição:** O clássico jogo de "Pedra, Papel e Tesoura" rodando no terminal contra as jogadas aleatórias selecionadas pelo computador.
* **Conceitos:** Manipulação de coleções imutáveis (Tuplas), importação e uso do módulo `randint` de `random` e controle de pausas cênicas com `sleep` de `time`.

### 46. Contagem Regressiva
* **Descrição:** Executa no terminal uma contagem de 10 até 0 com pausas ritmadas de 1 segundo para simular o estouro de fogos de artifício.
* **Conceitos:** Estrutura de repetição controlada por variável (`for`) com decremento progressivo (passo `-1`) e módulo `time.sleep()`.

### 47. Contagem de Pares
* **Descrição:** Mostra dinamicamente na tela todos os números pares que estão no intervalo entre 1 e 50.
* **Conceitos:** Utilização eficiente da função `range()` configurando o incremento direto de passo (`2`) para otimizar processamento.

### 48. Soma de Ímpares Múltiplos de Três
* **Descrição:** Calcula e exibe a soma de todos os números ímpares e que sejam simultaneamente múltiplos de 3 no intervalo de 1 até 500.
* **Conceitos:** Estrutura `for` combinada com condições de módulo aritmético (`% 3 == 0`) e lógica de acumuladores/contadores numéricos.

### 49. Tabuada v2.0
* **Descrição:** Otimização do Desafio 09. Gera dinamicamente a tabuada completa de multiplicação para o valor inteiro informado pelo usuário.
* **Conceitos:** Geração de sequências repetitivas com o laço `for`.

### 50. Soma dos Pares
* **Descrição:** Solicita 6 entradas de números inteiros no terminal e realiza a soma acumulada unicamente daqueles que forem pares, descartando os ímpares.
* **Conceitos:** Lógica de entrada dinâmica dentro de laços de repetição aliada a filtros condicionais de resto de divisão.

### 51. Progressão Aritmética (PA)
* **Descrição:** Recebe o primeiro termo e a razão de uma Progressão Aritmética e exibe seus 10 primeiros termos no console.
* **Conceitos:** Lógica de progressões matemáticas calculando o enésimo termo e aplicando-o na parametrização do laço `for`.

</details>

---

## 🛠️ Tecnologias e Ferramentas

* **Python 3.x**
* **Visual Studio Code (VS Code)**
* **Git & GitHub**

### 📦 Bibliotecas Utilizadas

Para garantir o funcionamento correto dos desafios instalados localmente:

* **`pygame`**: Utilizada para a execução de arquivos de áudio (Exercício 21).

Instale rodando no terminal:
```bash
pip install pygame

```

## 👤 Autora

* **Gleise** - [Meu LinkedIn](https://www.linkedin.com/in/gleisepacificosilva/)
