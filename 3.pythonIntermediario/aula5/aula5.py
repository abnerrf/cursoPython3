'''
EXPRESSOES LAMBDA - PYTHON
'''

def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)
print(var)

a = lambda x, y: x * y  # ESSA FUNÇÃO É A MESMA COISA DA FUNÇÃO ACIMA
print(a(2,2))