'''
FORMATANDO VALORES COM MODIFICADORES
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0^10}')

num_3 = 452
print(f'{num_3:0<10}')

num_4 = 4278
print(f'{num_4:0>10.2f}')

nome = 'Abner'
sobrenome = 'Rodrigues'
nome_formatado = '{0:@>10}{1:#>17}'.format(nome, sobrenome)
print(nome_formatado)