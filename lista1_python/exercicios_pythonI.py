# c1 = not True
# c2 = True and False
# c3 = False and 3>5
# c4 = True and 3>5
# c5 = 1+2 or 3+4
# c6 = 1 + 2 and 3 + 4
# print(c1)
# print(c2)
# print(c3)
# print(c4)
# print(c5)
# print(c6)

# letra a, numero 5
L = 2
A = L*L
print(f'A área do quadrado é de {A}cm²')

# letra b
mala = 120
desconto = 0.05
preco = mala*(1 - desconto)
print(f'O preço da mala é de R${preco}')

#letra c
VM = 100
D = 200
T = D/VM
print(f'{T}h')

#letra d
joao = 2
maria = 3
sofia = 1
total = joao + maria + sofia
media = total / 3
print(f'A média de pirulitos é de {media} pirulitos')

#letra e
davi = 13
irma = 7
eh_mais_velho = davi > irma
print(f'a resposta é {eh_mais_velho}')

#numero 6
z = (3+2)*6/5
print(z)

# numero 7
ovo = 3.4
caju = 12.4
resposta = 100 if ovo == 3 else 0
print(resposta)

#numero 9 
valor = input("Informe um valor: ")
print("Valor informado: ", valor)
tipo = type(valor)
print(tipo)
x_str = "123"
x = int(x_str)
xf = float(x)
sao_iguais = x == xf
print("Um float é igual a um int?", sao_iguais)