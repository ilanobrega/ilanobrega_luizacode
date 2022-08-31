# semana = False
# feriado = True

# print(type(semana))
# print(type(feriado))

# var1 = 4.12
# var2 = 5.34

# if var2 >= var1:
#     print('maior')
# else:
#     print('menor')
    
# numero = 5

# numero += 7
# print(numero)

# numero = 5

# numero -= 2
# print(numero)

# numero = 5

# numero *= 2
# print(numero)

# numero = 5

# numero /= 15
# print(numero)

# numero = 5

# numero %= 3
# print(numero)

# num1 = 7
# num2 = 4

# if not(num1 < 30 and num2 < 8):
#     print('Inverte o resultado da condição entre os parâmetros')
# else:
#     print('não')

# lista = ['a', 'b', 'c', 'd'] 
# if 'c' not in lista:
#     print('não tem o c na lista')
# else:
#     print('tem o c na lista')

# def foo(value):
#     print(f'Olá, esse é o parâmetro: {value}')
    
# foo('Luizacode')

# from functools import reduce


# lista = [100, 248.90, 88, 124.90]

# def desconto(preco):
#     return preco*(1-0.1)

# lista_map = map(lambda x: desconto(x), lista)
# print(list(lista_map))

# maior_que_100 = filter(lambda x: x > 100, lista)
# print(list(maior_que_100))

# soma = reduce(lambda x, y: x+y, lista, 0)
# print(soma)

import time

def calcula_tempo(funcao):
    def wrapper():
        tempo_inicio = time.time()
        funcao()
        tempo_final = time.time()
        
        calculo = tempo_final - tempo_inicio
        
        print(f'A {funcao.__name__} levou o total de {calculo} p/ ser executada')
        
    return wrapper

@calcula_tempo
def run():
    for n in range(100000000000000):
        yield
run()
    
    
lista = [1, 2, 3, 4]

print(list(filter(lambda x: x%2 == 0, lista)))
print(list(map(lambda x: x ** 2, lista)))
    