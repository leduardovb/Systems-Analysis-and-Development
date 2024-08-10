''' 

Luiz Eduardo Vieira Barreto
Data: 17/03/2020
1° Período TADS

'''

import math


def titulo(a):
  print('=' * 30)
  print('{:^30}'.format(a))
  print('=' * 30)

def ex_1(a , b , c , d , e , f):
  peso_maximo = a
  peso_total =  b + c + d + e + f
  if peso_maximo > peso_total:
    result = 'Portas fechando...'
  else:
    result = 'Carga máxima excedida...'
  return result

def ex_2(a):
  result = a % 3 
  result1 = a % 7 
  if result and result1 == 0:
    resultado = 'O número {} é divísivel por 3 e 7'.format(a)
  else:
    resultado = 'O número {} não é divísivel por 3 e 7'.format(a)
  return resultado

def ex_3(a , b , c , d):
  media = (a + b + c + d) / 4
  if media > 7:
    result = 'Aluno aprovado'
  else:
    result = 'Aluno reprovado'
  return result
  
def ex_4(a , b):
  n1 = a
  n2 = b
  if n1 > n2:
    result = n1 - n2
    diferenca = result * 0.6
    resultado = 'A diferença é {} e 60% de {} é {}'.format(result , result , diferenca)
    
  else:
    result = n1 - n2
    diferenca = result * 0.6
    resultado = 'A diferença é {} e 60% de {} é {}'.format(result , result , diferenca)
  return resultado

def ex_5(a , b):
  n1 = a
  n2 = b
  if n1 > n2:
    result = 'O número maior entre {} e {} é {}'.format(n1 , n2 , n1)
  elif n2 > n1:
    result = 'O número maior entre {} e {} é {}'.format(n1 , n2 , n2)
  elif n1 == n2:
      result = 'Os números são iguais'
  return result

def ex_6(a):
  total_minutos = a
  total_horas = total_minutos / 60
  conta = float(10 * 0.3)
  if total_minutos >= 11:
    conta_final = ((total_minutos - 10) * 0.05) + conta
    result = '''Tempo de chamada: 
    {} minutos;
    {:.2f} horas;

    Valor da Tarifa:
    R$ {}'''.format(total_minutos , total_horas , conta_final)
  elif total_minutos < 11:
    conta_final = total_minutos * 0.3
    result = '''Tempo de chamada: 
    {} minutos;
    {:.2f} horas;

    Valor da Tarifa:
    R$ {:.2f}'''.format(total_minutos , total_horas , conta_final)
  return result

def ex_7(a):
  total_macas = a
  preco_normal = 0.80
  preco_promocao = 0.70
  if total_macas >= 12:
    total = a * preco_promocao
    titulo('TOTAL DA COMPRA')
    result = '{} MAÇÃS | R$ {:.2f}'.format(total_macas , total)
    
  elif total_macas < 12:
    total = total_macas * preco_normal
    titulo('TOTAL DA COMPRA')
    result = '{} MAÇÃS | R$ {:.2f}'.format(total_macas , total)
  return result
    

def ex_8(a , b , c , d):
    p1 = a % 2
    p2 = b % 2
    p3 = c % 2
    p4 = d % 2
    soma = 0
    if p1 == 0:
      soma += a
    if p2 == 0:
      soma += b
    if p3 == 0:
      soma += c
    if p4 == 0:
      soma += d      
    result = 'A soma dos números pares é: {}'.format(soma)
    return result

