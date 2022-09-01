aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('Informe o nome do quarto aluno: ')

nota1 = float(input('Informe a nota do primeiro aluno: '))
nota2 = float(input('Informe a nota do segundo aluno: '))
nota3 = float(input('Informe a nota do terceiro aluno: '))
nota4 = float(input('Informe a nota do quarto aluno: '))

lista = [{"nome": aluno1, "nota": nota1}, {"nome": aluno2, "nota": nota2}, {"nome": aluno3, "nota": nota3}, {"nome": aluno4, "nota": nota4}]
print(lista)

notas = []
for dicionario in lista:
    notas.append(dicionario.get("nota"))
    nota_max = max(notas)
        
print(nota_max)
    

    
    