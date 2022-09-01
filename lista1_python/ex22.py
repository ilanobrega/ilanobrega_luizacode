# Crie um script que leia 10 números inteiros positivos e que irá apresentar:
# ● A lista dos valores lidos de forma ordenada.
# ● A contagem de cada item. Por exemplo, se o usuário informou [1,1,1,1,2, 3],
# aqui apresentamos:
# ○ 1: 4x.
# ○ 2: 1x.
# ○ 3: 1x.
# ● Uma saída identificando o número, se o número é par e se é primo. Isto será feito
# separando por vírgulas: Por exemplo, se informou [1,2,3,6]. Iremos apresentar aqui:
# ○ 1,ímpar,não é primo
# ○ 2,par,é primo
# ○ 3,ímpar,é primo
# ○ 6,par,não é primo


from itertools import count


lista = list(input('Insira aqui sua lista: '))
lista_int = list(map(int, lista))
print(lista_int)

lista_append = sorted(lista_int)
print(f'Lista ordenada: {lista_append}')

for i in set(lista_int):
    contagem = lista_int.count(i)
    print(f'{i}: {contagem}x')
    
for i in lista_int:
    if i % 2 == 0:
        par_impar = 'par'
    else:
        par_impar = 'impar'
    
    if i == 1 or i == 0:
        primez = 'não é primo'
    else:
        mult = 0
        for numero in range(2, i):
            if (i % numero == 0):
                mult += 1
        
        if (mult == 0):
            primez = 'é primo'
        else:
            primez = 'não é primo'
            
    
    print(f'{i}, {par_impar}, {primez}')


# for i in lista_int:
#     lista_append.append(i)
    

# lista_append.sort()
# print(f'Lista ordenada: {lista_append}')

# for i in lista_append:
    