def ex_9(a , b):
  tip_bilhete = a
  dinheiro = b
  if tip_bilhete == 1:
    quantidade_bilhete = math.floor(dinheiro / 1.30)
    valor_total_bilhete = float(quantidade_bilhete * 1.30)
    troco = dinheiro - valor_total_bilhete
    result = '''
    Dinheiro depositado: R$ {}
    Valor total: R$ {}
    Quantidade de Bilhetes: {}
    Troco: R$ {}'''.format(dinheiro , valor_total_bilhete , quantidade_bilhete , troco)
  elif tip_bilhete == 2:
    quantidade_bilhete = math.floor(dinheiro / 2.60)
    valor_total_bilhete = float(quantidade_bilhete * 2.60)
    troco = dinheiro - valor_total_bilhete
    result = '''
    Dinheiro depositado: R$ {}
    Valor total: R$ {}
    Quantidade de Bilhetes: {}
    Troco: R$ {}'''.format(dinheiro , valor_total_bilhete , quantidade_bilhete , troco)
  elif tip_bilhete == 3:
    quantidade_bilhete = math.floor(dinheiro / 12)
    valor_total_bilhete = float(quantidade_bilhete * 12)
    troco = dinheiro - valor_total_bilhete
    result = '''
    Dinheiro depositado: R$ {}
    Valor total: R$ {}
    Quantidade de Bilhetes: {}
    Troco: R$ {}'''.format(dinheiro , valor_total_bilhete , quantidade_bilhete , troco)
  return result

def ex_10(a):
  salario = a
  if salario < 800:
    reajuste = salario * 1.10
    result = ''' Salário Antigo: R$ {}
    Reajuste: 10 %
    Salário Atual: R$ {}'''.format(salario , reajuste)
  elif salario > 800 and salario < 1500:
    reajuste = salario * 1.075
    result = ''' Salário Antigo: R$ {}
    Reajuste: 7,5 %
    Salário Atual: R$ {}'''.format(salario , reajuste)
  elif salario > 1500:
    reajuste = salario * 1.05
    result = ''' Salário Antigo: R$ {}
    Reajuste: 5 %
    Salário Atual: R$ {}'''.format(salario , reajuste)
  return result

def ex_11(a):
  nome = a
  meu_nome = 'Luiz'
  if nome == meu_nome:
    result = 'Você é meu xará'
  else: 
    result = 'Você infelizmente não é meu xará'
  return result

def ex_12(a):
  idade = a
  if idade >= 5 and idade <= 7:
    result = 'Você está classificado na categoria: {}'.format('Infantil A')
  if idade >= 8 and idade <= 10:
    result = 'Você está classificado na categoria: {}'.format('Infantil B')   
  if idade >= 11 and idade <= 13:
    result = 'Você está classificado na categoria: {}'.format('Juvenil A')   
  if idade >= 14 and idade <= 17:
    result = 'Você está classificado na categoria: {}'.format('Juvenil B')    
  if idade >= 18:
    result = 'Você está classificado na categoria: {}'.format('Adulto')
  return result
    

def ex_13(a , b , c):
  if a > b and a > c:
    result = 'O maior número entre {} , {} e {} é: {}'.format(a , b , c , a)
  elif b > a and b > c:
    result = 'O maior número entre {} , {} e {} é: {}'.format(a , b , c , b)
  elif c > a and c > b:
    result = 'O maior número entre {} , {} e {} é: {}'.format(a , b , c , c)
  elif b == a == c:
    result = 'Todos os números são iguais'
  return result

def ex_14(a):
  num = a
  result = num % 2
  if result == 1 and num < 10:
    ex = 'Número {} é ímpar e menor que 10'.format(num)
  elif result == 0 and num < 10:
    ex = 'Número {} é par e menor que 10'.format(num)
  else: 
    ex = 'Número fora do intervalo'
  return ex

def ex_15(a):
  salario = a
  if salario < 500:
    reajuste = salario * 1.15
    result = '''Salário antigo: R$ {} \nReajuste: 15% \nSalário Atual: R$ {:.2f}'''.format(salario , reajuste)
  if salario >= 500 and salario <= 1000:
    reajuste = salario * 1.10
    result = '''Salário antigo: R$ {} \nReajuste: 10% \nSalário Atual: R$ {:.2f}'''.format(salario , reajuste)
  if salario > 1000:
    reajuste = salario * 1.05
    result = '''Salário antigo: R$ {} \nReajuste: 5% \nSalário Atual: R$ {:.2f}'''.format(salario , reajuste)
  return result

