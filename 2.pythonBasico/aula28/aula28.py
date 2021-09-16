'''
OPERADOR TERNÁRIO EM PYTHON
'''
idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números.')
else:
    idade = int(idade)
    e_demaior = (idade >= 18)
    msg = 'Pode acessar' if e_demaior else 'Não pode acessar.'

    print(msg)