# delta = b² - 4ac
# x1 = (-b + sqrt(delta))/2a
# x2 = (-b - sqrt(delta))/2a
# segundo_grau: ax² + bx + c = 0

from cmath import sqrt


a = int(input('Insira o parâmetro a: '))
b = int(input('Insira o parâmetro b: '))
c = int(input('Insira o parâmetro c: '))

delta = b**2 - 4*a*c
x1 = (-b + sqrt(delta))/2*a
x2 = (-b - sqrt(delta))/2*a


print(f'A primeira raíz dessa equação do segundo grau é {x1} e a segunda é {x2}.')

