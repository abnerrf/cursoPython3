'''
OPERADORES LÓGICOS
AND, OR, NOT
IN E NOT IN
'''
a = 2
b = 3
nome = 'Abner.'

# COMPARAÇÃO AND OU OR
if a > b and a < b:
    print('Verdade')
else:
    print('Mentira')

if a > b or a < b:
    print('Verdade')
else:
    print('Mentira')

# NOT NEGA A LINHA
if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')

# IN
if 'n' in nome:
    print(f'Existe a letra N em {nome}')
else:
    print('Não Existe')