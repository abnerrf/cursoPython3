'''
SPLIT, JOIN, ENUMERATE em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
'''

string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
cont = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > cont:
        cont = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({cont}x)')

for valor in lista_2:
    print(valor.strip().upper())