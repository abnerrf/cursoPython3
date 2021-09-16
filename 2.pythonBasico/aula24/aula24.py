'''
FOR / ELSE em Python
'''

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')