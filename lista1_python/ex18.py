nota = int(input('Informe a nota do aluno: '))

if nota in range(101):
    if nota > 60:
        print('Aluno aprovado!')
    else:
        print('Aluno reprovado.')
else:
    print('Nota inválida.')
