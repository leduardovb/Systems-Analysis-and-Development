def conversor_binario():
  num = int(input('Digite um número: '))
  conta_1 = num
  binario = ''
  while conta_1 > 0:
    if conta_1 % 2 == 1:
      binario = '1' + binario
    elif conta_1 % 2 == 0:
      binario = '0' + binario 
    print(conta_1 , binario)
    conta_1 //= 2
  print('O número {} em Binário é: {}'.format(num , binario))

def main():
  conversor_binario()

main()
