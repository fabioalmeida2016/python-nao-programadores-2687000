# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esses dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcorridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante = {}
estudante['nome'] = input('Qual seu nome? ')
estudante['ano_conheceu_linkedin'] = int(input('Quando conheceu o LinkedIn? '))
estudante['ano_atual'] = int(input('Em que ano estamos? '))
cursos = input('Quais cursos você já fez no Linkedin Learning? (separe-os com vígula) ')

estudante['cursos'] = cursos.split(', ')


total_anos = estudante['ano_atual'] - estudante['ano_conheceu_linkedin']

total_cursos = len(estudante['cursos'])
print(f"Oi {estudante['nome']}, visto que você conheceu o LinkedIn em {estudante['ano_conheceu_linkedin']}, há {total_anos} já realizou {total_cursos} cursos, sendo '{estudante['cursos'][0]}' o primeiro e '{estudante['cursos'][-1]}' o último.")