def ex_16(a , b , c):
  nome = a
  salario_bruto = b
  dependentes = c
  if salario_bruto <= 300:
    salario_liquido = (salario_bruto * 0.92) + (15 * dependentes) + 40 + 100
    result = '''Nome do Funcionário: {} \nSalário Líquido: R$ {}'''.format(nome , salario_liquido)
  if salario_bruto >= 301 and salario_bruto <= 700:
    salario_liquido = (salario_bruto * 0.91) + (15 * dependentes) + 40 + 100
    result = '''Nome do Funcionário: {} \nSalário Líquido: R$ {}'''.format(nome , salario_liquido)
  if salario_bruto >= 700:
    salario_liquido = (salario_bruto * 0.90) + (15 * dependentes) + 40 + 100
    result = '''Nome do Funcionário: {} \nSalário Líquido: R$ {}'''.format(nome , salario_liquido)
  return result 

def ex_17(a , b):
  nome = a
  batimento = b
  if batimento >= 40 and batimento <= 59:
    result = 'Seu batimento está baixo. Faça alguma atividade física.'
  if batimento >= 60 and batimento <= 70:
    result = 'Seu batimento está normal. Aprecie a vida.'
  if batimento >= 71 and batimento <= 100:
    result = 'Seu batimento está acelerado. Semana que vem é prova de algoritmos!'
  if batimento >= 120:
    result = 'Seu batimento está ligado no 220W. To fazendo prova!!! ;---; :( '
  if batimento == 0:
    result = 'Deve ter morrido, saiu o resultado das notas!'
  return result 

def ex_18(a , b , c , d):
  espirro = a
  coriza = b
  dor_cabeca = c
  temperatura = d
  if espirro == 'Sim' and coriza == 'Sim' and dor_cabeca == 'Sim' and temperatura > 37 or temperatura < 36.5:
    result = 'Seu diagnóstico diz que é pneumonia.'
  elif coriza == 'Sim' and espirro == 'Sim' and dor_cabeca == 'Não' and temperatura >= 36.5 and temperatura <= 37:
    result = 'Seu diagnóstico diz que é resfriado.'
  elif coriza == 'Sim' and espirro == 'Sim' and dor_cabeca == 'Sim' and temperatura >= 36.5 and temperatura <= 37:
    result = 'Seu diagnóstico diz que é bronquite.'
  elif espirro == 'Sim' or coriza == 'Sim' or dor_cabeca  == 'Sim' or temperatura > 37 or temperatura < 36.5:
    result = 'Seu diagnóstico diz que é gripe.'
  else:
    result = 'Não sei o que é mano. ¯\_(ツ)_/¯'
  return result

def ex_19(a , b):
  velocidade_motorista = a 
  velocidade_permetida = b
  conta = velocidade_motorista - velocidade_permetida
  if conta >= 1 and conta <= 10:
    result = '''O motorista estava a {} Km/h, \nacima da velocidade permitida {} Km/h. \nIrá pagar uma multa de R$ 50 '''.format(velocidade_motorista , velocidade_permetida)
  elif conta >= 11 and conta <= 30:
    result = '''O motorista estava a {} Km/h, \nacima da velocidade permitida {} Km/h. \nIrá pagar uma multa de R$ 100 '''.format(velocidade_motorista , velocidade_permetida)
  elif conta >= 31:
    result = '''O motorista estava a {} Km/h, \nacima da velocidade permitida {} Km/h. \nIrá pagar uma multa de R$ 200 '''.format(velocidade_motorista , velocidade_permetida)
  else:
    result = '''O motorista estava de acordo \ncom as normas de trânsito.'''
  return result

def ex_20(a , b):
  tip = a
  quantidade_litros = b
  if tip == 'A' and quantidade_litros <= 20:
    preco_alcool = 2 * 0.97
    result = preco_alcool * quantidade_litros
    result_final = '''{} litros de Álcool deu R$ {}.
    Pode pagar lá no caixa mesmo.'''.format(quantidade_litros , result)
  elif tip == 'A' and quantidade_litros > 20:
    preco_alcool = 2 * 0.95
    result = preco_alcool * quantidade_litros
    result_final = '''{} litros de Álcool deu R$ {}.
    Pode pagar lá no caixa.'''.format(quantidade_litros , result)
  elif tip == 'G' and quantidade_litros <= 20:
    preco_gasolina = 3.15 * 0.96
    result = preco_gasolina * quantidade_litros
    result_final = '''{} litros de Gasolina deu R$ {:.2f}.
    Pode pagar lá no caixa.'''.format(quantidade_litros , result)
  elif tip == 'G' and quantidade_litros > 20:
    preco_gasolina = 3.15 * 0.94
    result = preco_gasolina * quantidade_litros
    result_final = '''{} litros de Gasolina deu R$ {:.2f}.
    Pode pagar lá no caixa.'''.format(quantidade_litros , result)
  return result_final 

