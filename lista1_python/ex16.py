valor_emprestimo = float(input('Insira o valor emprestado pelo banco: '))
taxa = float(input('Insira a taxa cobrada em cima do empréstimo: '))
tempo = int(input('Quantidade de meses em que o empréstimo será pago: '))

valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)
print(f'O valor final a ser pago é de {valor_final} reais.')
