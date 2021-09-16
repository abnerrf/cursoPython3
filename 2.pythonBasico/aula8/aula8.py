'''
DESAFIO PRATICO
* Criar variaveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
'''

nome = 'Abner'
idade = 28
altura = 1.78
peso = 117.5
ano = 2021
imc = peso / (altura ** 2)
nasc = ano - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nasc}')