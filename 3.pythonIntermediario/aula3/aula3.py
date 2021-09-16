'''
FUNÇÕES (DEF) EM PYTHON - *args **kwargs -
'''

def func(*args):
    print(args)

lista = [1,2,3,4,5]
print(*lista)
print('')
#######################################
def funcao(*args):
    for v in args:
        print(v)

funcao(1,2,3,4,5)

#####################################

def teste(*args, **kwargs):
    print(args)
    nome = kwargs.get('nome')
    print(nome)
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade inexistente')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
teste(*lista, *lista2, nome='Abner', sobrenome='Rodrigues', idade=27)