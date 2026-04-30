# Lista para armazena os dados dos alunos.

Turma = [1, 2, 3, 4, 5]

# Quantidade de alunos aprovados, reprovados e em análise.

qtd_alunos = int(input("Informe a quantidade de matriculados: "))

# Dados dos alunos.

for i in range(qtd_alunos):
    nome = input("informe o nome do aluno: ")

    idade = int(input("Informe a idade do aluno:"))

    frequência = float(input("informe a frequência do aluno:"))

    note = int(input("informe a nota do aluno: "))

    if idade < 18:
        print (f"Você é menor de idade para se matrícular. Matrícula negada.")
    elif note < 5:
        print (f"Sua note não atinge a nossa média mínima, negado.")
    elif note >= 9:
        print (f"Sua matrícula foi aprovada automaticamente. Seja bem vindo.")
    elif idade >= 18:
        print (f"Sua matrícula está sendo analisada. Aguarde o resultado.")
    else:
        print (f"Você não atinge nenhum requisito mínimo para se candidatar, negado.")
        