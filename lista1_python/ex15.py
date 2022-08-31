def divisao_luz(valor_conta, numero_pessoas):
    return valor_conta/numero_pessoas

valor_conta = float(input('Insira o valor da conta de energia: '))
numero_pessoas = int(input('Insira o número de pessoas na casa: '))
print(f'O valor que cada um deve pagar da conta de energia é de {divisao_luz(valor_conta, numero_pessoas)} reais.')