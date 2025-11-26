# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esses dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}
estudante['nome'] = input('Qual seu nome? ')
estudante['ano_conheceu_linkedin'] = int(input('Quando conheceu o LinkedIn? '))
estudante['ano_atual'] = int(input('Em que ano estamos? '))
cursos_linkedIn = input('Quais cursos está realizando atualmente? ')

# 2. Armazene esses dados em um dicionário
estudante = {'nome','ano_conheceu_linkedin', 'ano_atual', 'cursos_linkedIn'}
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcorridos, total de cursos realizados e (apenas) o primeiro e último curso.
estudante['cursos_linkedIn'] = cursos_linkedIn.split(', ')
total_anos = estudante['ano_atual'] - estudante['ano_conheceu_linkedin']
total_cursos = len(estudante['cursos_linkedIn'])
print(f"Oi {estudante[0]}, visto que você conheceu o LinkedIn em {estudante['ano_conheceu_linkedin']}, há {estudante['ano_atual']- estudante['ano_conheceu_linkedin']} já realizou {total_cursos} cursos, sendo {estudante[cursos_linkedIn][0,-1]} o primeiro e último, respectivamente")