# -*- coding: utf-8 -*-
"""Lista_Exercicios3_Aldenis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13gkUDuONeDMxWJISlJV6RC0GuqaN6EKO

###IFPE Jaboatão
###Tecnologia em Análise e Desenvolvimento de Sistemas
###Disciplina: Lógica de Programação
###Professora: Havana Alves
###Aluno: Aldenis Everton Alves Guilherme de França

##Lista de Exercícios 3

###1. Crie um programa que calcule a média aritmética de um conjunto de 8 valores (podem ser inteiros ou float) que deve ser inserido pelo usuário. Ao final, o algoritmo deve exibir a média calculada.
"""

valor_aux = 0
cont = 0

while cont < 8:
  valor = input('Digite um número: ')
  valor = float(valor.replace(',','.'))
  valor_aux = valor + valor_aux
  cont = cont + 1
  media = valor_aux/cont

print('')
print('-' * 50)
print('A média dos 8 valores digitados é: {:.2f}.'.format(media))
print('-' * 50)

"""2. Faça um algoritmo que calcule a média de salários de uma empresa, pedindo ao
usuário o nome dos funcionários e os salários e devolvendo a média, o salário
mais alto e o salário mais baixo. Use nome = “fim” para encerrar a leitura.
"""

sal_aux = 0
c = maior = menor = 0
nome = 'S'
salario = 0

while nome != "fim":
  nome = input('Nome do funcionário (ou fim para encerrar): ').lower()
  if nome == 'fim':
    break
  salario = input('Salário do funcionário: ')
  salario = float(salario.replace(',','.'))
  sal_aux = salario + sal_aux
  c = c + 1
  if c == 1:
    menor = maior = salario
  else:
    if salario > maior:
      maior = salario
    if salario < menor:
      menor = salario
  
mediaSalario = sal_aux / c
print('')
print('-' * 70)
print('A média de salários dos {} funcionários é: R$ {:.2f}'.format(c,mediaSalario))
print('O maior salário é R$ {} e o menor salário é R$ {}'.format(maior, menor))
print('-' * 70)

"""3. Uma varejista está dando 60% de desconto em uma variedade de produtos para
queima de estoque. Ela gostaria de ajudar seus clientes a calcular a redução de
preço nos anúncios imprimindo uma tabela de descontos que mostra o preço
original e o preço depois do desconto aplicado. Escreva um programa que
receba vários preços de produtos e que no final imprima uma tabela com o
preço original e o preço novo. Deixe o formato em reais.
"""

produto = ''
tabela = ''

while produto != 'FIM':
  produto = input('Digite o nome do produto ou FIM para encerrar: ').upper()
  if produto == 'FIM':
    break
  preco = input('Digite o preço desse produto: ')
  preco = float(preco.replace(',','.'))
  precoNovo = 0.4*preco
  tabela = tabela + '\nProduto: {}\nValor Original: R$ {}\nValor com desconto: R$ {:.2f}\n'.format(produto,preco,precoNovo)

print('\nLISTA DOS PRODUTOS DA QUEIMA DE ESTOQUE:')
print(tabela)

"""4. Uma universidade utiliza a tabela abaixo para mapear notas dadas com letras
em valores decimais:

Seu programa deverá calcular o valor em pontos a
partir de uma das notas com letras disponíveis na
tabela, para os 13 alunos de uma turma. Cada nota
inserida servirá para calcular a média da turma. Ao
final, o programa deve parar de solicitar as notas e este
deve então imprimir todas as notas inseridas e a média
calculada.
"""

cont = 1
nota = nota_aux = 0
nomeAluno = notaLetra = tabelaNotas = ''

while cont <= 13:
  nomeAluno = input('\nDigite o nome do aluno(a): ')
  notaLetra = input('Digite a nota alfabética (conceito) do aluno(a): ').upper()
  cont = cont + 1

  if notaLetra == 'A+':
    nota = 4.0
  elif notaLetra == 'A-':
    nota = 3.7
  elif notaLetra == 'B+':
    nota = 3.3
  elif notaLetra == 'B-':
    nota = 2.7
  elif notaLetra == 'C+':
    nota = 2.3
  elif notaLetra == 'C-':
    nota = 1.7
  elif notaLetra == 'D+':
    nota = 1.3
  elif notaLetra == 'D-':
    nota = 0.0
  else:
    print('\nVocê digitou uma nota inválida! Tente novamente!')
    cont = cont - 1
    continue
  nota_aux = nota + nota_aux
  tabelaNotas = tabelaNotas + '\nAluno(a): {}\nConceito: {}\nNota: {}\n'.format(nomeAluno,notaLetra,nota)

print('\nLISTA DAS NOTAS DOS ALUNOS:')
print(tabelaNotas)
print('A média das notas da turma é {:.2f}'.format(nota_aux/13))

"""5. Um zoológico determina que o preço da entrada é baseado na idade do
visitante. Visitantes com até 2 anos de idade não pagam. Crianças de 3 a 12
anos pagam R$ 10,00. Idosos a partir dos 65 anos pagam R$ 15,00. Demais
pessoas pagam R$ 20,00. Crie um programa que ao chegar uma família,
pergunta a idade de cada um dos componentes dessa família e no final calcule o
valor devido. O programa deve parar e exibir o resultado quando for digitado um
valor vazio à pergunta sobre a idade. O valor deve ser exibido no formato em
reais.
"""

