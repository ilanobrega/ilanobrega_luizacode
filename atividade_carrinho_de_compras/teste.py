# id produto, id usuario, preço, quantidade

                #item 1             #item 2
carts = [['123', '1', 100.0, 2], ['456', '1', 899.00, 1]]

# carts[0][0]
## Olha carrinho eu quero o item onde o produto for o tenis adidas,
#que é o código 123

# new_lista = []
for item in carts:
    print(item) #vai aparecer as duas sublistas
    if item[0] == '123':
        new_lista = item #dessa maneira, não será uma sublista dentro de uma lista, apenas uma outra lista
        # new_lista.append(item)
        
print(new_lista)

new_list = [item for item in carts if item[0] == '123'] #item na primeira posição é o que será retornado
print(new_list[0]) #no método acima, a lista criada acessa uma sublista então é uma lista com sublista
# assim vc acessa a lista no índice 0, que é a sublista e retorna a lista sozinha
        
def filtra_item(item, product):
    if item[0] == '123':
        return item
    
# n_list = filter(lambda seq: filtra_item(seq, '123'), carts)

n_list = filter(lambda seq: filtra_item(seq, '123'), carts)
print(list(n_list))