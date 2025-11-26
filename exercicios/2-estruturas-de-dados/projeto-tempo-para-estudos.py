# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:

# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input("Quem é você? ")
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = int(input("Quantos dias por semana você estuda? "))
# 3. Crie uma variável chamada "total_horas" e, usando o método input(), solicite a média de horas estudada por dia;
total_horas = float(input("Quantas horas por dia você estuda? "))
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input("Qual curso pretende ingressar? ")
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(f'{nome}, você estuda {total_horas * total_dias:.2f} horas por semana, parabéns!')