def ex_21(a , b , c , d , e , f):
  p1 = a
  p2 = b
  p3 = c
  l1 = d
  l2 = e
  l3 = f
  media_prova = (p1 + p2 + p3) / 3
  media_lista = (l1 + l2 + l3) / 3
  media_aproveitamento = (media_prova + media_lista) / 2
  if media_aproveitamento >= 9:
    result = 'Sua média foi {}. Conceito A: APROVADO'.format(media_aproveitamento)
  elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:
    result = 'Sua média foi {}. Conceito B: APROVADO'.format(media_aproveitamento)
  elif media_aproveitamento >= 6 and media_aproveitamento < 7.5:
    result = 'Sua média foi {}. Conceito C: APROVADO'.format(media_aproveitamento)
  elif media_aproveitamento >= 4 and media_aproveitamento < 6:
    result = 'Sua média foi {}. Conceito D: REPROVADO'.format(media_aproveitamento)
  elif media_aproveitamento < 4:
    result = 'Sua média foi {}. Conceito E: REPROVADO'.format(media_aproveitamento)
  return result

def ex_22(a , b , c , d , e , f):
  aulas_ano = a
  presenca = b
  nt1 = c
  nt2 = d
  nt3 = e
  nt4 = f
  total_faltas = aulas_ano - presenca
  presenca_total = aulas_ano * 0.25
  media = (nt1 + nt2 + nt3 + nt4) / 4
  if media >= 7 and total_faltas <= presenca_total:
    result = '''Média: {} \nSituação: APROVADO'''.format(media)
  else: 
    result = '''Média: {} \nSituação: REPROVADO'''.format(media) 
  return result

def ex_23(a , b):
  cliente = a
  saldo_medio = b
  if saldo_medio <= 200:
    result = '''Saldo Médio: R$ {} \n{}, infelizmente você não tem crédito especial.'''.format(saldo_medio , cliente)
  elif saldo_medio >= 201 and saldo_medio <= 400:
    credito = saldo_medio * 0.2
    result = '''Saldo Médio: R$ {} \n{}, parabéns você possui crédito especial. \nValor: R$ {:.2f}'''.format(saldo_medio , cliente , credito)
  elif saldo_medio >= 401 and saldo_medio <= 600:
    credito = saldo_medio * 0.3
    result = '''Saldo Médio: R$ {} \n{}, parabéns você possui crédito especial. \nValor: R$ {:.2f}'''.format(saldo_medio , cliente , credito)
  elif saldo_medio >= 601:
    credito = saldo_medio * 0.4
    result = '''Saldo Médio: R$ {} \n{}, parabéns você possui crédito especial. \nValor: R$ {:.2f}'''.format(saldo_medio , cliente , credito)
  return result

def ex_24(a):
  conta = a
  if conta > 99999 or conta < 11111:
    result = '{:^30}'.format('NÚMERO DE CONTA INVÁLIDO')
    return result
  c1 = conta // 1 % 10
  c2 = conta // 10 % 10
  c3 = conta // 100 % 10
  c4 = conta // 1000 % 10
  c5 = conta // 10000 % 10
  verificador = c1 + c2 + c3 + c4 + c5
  v1 = verificador // 1 % 10
  v2 = verificador // 10 % 10
  soma = v1 + v2
  s1 = soma // 1 % 10
  s2 = soma // 10 % 10
  soma2 = s1 + s2
  if verificador < 10:   
    result = 'Número de conta corrente é: {}-{}'.format(conta , verificador)
  elif verificador >= 10 and soma < 10:
    result = 'Número de conta corrente é: {}-{}'.format(conta , soma)
  elif verificador >= 10 and soma2 < 10:
    result = 'Número de conta corrente é: {}-{}'.format(conta , soma2)
  return result

