'''
FUNÇÕES - DEF EM PYTHON (PARTE 1)
'''
def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)
