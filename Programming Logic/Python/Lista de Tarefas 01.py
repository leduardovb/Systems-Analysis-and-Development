'''

Luiz Eduardo Vieira Barreto
1° Período TADS
10/03/2020

'''

PI = 3.14

#Definindo as funções#
def area_triangulo_retangulo(base , altura):
  area = (base * altura) / 2
  return area

def area_circulo(raio):
  area = PI * (raio ** 2)
  return area

def quantidade_chuva(d1 , d2 , d3 , d4 , d5 , d6):
  conv = (d1 + d2 + d3 + d4 + d5 + d6) * 25.4
  return conv

def desconto_valor(valor):
  desconto = valor * 0.905
  return desconto

def total_do_bolo(p1 , p2 , p3 , p4 , p5):
  total = (p1 * 0.33) + (p2 * 0.5) + (p3 * 0.2) + (p4 * 2) + (p5 * 1.5)
  return total

def desconto_produto(produto):
  desconto = produto * 0.9
  return desconto

def area_livre_terreno(a , b):
  area_livre = a - b
  return area_livre

def exercicio_salario(a):
  ope = a * 0.924
  return ope

def desconto_do_produto(a):
  desconto = a - 0.095
  return desconto

def altura_predio(a , b , c):
  altura = a * (b / c)
  return altura 

def media_aproveitamento(a , b , c , d):
  media = (a + (b * 2) + (c * 3) + d) / 7
  return media

def exer_7(a):
  desconto_10 = a * 0.9
  return desconto_10

def exer_8(a , b , c):
  percentual_vendas = a
  total_vendas = b
  salario_fixo = c
  porc = percentual_vendas / 100
  salario_total = float(900 + (total_vendas * porc))
  result = '''
  Dados sobre o vendedor João:
  Salário Fixo: {} R$
  Total de vendas: {} R$
  Comissão: {} %
  
  Sálario total do mês: {} R$ '''.format(salario_fixo , total_vendas , percentual_vendas , salario_total)
  return result 

def exer_9(a , b , c , d):
  base_retangulo = a
  altura_retangulo = b 
  comprimento_casa = c
  largura_casa = d
  terreno = base_retangulo * altura_retangulo
  casa = comprimento_casa * largura_casa
  area_livre = terreno - casa
  porce = float((area_livre / terreno) * 100)
  result = 'A área livre do terreno é {} mts e sua porcentagem é {:.2f} %'.format(area_livre , porce)
  return result

def exer_10(a , b , c):
  deposito = a
  cheque1 = b
  cheque2 = c
  saldo_final = (deposito * 0.9924) - (cheque1 + cheque2)
  return saldo_final

def exer_11(a):
  valor = a
  nt100 = valor // 100
  valor %= 100
  nt50 = valor // 50
  valor %= 50
  nt20 = valor // 20
  valor %= 20
  nt10 = valor // 10
  valor %= 10
  nt5 = valor // 5
  valor %= 5
  nt2 = valor // 2
  valor %= 2
  nt1 = valor // 1
  result = '''QUANTIDADE DE NOTAS:
  [100 R$] {}
  [50 R$]  {}
  [20 R$]  {}
  [10 R$]  {}
  [5 R$]   {}
  [2 R$]   {}
  [1 R$]   {}'''.format(nt100 , nt50 , nt20 , nt10 , nt5 , nt2 , nt1)
  return result 

def exer_12(a , b):
  horas = a
  salario = b
  valor_horas = float(0.04 * salario)
  salario_bruto = horas * valor_horas
  imposto = salario_bruto * 0.03
  salario_receber = salario_bruto - imposto
  return salario_receber

def exer_13(a):
  salario_atual = a
  porcentagem = salario_atual * 0.05
  salario_reajustado = salario_atual + porcentagem
  result = '''  Salário Mensal Atual: R$ {}
  Salário Mensal com o reajuste de 5%: R$ {}'''.format(salario_atual , salario_reajustado)
  return result

