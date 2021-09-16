'''
ITERANDO STRINGS COM WHILE
'''
# Indices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
cont = 0

while cont < tamanho_frase:
    print(frase[cont], cont)
    cont += 1
