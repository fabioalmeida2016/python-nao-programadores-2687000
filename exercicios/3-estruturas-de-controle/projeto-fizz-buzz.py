# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"
lista = []

for i in range(16):
  print(i)
  lista.append(i)

for i in lista:
  if i%3 == 0 and i%5 != 0 and i < 10:
      print(f'0{i} Fizz')
  else:
    print(f'{i} Fizz')

  if i%5 == 0 and i%3 != 0 and i < 10:
    print(f'0{i} Buzz')   
  else: 
    print(f'{i} Buzz')

  if i%3 == 0 and i%5 == 0:
    print(f'{i} FizzBuzz')
  elif i%3 != 0 and i%5 != 0 and i < 10:
      print(f'0{i} FizzBuzz')
  else:
    print(f'0{i} Buzz')  

else:
  if i < 10:
    print(f'0{i} não é divisível por 3 nem 5')
  else:
    print(f'{i} não é divisível por 3 nem 5')