def ex_25(a , b):
  opc = a
  metros_cub = b
  dif_comercial = metros_cub - 80
  dif_industrial = metros_cub - 100 
  residencial = 5 + (0.55 * metros_cub)
  comercial = 120 + (0.55 * metros_cub)
  comercial_ad = 0.85 * dif_comercial
  industrial = 450 + (0.55 * metros_cub)
  industrial_ad = 1.25 * dif_industrial
  total_com = comercial_ad + comercial
  total_ind = industrial_ad + industrial
  if opc == 1:
    result = '''
    CONTA DE ÁGUA

    Infraestrutura: Residencial
    Consumo de água: {} m3

    Conta a pagar: R$ {:.2f}'''.format(metros_cub , residencial)
  elif opc == 2 and metros_cub < 80:
    result = '''
    CONTA DE ÁGUA

    Infraestrutura: Comercial
    Consumo de água: {} m3

    Conta a pagar: R$ {:.2f}'''.format(metros_cub , comercial)
  elif opc == 3 and metros_cub < 100:
    result = '''
    CONTA DE ÁGUA

    Infraestrutura: Comercial
    Consumo de água: {} m3

    Conta a pagar: R$ {:.2f}'''.format(metros_cub , industrial)
  elif opc == 2 and metros_cub > 80:
    comercial = 120 + (0.55 * 80)
    total_com = comercial_ad + comercial
    result = '''
    CONTA DE ÁGUA

    Infraestrutura: Comercial
    Consumo de água: {} m3

    Conta a pagar: R$ {:.2f}'''.format(metros_cub , total_com)
  elif opc == 3 and metros_cub > 100:
    industrial = 450 + (0.55 * 100)
    total_ind = industrial_ad + industrial
    result = '''
    CONTA DE ÁGUA

    Infraestrutura: Comercial
    Consumo de água: {} m3

    Conta a pagar: R$ {:.2f}'''.format(metros_cub , total_ind)
  return result
#Exercício 1
def main():
  titulo('ELEVADOR HOTEL')
  peso_maximo = int(input('Peso máximo do elevador: KG '))
  print('=' * 30)
  p1 = float(input('Defina o peso da Pessoa 1: KG '))
  p2 = float(input('Defina o peso da Pessoa 2: KG '))
  p3 = float(input('Defina o peso da Pessoa 3: KG '))
  p4 = float(input('Defina o peso da Pessoa 4: KG '))
  p5 = float(input('Defina o peso da Pessoa 5: KG '))
  result = ex_1(peso_maximo , p1 , p2 , p3 , p4 , p5)
  print(result)
#Exercício 2
def main():
  titulo('NÚMERO DIVISOR')
  num = int(input('Defina seu número: '))
  result = ex_2(num)
  print(result)
#Exercício 3
def main():
  titulo('MÉDIA DO ALUNO')
  print('Bem vindo Professor')
  print('=' * 30)
  print('Notas de Provas: 0 - 10')
  print('=' * 30)
  print('Aluno Josefino:')
  nt1 = float(input('Nota 1° Prova: '))
  nt2 = float(input('Nota 2° Prova: '))
  nt3 = float(input('Nota 3° Prova: '))
  nt4 = float(input('Nota 4° Prova: '))
  result = ex_3(nt1 , nt2 , nt3 , nt4)
  print(result)
#Exercício 4
def main():
  titulo('DIFERENÇA VALOR')
  print('Apresentar 60% da diferença do maior pelo menor valor')
  print('=' * 30)
  n1 = int(input('Digite o primeiro número: '))
  n2 = int(input('Digite o segundo número: '))
  result = ex_4(n1 , n2)
  print(result)
#Exercício 5
def main():
  titulo('NÚMERO MAIOR OU IGUAL')
  print('Digite dois números, e irei verificar qual o maior ou se são iguais')
  print('=' * 30)
  n1 = int(input('Digite o primeiro número: '))
  n2 = int(input('Digite o segundo número: '))
  result = ex_5(n1 , n2)
  print(result)
#Exercício 6
def main():
  titulo('TELEFONIA')
  print('''TARIFA TELEFÔNICA:

  Preço por minuto = R$ 0,30 – para os 10 primeiros minutos;

  11º minuto e seguintes cobrados = R$ 0,05 por minuto;
  ''')
  print('=' * 30)
  total_minutos = float(input('Total de minutos em chamada: '))
  result = ex_6(total_minutos)
  print(result)