def exer_14():
  total_litros = float(520 / 12)
  total_gasto =  float(total_litros * 3.75)
  result = 'Para chegar a casa de sua irmã, Maria terá que colocar {:.2f} litros de gasolina. Dando um total de {} R$'.format(total_litros , total_gasto)
  return result

def exer_15(a):
  total_alunos = a
  quant_masc = total_alunos * 0.4
  quant_fem = total_alunos * 0.6
  maior_masc = quant_masc * 0.8
  maior_fem = quant_fem * 0.2
  result = '''Sala A:
  Total alunos: {}
  Quantidade Masculina: {:.2f} alunos 
  Quantidade Feminina: {:.2f} alunos

  Maiores de Idade:
  Quantidade Mascilina: {:.2f} alunos
  Quantidade Feminina: {:.2f} alunos'''.format(total_alunos ,quant_masc , quant_fem , maior_masc , maior_fem)
  return result

def exer_16(a , b , c , d , e):
  total_cidadao = a
  total_eleitores = b
  votos_brancos = c
  votos_nulos = d
  nao_votaram = e
  votos_validos = total_eleitores - (votos_brancos + votos_nulos + nao_votaram)
  per1 = (votos_brancos / total_eleitores) * 100
  per2 = (votos_validos / total_eleitores) * 100  
  per3 = (votos_nulos / total_eleitores) * 100
  per4 = (nao_votaram / total_eleitores) * 100
  result = '''Situação da Eleição:
  
  Total de cidadãos: {}
  Total de eleitores: {}

  Quantidade de votos:

  Votos brancos: {}; {:.2f} %
  Votos válidos: {}; {:.2f} %
  Votos nulos: {}; {:.2f} %
  Não votaram: {}; {:.2f} %'''.format(total_cidadao , total_eleitores , votos_brancos , per1 , votos_validos , per2 , votos_nulos , per3 , nao_votaram , per4)
  return result

def exer_17(a):
  valor_compra = a
  compra_vista = valor_compra * 0.9
  compra_prazo = valor_compra * 1.05
  result = ''' 
  Valor a vista: {:.2f}
  Valor a prazo: 3 parcelas de {:.2f}'''.format(compra_vista , compra_prazo)
  return result

