'''
Luiz Eduardo Vieira Barreto 
29/02/2020

'''
#Funções
def ficha(nom , sex , idad , altur , pes):
  nome = nom
  sexo = sex
  idade = idad
  altura = altur
  peso = pes
  result = '''Nome: {}
  Sexo: {}
  Idade: {}
  Altura: {} cm
  Peso: {} kg '''.format(nome , sexo , idade , altura , peso)
  return result

def taxa_metabolica_basal(sex , peso , altura , idade ,):
  sexo = sex
  if sexo == 'Masculino' or sexo == 'masculino':
    tmb = 66 + 13.8 * (peso) + 5 * (altura) - 6.8 * (idade)
  else:
    tmb =  655 + 9.6 * (peso) + 1.8 * (altura) - 4.7 * (idade)
  return tmb

def atividade_fisica(taxa , opc):
  tmb = taxa 
  tipo = opc
  sedentario = 1.2 * tmb
  exercicio_leve = 1.375 * tmb
  exercicio_moderado = 1.55 * tmb 
  exercicio_intenso = 1.725 * tmb 
  exercicio_muito_intenso = 1.9 * tmb
  
  if tipo == 1:
    result = 'Gasto total diário: {:.2f} kcal'.format(sedentario)
  elif tipo == 2:
    result = 'Gasto total diário: {:.2f} kcal'.format(exercicio_leve)
  elif tipo == 3:
    result = 'Gasto total diário: {:.2f} kcal'.format(exercicio_moderado)
  elif tipo == 4:
    result = 'Gasto total diário: {:.2f} kcal'.format(exercicio_intenso)
  elif tipo == 5:
    result = 'Gasto total diário: {:.2f} kcal'.format(exercicio_muito_intenso)
  return result

def main():
  print('=' * 30)
  print('Ficha de inscrição do Aluno:')
  print('=' * 30)
  nome = input('Nome: ')
  sexo = input('Sexo: ')
  idade = int(input('Idade: ') )
  peso = int(input('Peso em kg: ' ) )
  altura = int(input('Altura em cm: ' ) )
  ficha(nome , sexo , idade , altura , peso)
  tmb = taxa_metabolica_basal(sexo , peso , altura , idade) 
  print('=' * 30)
  nivel_de_atividade_fisica = int(input('''Nível de Atividade Fisíca:
  
  [ 1 ] Sedentário(exercício mínimo)
  [ 2 ] Exercício Leve(1-3 dias por semana)
  [ 3 ] Exercício Moderado(3-5 dias por semana)
  [ 4 ] Exercício Intenso(6-7 dias por semana)
  [ 5 ] Exercício muito Intenso(atleta, 2 vezes por dia) 
  
  R= '''))
  print('=' * 30)
  print(atividade_fisica(tmb , nivel_de_atividade_fisica))
  print('=' * 30)

main()
 