#Exercício 7
def main():
  titulo('FEIRA DO SEU JOÃO')
  print('''PROMOÇÃO DE HOJE:

  ACIMA DE 12 MAÇÃS: R$ 0,70 c/d
  PREÇO NORMAL DA MAÇÃ: R$ 0,80 c/d
  ''')
  print('=' * 30)
  quantidade = int(input('Quanto deseja levar? '))
  result = ex_7(quantidade)
  print(result)
#Exercício 8
def main():
  titulo('SOMA DOS NÚMEROS PARES')
  n1 = int(input('Defina o 1° número: '))
  n2 = int(input('Defina o 2° número: '))
  n3 = int(input('Defina o 3° número: '))
  n4 = int(input('Defina o 4° número: '))
  result = ex_8(n1 , n2 , n3 , n4)
  print(result)
#Exercício 9
def main():
  titulo('BILHETERIA METRÔ')
  print(''' OPÇÕES DE BILHETES:
  [ 1 ] Bilhete Unitário..............R$ 1,30
  [ 2 ] Bilhete duplo.................R$ 2,60
  [ 3 ] Bilhete 10 viagens...........R$ 12,00
  ''')
  tip_bilhete = int(input('Qual opção de bilhete deseja escolher? '))
  dinheiro = float(input('Deposite a quantidade de dinheiro: R$ '))
  result = ex_9(tip_bilhete , dinheiro)
  print(result)
#Exercício 10
def main():
  titulo('CALCÚLO DE SALÁRIO')
  salario_atual = float(input('Defina seu salário atual: R$ '))
  result = ex_10(salario_atual)
  print(result)
#Exercício 11
def main():
  titulo('VOCÊ É MEU XARÁ?') 
  nome = input('Digite seu nome: ')
  result = ex_11(nome)
  print(result)
#Exercício 12
def main():
  titulo('CATEGORIAS DE NADADOR')
  print('''
  Categoria: Infantil A | Idade: 5-7 anos
  Categoria: Infantil B | Idade: 8-10 anos
  Categoria: Juvenil A  | Idade: 11-13 anos
  Categoria: Juvenil B  | Idade: 14-17 anos
  Categoria: Adulto     | Idade: Maior/Igual 18 anos''')
  print('=' * 30)
  idade = int(input('Digite sua idade: '))
  print('=' * 30)
  result = ex_12(idade)
  print(result)
#Exercício 13 
def main():
  titulo('QUAL O MAIOR VALOR?')
  a = int(input('Digite 1° número: '))
  b = int(input('Digite 2° número: '))
  c = int(input('Digite 3° número: '))
  print('=' * 30)
  result = ex_13(a , b , c)
  print(result)
#Exercício 14
def main():
  titulo('NUMERO QUALQUER')
  num = int(input('Defina um número: '))
  result = ex_14(num)
  print(result)
#Exercício 15
def exercicio_15():
  titulo('REAJUSTE DE SALÁRIO')
  salario = float(input('Defina o salário do funcionário: R$ '))
  result = ex_15(salario)
  print('=' * 30)
  print(result)
  print('=' * 30)
#Exercício 16
def main():
  titulo('CALCÚLO DO SALÁRIO')
  print('Informções do Funcionário')
  print('=' * 30)
  nome = input('Nome: ')
  salario_bruto = float(input('Salário Bruto: R$ '))
  dependentes = int(input('N° Dependentes: '))
  titulo('Cálculo de Salário Líquido')
  result = ex_16(nome , salario_bruto , dependentes)
  print(result)
#Exercício 17 
def main():
  titulo('CONDICIONAMENTO FISÍCO')
  print('Informações do Paciente')
  nome = input('Nome: ')
  batimento = int(input('Defina seu batimento do coração por minuto: '))
  result = ex_17(nome , batimento)
  print('=' * 30)
  print(result)
  print('=' * 30)