def exer_18(a , b , c , d):
  salario = a 
  anos_servico = b 
  posicao = c 
  n_filhos = d
  ad_5_anos = ((anos_servico // 5) * 0.05) * salario
  ad_ano_de_trabalho = (anos_servico * 0.01) * salario
  ad_numero_filhos = (n_filhos * 0.03) * salario
  result = (ad_5_anos + ad_ano_de_trabalho + ad_numero_filhos + salario) 
  result1 = '''Funcionário José:

  Posição: {}
  Salário: R$ {} 
  Anos Trabalhado: {}
  N° de filhos: {}
  Salário reajustado: R$ {:.2f}'''.format(posicao , salario , anos_servico , n_filhos , result)
  return result1 

def exer_19(a , b , c , d , e , f , g , h , i):
  farinha = a
  agua = b
  fermento = c
  p1 = d
  p2 = e
  p3 = f
  energia = g
  imposto = h
  p4 = i
  preco_farinha = farinha * p1
  preco_agua = agua * p2
  preco_fermento = fermento * p3
  preco_energia = energia * p4
  total = (preco_farinha + preco_agua + preco_fermento + preco_energia) * (imposto / 100)
  preco_custo = total / 100
  preco_venda = preco_custo * 1.3
  result = '''
  INGREDIENTE     |  PREÇO     
  ==============================
  FARINHA {} KG    R$ {}   
  ÁGUA {} LT       R$ {}    
  FERMENTO {} G    R$ {}   
  ==============================

  CUSTO PADRÃO    | PREÇO   
  ==============================
  ENERGIA {} kW    R$ {}    
  IMPOSTO {} %     
  
  PREÇO TOTAL: R$ {:.2f}
  
  PREÇO CUSTO: R$ {:.2f}
  PREÇO VENDA: R$ {:.2f}'''.format(farinha , preco_farinha , agua , preco_agua , fermento , preco_fermento , energia , preco_energia , imposto , total , preco_custo , preco_venda)
  return result 

def exer_23(a):
  valor = a
  nt50 = valor // 50
  valor %= 50
  nt10 = valor // 10
  valor %= 10
  nt5 = valor // 5
  valor %= 5
  nt2 = valor // 2
  result = '''
  {} NOTAS R$ 50 
  {} NOTAS R$ 10
  {} NOTAS R$ 5
  {} NOTAS R$ 2'''.format(nt50 , nt10 , nt5 , nt2)
  return result

def exer_22(a):
  valor_arrecadado = a
  sena = valor_arrecadado * 0.35
  quina = valor_arrecadado * 0.19
  quadra = valor_arrecadado * 0.12
  result = '''Agora os ganhadores da Mega-Sena:
  Sena: Dona Maria-SP {} R$
  Quina: Seu José-ES {} R$
  Quadra: Dona Vilma-RJ {} R$'''.format(sena , quina , quadra)
  return result

def exer_21(a):
  valor = a
  nt50 = valor // 50
  valor %= 50
  nt10 = valor // 10
  valor %= 10
  nt5 = valor // 5
  valor %= 5
  nt2 = valor // 2
  result = '''
  {} NOTAS B$ 50 
  {} NOTAS B$ 10
  {} NOTAS B$ 5
  {} NOTAS B$ 2'''.format(nt50 , nt10 , nt5 , nt2)
  return result

def exer_20(a , b):
  diaria_normal = a
  lotacao = b
  diaria_promocional = diaria_normal * 0.75
  valor_total_promocional = diaria_promocional * (lotacao * 0.8)
  valor_total_normal = diaria_normal * (lotacao * 0.5)
  quartos_normal = lotacao * 0.5
  quartos_promo = lotacao * 0.8
  result1 = '''  TOTAL DE QUARTOS: {}
  DIÁRIA NORMAL: {} R$
  DIÁRIA PROMOCIONAL: {} R$
  
  VALOR TOTAL DIÁRIA NORMAL: {} R$
  OCUPAÇÃO TOTAL: {} QUARTOS
  =====================================
  VALOR TOTAL DIÁRIA PROMOCIONAL: {} R$
  OCUPAÇÃO TOTAL: {} QUARTOS
  '''.format(lotacao , diaria_normal , diaria_promocional , valor_total_normal , quartos_normal , valor_total_promocional , quartos_promo)
  return result1 

def exer_20_1(a , b):
  diaria_normal = a
  lotacao = b
  diaria_promocional = diaria_normal * 0.75
  valor_total_promocional = diaria_promocional * (lotacao * 0.8)
  valor_total_normal = diaria_normal * (lotacao * 0.5)
  if valor_total_normal > valor_total_promocional:
    result = 'A opção mais rentável é a diária normal'
  else:
    result = 'A opção mais rentável é a diária promocional'
  return result

def main():
  def exercicio_1():
    print('=' * 30)
    nome = input('Nome: ')
    endereco = input('Endereço: ')
    telefone = input('Telefone: ')
    print('=' * 30)
    print('''    Nome: {} 
    Endereço: {} 
    Telefone: {}'''.format(nome , endereco , telefone))
    print('=' * 30)

  def exercicio_2():
    print('=' * 30) 
    print('{:^30}'.format('Área do Triângulo Retângulo: '))
    print('=' * 30)
    base = float(input('Defina a base do Triângulo: '))
    altura = float(input('Defina altura do Triângulo: '))    
    result = area_triangulo_retangulo(base , altura)
    print('A área do triângulo é {}'.format(result))
    print('=' * 30) 

  def exercicio_3():
    print('=' * 30)
    print('{:^30}'.format('Área do Circúlo:'))
    print('=' * 30)
    raio = float(input('Defina o raio do circúlo: '))
    result = area_circulo(raio)
    print('A área do circúlo é {}'.format(result))
    print('=' * 30) 

  def exercicio_4():
    print('=' * 30)
    print('{:^30}'.format('Quantidade de chuva em mm: '))
    print('=' * 30)
    d1 = int(input('Segunda: '))
    d2 = int(input('Terça: '))
    d3 = int(input('Quarta: '))
    d4 = int(input('Quinta: ')) 
    d5 = int(input('Sexta: '))
    d6 = int(input('Sábado: '))
    result = quantidade_chuva(d1 , d2 , d3 , d4 , d5 , d6)
    print('A quantidade que choveu na semana foi {} mm'.format(result))
    print('=' * 30) 

  def exercicio_5():
    print('=' * 30)
    print('Produto com desconto de 9,5%')
    print('=' * 30)
    produto = int(input('Digite o valor do produto: R$ '))
    result = desconto_do_produto(produto)
    print('''
    O valor inicial: {}
    Desconto: 9,5%
    Valor final {}'''.format(produto , result))
    print('=' * 30)
     
  def exercicio_6():
    print('=' * 30)
    print('{:^30}'.format('Calculo do Bolo: '))
    print('=' * 30)
    ovo = float(input('Valor da duzia de Ovos: R$ '))
    farinha = float(input('Valor do kg da Farinha: R$ '))
    acucar = float(input('Valor do kg Açúcar: R$ '))
    creme_leite = float(input('Valor da lata de Creme de Leite: R$ '))
    leite = float(input('Valor do litro de Leite: R$ '))
    result = total_do_bolo(ovo , farinha , acucar , creme_leite , leite)
    print('O valor total dos ingredientes {:.2f} R$'.format(result))
    print('=' * 30) 
  
  def exercicio_7():
    print('=' * 30)
    print('{:^30}'.format('Desconto de 10%: '))
    print('=' * 30)
    num = int(input('Defina seu número: '))
    result = exer_7(num)
    print(''' Valor inicial {} R$
    Desconto {} %
    Valor final {} R$'''.format(num , '10' , result))
    print('=' * 30) 

  def exercicio_8():
    print('=' * 30)
    print('''Vendedores:
    [ 1 ] João''')
    print('=' * 30)
    salario_fixo = float(input('Defina o salário fixo: R$ '))
    total_vendas = float(input('Total de vendas do vendedor: R$ '))
    percentual_vendas = float(input('Porcentagem sobre vendas: '))
    result = exer_8(percentual_vendas , total_vendas , salario_fixo )
    result = exer_8(percentual_vendas , total_vendas , salario_fixo)
    print('=' * 30)
    print(result)
    print('=' * 30)
            
  def exercicio_9():
    print('=' * 30)
    print('{:^30}'.format('Área Livre do terreno:'))
    print('=' * 30)
    print('{:^30}'.format('DIMENSÃO TERRENO'))
    print('=' * 30)
    base_retangulo = float(input('Defina a base do terreno: '))
    altura_retangulo = float(input('Defina a altura do terreno: '))
    print('=' * 30)
    print('{:^30}'.format('DIMENSÃO CASA:'))
    print('=' * 30)
    comprimento_casa = float(input('Defina o comprimento da casa: '))
    largura_casa = float(input('Defina a largura da casa: '))
    result = exer_9(base_retangulo , altura_retangulo , comprimento_casa , largura_casa)
    print('=' * 30) 
    print(result)
    print('=' * 30)

  def exercicio_10():
    print('=' * 30)
    print('{:^30}'.format('Saldo final'))
    print('=' * 30)
    deposito = float(input('Defina o valor do depósito: R$ '))
    print('Junin emitiu 2 cheques')
    cheque1 = float(input('Valor cheque 01: R$ '))
    cheque2 = float(input('Valor cheque 02: R$ '))
    saldo_final = exer_10(deposito , cheque1 , cheque2)
    print('=' * 30) 
    print('Saldo final {:.2f} R$'.format(saldo_final))
    print('=' * 30) 
  
  def exercicio_11():
    print('=' * 30)
    print('{:^30}'.format('BANCO ATM'))
    print('=' * 30)
    valor = int(input('Defina o valor da conta: R$ '))
    result = exer_11(valor)
    print(result)

  def exercicio_12():
    print('=' * 30)
    print('{:^30}'.format('Calculo do Salário Mínimo:')) 
    print('=' * 30)
    horas = int(input('Número de horas trabalhadas: '))
    salario = float(input('Valor Salário Minímo: R$ '))
    salario_receber = exer_12(horas , salario)
    print('=' * 30)
    print('O sálario a receber: R$ {:.2f}'.format(salario_receber))
    print('=' * 30)

  def exercicio_13():
    print('=' * 30)
    print('Salário atual e novo valor com reajuste de 5%:')
    print('=' * 30)
    salario_atual = float(input('Defina o salário atual: R$ '))
    result = exer_13(salario_atual)
    print('=' * 30)
    print(result)
    print('=' * 30)

  def exercicio_14():
    print('=' * 30)
    print('Viagem de Maria:')
    print('=' * 30)
    result = exer_14()
    print(result)
    print('=' * 30)

  def exercicio_15():
    total_alunos = int(input('Defina o número de alunos da sala A: '))
    result = exer_15(total_alunos)
    print('=' * 30)
    print(result)
    print('=' * 30)

  def exercicio_16():
    print('=' * 30)
    print('{:^30}'.format('Eleitores de Boa Esperança:'))
    print('=' * 30)
    total_cidadao = int(input('Total de cidadãos: '))
    total_eleitores = int(input('Total de eleitores: '))
    votos_brancos = float(input('Total de votos brancos: '))
    votos_nulos = float(input('Total de votos nulos: '))
    nao_votaram = float(input('Total que não votaram: '))
    print('=' * 30)
    result = exer_16(total_cidadao , total_eleitores , votos_brancos , votos_nulos , nao_votaram)
    print(result)
    print('=' * 30)

  def exercicio_17():
    print('=' * 30)
    print('{:^30}'.format('Compra na loja:'))
    print('=' * 30)
    valor_compra = int(input('Valor da compra: R$ '))
    print('=' * 30)
    print('''  Compra a vista = 10% desconto
    Compra a prazo = 3 parcelas c/ acréscimo de 5%''')
    result = exer_17(valor_compra)
    print(result)
    print('=' * 30)

  def exercicio_18():
    print('=' * 30)
    print('{:^30}'.format('QG MARINHA'))
    print('=' * 30)
    print('Funcionário José:')
    print('=' * 30)
    salario = float(input('Salário do funcionário: R$ '))
    anos_servico = int(input('Anos de serviço: '))
    posicao = input('Posição do funcionário: ')
    n_filhos = int(input('Número de filhos: '))
    print('=' * 30)
    result = exer_18(salario , anos_servico , posicao , n_filhos)
    print(result)
    print('=' * 30)

  def exercicio_19():
    print('=' * 30)
    print('{:^30}'.format('CUSTO PÃO FRANCÊS'))
    print('=' * 30)
    print('{:^30}'.format('INGREDIENTES'))
    print('=' * 30)
    farinha = float(input('Farinha(kg): '))
    agua = float(input('Água(lt): '))
    fermento = float(input('Fermento(g): '))
    print('=' * 30)
    print('{:^30}'.format('VALOR PRODUTOS'))
    print('=' * 30)
    p1 = float(input('Farinha(kg): R$ '))
    p2 = float(input('Água(lt): R$ '))     
    p3 = float(input('Fermento(g): R$ '))
    print('=' * 30)
    print('{:^30}'.format('CUSTOS FIXOS'))
    print('=' * 30)
    energia = float(input('Energia(kWh): kWh '))
    imposto = float(input('Imposto(%): % '))
    p4 = float(input('Valor kWh: R$ '))
    print('=' * 30)
    print('{:^30}'.format('TABELA DE CUSTO'))
    print('=' * 30)
    result = exer_19(farinha , agua , fermento , p1 , p2 , p3 , energia , imposto , p4)
    print(result)

  def exercicio_20():
    print('=' * 30)
    print('{:^30}'.format('HOTEL CALIFORNIA'))
    print('=' * 30)
    lotacao = int(75)
    diaria_normal = float(input('Valor da diária normal: R$ '))
    print('=' * 30)
    print('{:^30}'.format('SISTEMA HOTEL'))
    print('=' * 30)
    result = exer_20(diaria_normal , lotacao)
    result2 = exer_20_1(diaria_normal , lotacao)
    print(result)
    print(result2)
  
  def exercicio_21():
    print('=' * 30)
    print('{:^30}'.format('WELCOME TO WEBLANDs ATM'))
    print('=' * 30)
    valor = int(input('Valor a sacar: B$ '))
    print('=' * 30)
    print('{:^30}'.format('SACANDO'))
    print('=' * 30)
    result = exer_21(valor)
    print(result)
  
  def exercicio_22():
    print('=' * 30)
    print('{:^30}'.format('MEGA-SENA'))
    print('=' * 30)
    valor_arrecadado = float(input('Silvio qual o valor da Mega-Sena? R$ '))
    print('O valor ta no total de {} R$'.format(valor_arrecadado))
    print('=' * 30)
    result = exer_22(valor_arrecadado)
    print(result)
    print('=' * 30)
    print('Estes foram os ganhadores da Mega-Sena, uma boa noite telespectadores. Maoeeeeeee')

  def exercicio_23():
    print('=' * 30)
    print('{:^30}'.format('BANCO DISTRIBUIÇÃO'))
    print('=' * 30)
    valor = int(input('Valor a sacar: R$ '))
    print('=' * 30)
    print('{:^30}'.format('SACANDO'))
    print('=' * 30)
    result = exer_23(valor)
    print(result)

  #Medir um prédio com uma trena. GENIAL!!!!
  def exercicio_24():
    print('=' * 30)
    print('{:^30}'.format('ALTURA PRÉDIO'))
    print('=' * 30)
    sombra_predio = float(input('Defina o tamanho da sombra do prédio em mts: '))
    altura_eu = float(input('Defina a sua altura em mts: '))
    sombra_eu = float(input('Defina o tamanho da sua sombra em mts: '))
    result = altura_predio(altura_eu , sombra_predio , sombra_eu)
    print('A altura do prédio é: {} mts'.format(result))

  def exercicio_25():
    print('=' * 30)
    print('{:^30}'.format('BANCO DE DADOS'))
    print('=' * 30)
    n_ident = int(input('Número de identificação: '))
    print('''Bem vinda Professora JuhJuh
    N°: {}
    Cargo: Professora
    Hobbys: Assistir anime e programar
    '''.format(n_ident))
    aluno = input('Nome do Aluno: ')
    print('=' * 30)
    print('ALUNO {}'.format(aluno))
    print('=' * 30)
    nt1 = float(input('Nota 1: '))
    nt2 = float(input('Nota 2: '))
    nt3 = float(input('Nota 3: '))
    media_ex = float(input('Média dos exercícios: '))
    result = media_aproveitamento(nt1 , nt2 , nt3 , media_ex)
    print('=' * 30)
    print('MA = {:.2f}'.format(result))
    print('=' * 30)
    print('FINALIZANDO...')
  


main()
