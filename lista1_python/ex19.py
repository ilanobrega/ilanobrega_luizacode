valor_venda = float(input('Informe o valor da venda: '))

if valor_venda <= 1000:
    print('Nenhuma comissão.')
elif 1000 < valor_venda <= 5000:
    comissao = valor_venda*0.1
    print(f'O valor da comissão é de {comissao} reais.')
elif 5000 < valor_venda <= 10000:
    comissao = valor_venda*0.2
    print(f'O valor da comissão é de {comissao} reais.')
elif 10000 < valor_venda <= 50000:
    comissao = valor_venda*0.25
    print(f'O valor da comissão é de {comissao} reais.')
elif valor_venda > 50000:
    comissao = valor_venda*0.3
    print(f'O valor da comissão é de {comissao} reais.')
    