#Exercício 18
def main():
  titulo('ANÁLISE MÉDICA')
  paciente = input('Seu nome: ')
  print('=' * 30)
  print('Responda com Sim ou Não')
  print('=' * 30)
  espirro = input('Tem espirros? ')
  coriza = input('Tem coriza? ')
  dor_cabeca = input('Tem dor de cabeça? ')
  temperatura = float(input('Temperatura? '))
  print('=' * 30)
  result = ex_18(espirro , coriza , dor_cabeca , temperatura)
  print(result)
  print('=' * 30)
#Exercício 19
def main():
  titulo('RADAR MÓVEL')
  velocidade_motorista = int(input('Velocidade do motorista: Km/h '))
  velocidade_permetida = int(input('Velocidade permetida da avenida: Km/h '))
  print('=' * 30)
  result = ex_19(velocidade_motorista , velocidade_permetida)
  print(result)
  print('=' * 30)
#Exercício 20
def main():
  titulo('POSTO DE GASOSA')
  print('''Álcool: 
  *Até 20 litros, desconto de 3% por litro;
  *Acima de 20 litros, desconto de 5% por litro;\n=============================================== \nGasolina: 
  *Até 20 litros, desconto de 4% por litros;
  *Acima de 20 litros, desconto de 6% por litro;''')
  print('=' * 47)
  tip = input('''O que vai ser hoje chefia? 
  A = álcool
  G = gasolina
  Qual? ''')
  quantidade_litros = float(input('Quantos litros? '))
  print('=' * 30)
  result = ex_20(tip , quantidade_litros)
  print(result)
  print('=' * 30)
#Exercício 21
def main(): 
  titulo('MÉDIA DE APROVEITAMENTO')
  ra = int(input('Seu RA: '))
  nome_aluno = input('Seu nome: ')
  print('=' * 30)
  print('''BEM VINDO \nAluno: {} \nRA: {}'''.format(nome_aluno , ra))
  titulo('NOTAS DE PROVA: 0 - 10')
  p1 = float(input('Nota da 1° Prova: ')) 
  p2 = float(input('Nota da 2° Prova: '))
  p3 = float(input('Nota da 3° Prova: '))
  titulo('NOTAS DE LISTA: 0 - 10')
  l1 = float(input('Nota da 1° lista ex:  '))
  l2 = float(input('Nota da 2° lista ex:  '))
  l3 = float(input('Nota da 3° lista ex:  '))
  result = ex_21(p1 , p2 , p3 , l1 , l2 , l3)
  print(result)
#Exercício 22
def main():
  titulo('SITUAÇÃO FINAL')
  aluno = input('Nome: ')
  disc = input('Nome da Disciplina: ')
  print('=' * 30)
  aulas_ano = int(input('Quantidade de aulas no ano: '))
  presenca = int(input('Quantidade de presenças: '))
  titulo('NOTAS BIMESTRAIS: 0 - 10')
  nt1 = float(input('Nota 1° Bimestre: '))
  nt2 = float(input('Nota 2° Bimestre: '))
  nt3 = float(input('Nota 3° Bimestre: '))
  nt4 = float(input('Nota 4° Bimestre: '))
  result = ex_22(aulas_ano , presenca , nt1 , nt2 , nt3 , nt4)
  print('=' * 30)
  print(result)
  print('=' * 30)
#Exercício 23
def main():
  titulo('CRÉDITO ESPECIAL ANO NOVO')
  cliente = input('Seu nome: ')
  saldo_medio = float(input('Informe seu Saldo Médio do Último Ano: R$ '))
  result = ex_23(cliente , saldo_medio)
  print('=' * 30)
  print(result)
  print('=' * 30)
#Exercício 24
def main():
  titulo('CONTA CORRENTE')
  conta = int(input('Digite o N° da c/c: '))
  result = ex_24(conta)
  print('=' * 30)
  print(result)
  print('=' * 30)
#Exercício 25
def main():
  titulo('CONTA DE ÁGUA')
  print('''  [ 1 ] Residencial
  [ 2 ] Comercial
  [ 3 ] Industrial''')
  print('=' * 30)
  opc = int(input('Tipo da infraestrutura:  '))
  print('=' * 30)
  metros_cub = int(input('Quantidade de água em m3: '))
  print('=' * 30)
  result = ex_25(opc , metros_cub)
  print(result)
  print('=' * 30)
