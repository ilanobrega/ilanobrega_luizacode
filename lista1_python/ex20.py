valor_inicial_parcela = float(input('Informe o valor inicial da parcela: '))
valor_percentual_parcela = float(input('Informe o valor percentual da parcela: '))
quantidade_parcelas = int(input('Informe a quantidade de parcelas: '))

valor_anterior = valor_inicial_parcela


n = 1
while n <= quantidade_parcelas:
    valor_parcela = valor_anterior + (valor_anterior*valor_percentual_parcela)
    valor_anterior = valor_parcela
    print(f'Valor da parcela {n} é {valor_parcela}.')
    n += 1
