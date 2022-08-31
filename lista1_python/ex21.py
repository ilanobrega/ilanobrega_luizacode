prefixo = int(input('Informe o prefixo: '))
quantidade_numeros = int(input('Informe a quantidade de telefones: '))
 
print('Os números que deverão ser ligados são os seguintes: ')
n = 1
while n <= quantidade_numeros:
    lista = [0, 0, 0, n]
    n += 1
    sufixo = "".join([str(_) for _ in lista])
    print(f'{prefixo}-{sufixo}')



