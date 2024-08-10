'''

Luiz Eduardo Vieira Barreto
04/03/2020
Turma: 1A

'''
import math

#Criação de funções#

PI = 3.14

def SOMA(a , b , c):
  som = a + b + c
  return som

def SUBTRAÇÃO(a , b , c):
  sub = a - b - c
  return sub

def MULTIPLICAÇÃO(a , b , c):
  mult = a * b * c
  return mult

def DIVISÃO(a , b , c):
  divi = a / b / c
  return divi

#Calcúlo de média de Aluno#
def MÉDIA_DO_ALUNO(a , b , c , d):
  média = (a + b + c + d) / 4
  return média

#Terça parte do Quadrado de um número#
def QUADRADO_NUMERO(a):
  result = (a ** 2) / 3
  return result

#Retorne o quadrado e a raiz quadrada de um número#
def QUADRADO_E_RAIZ(a):
  result = a ** 2
  result2 = a * 0,5
  return result , result2

#Média ponderada de 4 valores#
def MÉDIA_PONDERADA(a , b , c , d):
  result = (1 * a + 2 * b + 3 * c + 4 * d) / (1 + 2 + 3 + 4)
  return result 

#Area das formas geométricas#
def AREA_CIRULO(r):
  result = PI * (r ** 2)
  return result

def AREA_QUADRADO(a , b):
  result = a * b
  return result

def AREA_RETÂNGULO(base , altura):
  result = base * altura
  return result

def AREA_TRIÂNGULO(base , altura):
  result = base * altura / 2
  return result

#Perímetro das Formas Geométricas#
def PERÍMETRO_CIRCULO(r):  
  result = 2 * PI * r
  return result

def PERÍMETRO_QUADRADO(lado):
  result = lado * 4
  return result

def PERÍMETRO_RETÂNGULO(comprimento , largura):
  result = 2 * (comprimento + largura) ** 4
  return result

def PERÍMETRO_TRIÂNGULO(lado1):
  result = 3 * lado1
  return result

#Função para calcúlo de um triângulo equilátero, com apenas um lado fornecido#
def AREA_TRIÂNGULO_EQUILÁTERO(lado):
  result = ( (lado ** 2) * math.sqrt(3)  / 2)
  return result

#Função antecessor e sucessor
def ant_e_suc(a):
  antecessor = a - 1
  sucessor = a + 1
  result = 'O antecessor é: {}. O sucessor é: {}'.format(antecessor , sucessor)
  return result

#Função exercícios#
def exercicio_1():
  print('-' * 30)
  print('          Operações')
  print('-' * 30)
  print('''
  [ 1 ]Somar
  [ 2 ]Subtração
  [ 3 ]Multiplicação
  [ 4 ]Divisão
  ''')
  perg = 0
  perg = int(input('Qual opção deseja escolher? ') )

  if perg == 1:
    n1 = int(input('Defina o primeiro número: ') )
    n2 = int(input('Defina o segundo número: ') )
    n3 = int(input('Defina o terceiro número: ') )
    result = SOMA (n1 , n2 , n3)
    print('O resultado é' , result)
  if perg == 2:
    n1 = int(input('Defina o primeiro número: ') )
    n2 = int(input('Defina o segundo número: ') )
    n3 = int(input('Defina o terceiro número: ') )
    result = SUBTRAÇÃO(n1 , n2 , n3)
    print('O resultado é' , result)
  if perg == 3:
    n1 = int(input('Defina o primeiro número: ') )
    n2 = int(input('Defina o segundo número: ') )
    n3 = int(input('Defina o terceiro número: ') )
    result = MULTIPLICAÇÃO(n1 , n2 , n3)
    print('O resultado é' , result)
  if perg == 4:
    n1 = int(input('Defina o primeiro número: ') )
    n2 = int(input('Defina o segundo número: ') )
    n3 = int(input('Defina o terceiro número: ') )
    result = DIVISÃO(n1 , n2 , n3)
    print('O resultado é' , result)

def exercicio_2():
  print('-' * 30)
  print('Calcúlo de Área:')
  print('-' * 30)
  print(''' 
  [ 1 ]Quadrado
  [ 2 ]Círculo
  [ 3 ]Retângulo
  [ 4 ]Triângulo
  ''')
  
  perg = 0
  perg = int(input('Qual a sua opção? ') )

  if perg == 1:
    base = int(input('Defina a base do quadrado em mt: ') )
    altura = int(input('Defina a altura do quadrado em mt: ') )
    result = AREA_QUADRADO (base , altura)
    print('A área do quadrado é' , result , 'mt.')
  if perg == 2:
    raio = float(input('Defina o raio do Circúlo: '))
    result = AREA_CIRULO(raio)
    print('A área do circúlo é' , result)
  if perg == 3:
    base = float(input('Defina a base do retângulo: '))
    altura = float(input('Defina a altura: '))
    result = AREA_RETÂNGULO(base , altura)
  if perg == 4:
    base = int(input('Defina a base do Triângulo: '))
    altura = int(input('Defina a altura do Triângulo:'))
    result = AREA_TRIÂNGULO(base , altura)
    print('A área do Triângulo é' , result)

def exercicio_3():
  lado = float(input('Defina o Lado do Triângulo Equilátero: '))
  result = AREA_TRIÂNGULO_EQUILÁTERO(lado)
  print('A área do Triângulo Equilátero é {}'.format(result))

def exercicio_4():
  print('=' * 30)
  print('Calcúlo de média de aluno:')
  print('=' * 30)
  nt1 = float(input('Insira a nota da primeira prova: '))
  nt2 = float(input('Insira a nota da segunda prova: '))
  nt3 = float(input('Insira a nota da terceira prova: '))
  nt4 = float(input('Insira a nota da quarta prova: '))
  result = MÉDIA_DO_ALUNO(nt1 , nt2 , nt3 , nt4)
  print('A média do Aluno é' , result)

def exercicio_5():
  print('-' * 30)
  print('Descubra o antecessor e o sucessor de um número')
  print('-' * 30)
  numero = int(input('Digite um número: '))
  result = ant_e_suc(numero)
  print(result)

def exercicio_6():
  print('-' * 30)
  num1 = float(input('Defina um número: ') )
  result = QUADRADO_NUMERO(num1)
  print('O 1/3 de {} elevado ao quadrado é {}'.format(num1 , result))

def exercicio_7():
  n1 = float(input('Defina um número: '))
  result = QUADRADO_E_RAIZ(n1)
  print('O quadrado: {} e Raiz quadrada: {}'.format(result))

def exercicio_8():
  nt1 = float(input('Insira a nota da primeira prova: ') )
  nt2 = float(input('Insira a nota da segunda prova: ') )
  nt3 = float(input('Insira a nota da terceira prova: ') )
  nt4 = float(input('Insira a nota da quarta prova: ') )
  result = MÉDIA_PONDERADA(nt1 , nt2 , nt3 , nt4)
  print('A média ponderada é {}'.format(result))