idade = 0
ingresso = ingresso_aux = 0

while idade != '':
  idade = input('Digite a idade do visitante em anos ou espaço para parar: ')
  if idade == '':
    break
  idade = int(idade)
  if idade <= 2:
    ingresso = 0
  elif 3 <= idade <= 12:
    ingresso = 10
  elif idade >= 65:
    ingresso = 15
  else:
    ingresso = 20
  ingresso_aux = ingresso + ingresso_aux

print('')
print('-' * 40)
print('A família irá pagar R$ {},00.'.format(ingresso_aux))
print('-' * 40)

"""6. O valor de π (pi) pode ser aproximando pela seguinte série infinita:
π ≈ 3 + 4
2 × 3 × 4 − 4
4 × 5 × 6 − 4
6 × 7 × 8 − 4
8 × 9 × 10 −...
Escreva um programa que exiba 15 aproximações de π. A primeira aproximação
deve fazer uso apenas do primeiro termo da série infinita (3). Cada próxima
aproximação exibida pelo seu programa deve incluir um ou mais termos na série.
"""

primeiroTermo = 3

fracao = 0
denominador = 2
termo = 0

print('Estes são os 15 primeiros termos da série infinita de π: \n')
print(primeiroTermo)

while fracao < 14:

  if fracao == 0:
    termo = primeiroTermo + 4 / (denominador * (denominador + 1) * (denominador + 2))
    denominador = denominador + 2
    print(termo)
    fracao = fracao + 1
  else:
    termo = termo - 4 / (denominador * (denominador + 1) * (denominador + 2))
    denominador = denominador + 2    
    print(termo)
    fracao = fracao + 1

"""7. Foi feita uma pesquisa com um grupo de alunos de uma universidade, na qual
se perguntou para cada aluno o número de vezes que utilizou o restaurante da
universidade no último mês. Construa um algoritmo que determine:

a) O percentual de alunos que utilizaram menos que 10 vezes o restaurante;

b) O percentual de alunos que utilizaram entre 10 e 15 vezes;

c) O percentual de alunos que utilizaram o restaurante acima de 15 vezes.
"""

qtdRest = 0
menos = medio = mais = cont = 0

while qtdRest != 'FIM':
  qtdRest = input('Digite quantas vezes você utilizou o restaurante da universidade no último mês ou FIM para encerrar? ').upper()
  if qtdRest == 'FIM':
    break
  qtdRest = int(qtdRest)
  cont = cont + 1
  if qtdRest < 10:
    menos = menos + 1
  elif 10 <= qtdRest <= 15:
    medio = medio + 1
  else:
    mais = mais + 1

print('\nPorcentagem de alunos que utilizaram o restaurante menos que 10 vezes: {:.2f}%'.format((menos/cont)*100))
print('Porcentagem de alunos que utilizaram o restaurante entre 10 e 15 vezes: {:.2f}%'.format((medio/cont)*100))
print('Porcentagem de alunos que utilizaram o restaurante acima de 15 vezes: {:.2f}%'.format((mais/cont)*100))

"""8. Escreva um programa que converta um valor binário (base 2) em um número
decimal (base 10). Seu programa deve começar lendo o número binário de um
usuário como uma string. Depois, ele deve calcular o equivalente decimal
processando cada dígito do valor binário. No fim de tudo, o programa deve
imprimir o valor decimal.
Ex: “001011” → 11
"""

decimal = 0
exp = 0

numBin = int(input('Digite o número binário: '))

while numBin != 0:
  digito = numBin % 10
  decimal = decimal + digito * 2 ** exp
  numBin = numBin // 10
  exp = exp + 1

print('\nO número binário digitado corresponde a {} na base decimal.'.format(decimal))

"""9. Faça um programa que imprime a tabuada de x até y (valores de x e y devem
ser digitados pelo usuário).
"""

Y = 0
x = int(input('Você quer a tabuada de que número? '))
y = int(input('Essa tabuada deve ir até que valor? '))

while Y < y:
  Y = Y + 1
  print('{} x {} = {}'.format(x,Y,x*Y))

x = int(input('Você quer a tabuada de que número? '))
y = int(input('Essa tabuada deve ir até que número? '))

while x <= y:
  cont = 1
  print('\nTabuada de {}'.format(x))
  while cont <= 10:
    print('{} x {} = {}'.format(x,cont,x*cont))
    cont = cont + 1
  x = x + 1

"""10. Um professor possui 5 turmas, e cada turma possui uma quantidade variada de
alunos. Construa um algoritmo que leia a quantidade de alunos em cada turma,
e para cada um deles, leia a nota. Exiba a média de notas por turma.
"""

turma = 1

while turma <= 5:
  qtdTurmas = 0
  qtdAlunos = int(input('Digite a quantidade de alunos da Turma {}: '.format(turma)))
  contAlunos = 1
  nota_aux = 0

  while contAlunos <= qtdAlunos:
    nomeAluno = input('Digite o NOME do aluno(a): ')
    notaAluno = input('Digite a NOTA do aluno(a): ')
    print('')
    notaAluno = float(notaAluno.replace(',','.'))

    contAlunos = contAlunos + 1
    nota_aux = notaAluno + nota_aux
    mediaTurma = nota_aux / qtdAlunos

  print('-' * 40)
  print('A média de notas da Turma {} é {:.2f}'.format(turma,mediaTurma))
  print('-' * 40)
  print('')
    
  turma = turma + 1