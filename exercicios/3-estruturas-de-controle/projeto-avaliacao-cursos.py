# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro 
# deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
cursos = ['Programação', 'SQL', 'Excel', 'Ciência de dados', 'C+']
primeiro = 'Programação'
segundo = 'SQL'
terceiro = 'Excel'
nota = {}

if primeiro in cursos:
  print(f'O curso {primeiro} está no catálogo, avalie o curso.')
  nota[primeiro] = int(input('Dê uma nota de 0 a 5.' ))
if segundo in cursos:
  print(f'O curso {segundo} está no catálogo, avalie o curso.')
  nota[segundo] = int(input('Dê uma nota de 0 a 5.' ))
if terceiro in cursos:
  print(f'O curso {terceiro} está no catálogo, avalie o curso.')
  nota[terceiro] = int(input('Dê uma nota de 0 a 5.' ))
else: 
  print('Infelizmente nenhum curso está no catálogo.')

print(nota)
